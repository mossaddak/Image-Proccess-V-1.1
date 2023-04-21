from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import(
    User
)


#serializer
from .serializer import(
    UserSerializer,
    VeriFyAccountSerializer,
    LoginSerializer
)

#otp verification
from .otp_send import send_otp_via_email

from rest_framework_simplejwt.tokens import RefreshToken



# Create your views here.
class SingUp(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if not serializer.is_valid():
                return Response(
                    {
                        'message':"something Went Wrong",
                        'data':serializer.errors
                    },status = status.HTTP_400_BAD_REQUEST
                )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    { 
                        'message':"Your account is created, to verify check your mail. An email is sent.",
                        'data':serializer.data,
                        'mail':send_otp_via_email(serializer.data['email']),
                    },status = status.HTTP_201_CREATED
                )
        
        except Exception as e:
            print(e)
            return Response(
                    {
                        'message':"something Went Wrong",
                        'message':serializer.errors,
                    },status = status.HTTP_400_BAD_REQUEST
                    
                )
        

class VerifyOTPview(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VeriFyAccountSerializer(data=data)
            
            if serializer.is_valid():
                otp = serializer.data['otp']
                user = User.objects.filter(otp=otp)

                # if user.filter(verified=False).exists():
                #print("OTPUser=====================================>", user)
                if not user.exists():
                    return Response(
                        {
                            'message':"You didn't create account yet, please create an account",
                            'error':"User not found"
                        },status = status.HTTP_404_NOT_FOUND
                    )
                print("OTPUser=====================================>", user)
                if not user[0].otp == otp:
                    return Response(
                        {
                            'message':"Please give here correct OTP",
                            'error':"Wront OTP"
                        },status = status.HTTP_404_NOT_FOUND
                    )
                user = user[0]
                if user.is_verified == False:
                
                    user.is_verified = True
                    user.otp=""
                    user.save()

                    #print("OTPemail=====================================",user[0].verified)
                    refresh = RefreshToken.for_user(user)
                    return Response(
                        {
                            'message':"Your account is verified now. Wellcome to RVK.",
                            'data':serializer.data,
                            'token':{
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                            }
                            
                        },status = status.HTTP_201_CREATED
                    )
                else:
                    return Response(
                        {
                            'message':"Your already verified your account"
                        },status = status.HTTP_201_CREATED
                    )

            
        except Exception as e:
            print("Error=======================================", e)


class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if not serializer.is_valid():
                return Response(
                    {
                        'data':serializer.errors,
                        'message':"something Went Wrong"
                    },status = status.HTTP_400_BAD_REQUEST
                )
            response = serializer.get_jwt_token(serializer.data)
            return Response(response,status = status.HTTP_200_OK)

        except Exception as e:
            return Response(
                    {
                        'error':e,
                        'message':"something Went Wrong"
                    },status = status.HTTP_400_BAD_REQUEST
                )