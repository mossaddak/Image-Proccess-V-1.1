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


class ProfilePictureSerializer(ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = "__all__"

class UserSerializer(ModelSerializer):
    image_to_image = ImageProcessSerializer(many=True, read_only=True)
    pdf_to_image = PdfToImageSerializer(many=True, read_only=True)
    profile_picture = ProfilePictureSerializer(many=True, read_only=True)
    class Meta:
        #image_to_image = ImageProcessSerializer()
        model = User
        is_superuser = serializers.BooleanField(read_only=True)
        fields = (
            'id',
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_picture",
            "password",
            "is_superuser",
            "image_to_image",
            "pdf_to_image",
        )

        extra_kwargs = {
           "password": {"write_only":True, "style":{"input_type": "password"}},
           "is_superuser": {"read_only": True}, 
        }

    def validate(self, data):
        request = self.context.get('request')
        current_user_id = request.user.id if request and request.user else None
        if User.objects.filter(username = data['username']).exclude(id=current_user_id).exists():
             raise serializers.ValidationError("username already exist")
        
        return data
    
    def create(self, validate_data):
        user = User.objects.create(
            username=validate_data["username"],
            first_name=validate_data["first_name"],
            last_name=validate_data["last_name"],
            password=validate_data["password"],
            email=validate_data["email"]
            
            
        )
        print("End User======================", user)
        #user.set_password(validate_data["password"])
        user.set_password(validate_data["password"])
        user.save()

        return validate_data
    

class VeriFyAccountSerializer(serializers.Serializer):
    otp = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data['username']
        if not User.objects.filter(username = username).exists():
             raise serializers.ValidationError("Account not found")
        user = User.objects.filter(username=username)
        user = user[0]
        return data
    
    
    def get_jwt_token(self, data):
        user = authenticate(username=data['username'], password=data['password'])
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
        return { 
            'message': 'Login success',
            'data': {
                'token': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'is_superuser': user.is_superuser,
                }
            }
        }

