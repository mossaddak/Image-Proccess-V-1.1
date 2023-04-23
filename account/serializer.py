from rest_framework.serializers import ModelSerializer
from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from app.models import (
    ImageProcess
)
from app.serializer import(
    ImageProcessSerializer
)

class UserSerializer(ModelSerializer):
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
            "is_verified",
            #"image_to_image",
            "is_superuser",
        )

        extra_kwargs = {
           "password": {"write_only":True, "style":{"input_type": "password"} 
           } 
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
            email=validate_data["email"],
            profile_picture=validate_data["profile_picture"],
            
            
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

        print("data================================================", data)
        username = data['username']
        if not User.objects.filter(username = username).exists():
             raise serializers.ValidationError("Account not found")
        user = User.objects.filter(username=username)
        user = user[0]
        user.is_verified

        if user.is_verified == False:
            raise serializers.ValidationError("Account is not verified")
        print("NEwemial=================================", user.is_verified)
        return data
    
    
    def get_jwt_token(self, data):

        user = authenticate(username=data['username'], password=data['password'])
        print("user===========================================", user)

        if not user:
            return {
                'message':'invalid credentials',
                'data':{}
            }

        refresh = RefreshToken.for_user(user)
        return { 
                'message':'Login Success',
                'data':{
                    'token':{
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        "is_superuser":user.is_superuser,
                    }

                }
            }
