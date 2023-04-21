from rest_framework import (
    generics,
    status,
    viewsets,
    response
)

from django.conf import settings
from account.models import (
    User
)



from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .serializer import(
    EmailSerializer,
    ResetPasswordSerializer
)

from django.core.mail import send_mail
from django.conf import settings 
from django.template.loader import render_to_string
from django.core.mail import EmailMessage



class PasswordReset(generics.GenericAPIView):
    """
    Request for Password Reset Link.
    """

    serializer_class = EmailSerializer

    def post(self, request):
        """
        Create token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]


        print("email==============================================", email)
        user = User.objects.filter(email=email).first()


        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user) 

            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )

            rest_link = f"http://127.0.0.1:8000{reset_url}"
            mydict = {
                'rest_link':rest_link
            }

            html_template = 'email.html'
            html_message = render_to_string(html_template, context=mydict)

            subject = 'Your forget password link'
            
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]

            message = EmailMessage(subject, html_message, email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()


            return response.Response(
                {
                    "message": "Please check your mail an email is sent.",
                    "reset_link": rest_link,
                    "encoded_pk":encoded_pk,
                    "token":token

                },
                status=status.HTTP_200_OK,
            )
        else:
            return response.Response(
                {"message": "User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        

class ResetPasswordAPI(generics.GenericAPIView):
    """
    Verify and Reset Password Token View.
    """

    serializer_class = ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        """
        Verify token & encoded_pk and then reset the password.
        """
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )