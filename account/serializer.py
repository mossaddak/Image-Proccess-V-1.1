from rest_framework.serializers import ModelSerializer
from .models import (
    User,
    ProfilePicture
)
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from app.models import (
    ImageProcess,
)
from app.serializer import(
    ImageProcessSerializer,
    PdfToImageSerializer
)
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password


def auto_user(set_email):
    provider = set_email.split("@")[1]
    usernames = {
        "gmail.com": "",
        "yahoo.com": "2",
        "hotmail.com": "3",
        "aol.com": "4",
        "outlook.com": "5",
        "icloud.com": "6",
        "protonmail.com": "7",
        "zoho.com": "8",
        "mail.com": "9",
        "gmx.com": "10",
    }

    # Generate the unique username based on the email provider
    if provider in usernames:
        username = set_email.split("@")[0] + usernames[provider]
    else:
        username = set_email.split("@")[0]

    return username


class ProfilePictureSerializer(ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = "__all__"


class UserSerializer(ModelSerializer):
    profile_picture = ProfilePictureSerializer(many=True, read_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        is_superuser = serializers.BooleanField(read_only=True)
        is_subscribed = serializers.BooleanField(read_only=True)
        is_verified = serializers.BooleanField(read_only=True)
        fields = [
            'id',
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_picture",
            "password",
            "is_superuser",
            "is_subscribed",
            "is_verified",
        ]


        extra_kwargs = {
           "password": {"write_only":True, "style":{"input_type": "password"}},
           "is_superuser": {"read_only": True}, 
        }

    def get_last_profile_picture(self, obj):
        try:
            last_profile_picture = obj.profile_picture.order_by('-id').first().profile_picture.url
        except:
            last_profile_picture = None
        return last_profile_picture

    def get_username(self, obj):
        return obj.username

    def validate(self, data):
        request = self.context.get('request')
        current_user_id = request.user.id if request and request.user else None
        if User.objects.filter(email = data['email']).exclude(id=current_user_id).exists():
             raise serializers.ValidationError("email already exist")
        return data

    def create(self, validate_data):
        email = validate_data["email"]
        username = auto_user(email)
        user = User.objects.create(
            username=username,
            first_name=validate_data["first_name"],
            last_name=validate_data["last_name"],
            password=validate_data["password"],
            email=email
        )
        user.set_password(validate_data["password"])
        user.save()
        return validate_data
    
class VeriFyAccountSerializer(serializers.Serializer):
    otp = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data['email']
        if not User.objects.filter(email = email).exists():
             raise serializers.ValidationError("Account not found")
        user = User.objects.filter(email=email)
        user = user[0]
        return data
    
    
    def get_jwt_token(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            return {
                'message': 'Invalid credentials',
                'data': {}
            }

        if not check_password(data['password'], user.password):
            return {
                'message': 'Invalid credentials',
                'data': {}
            }

        refresh = RefreshToken.for_user(user)
        print("Serializer data=====================================>",user)
        serialized_user = UserSerializer(user).data
        return { 
            'message': 'Login success',
            'data':serialized_user,
            'access': str(refresh.access_token),
            'is_superuser': user.is_superuser
        }
    



