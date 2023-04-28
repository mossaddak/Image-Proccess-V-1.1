import stripe
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import(
    Charge
)
from .serializer import(
    ChargeSerializer
)
from django.conf import settings

# Create your views here.

stripe.api_key = 'sk_test_51Mei6tA4Xf1XOr7ROyXtE7oBA3CUKjMg3jhpbjcc9EgCzFENvPxQfRxe0caqLIvHokpUNwLEazVeJMmkeHgW6G1y00fHxP7I11'

class StripePaymentView(APIView):
    def post(self, request):

        
        try:
            # Get the amount from the request data
            amount = request.data['amount']

            # Create a charge on Stripe
            charge = stripe.Charge.create(
                amount=int(amount * 100),
                currency='usd',
                source=request.data['token']
            )

            # Create a charge in the database
            charge_obj = Charge.objects.create(
                amount=amount,
                stripe_charge_id=charge.id,
                user=request.user
            )

            # Serialize and return the charge
            serializer = ChargeSerializer(charge_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


