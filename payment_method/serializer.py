from rest_framework import serializers
from .models import Charge

class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = ('id', 'amount', 'created', 'stripe_charge_id', 'user')