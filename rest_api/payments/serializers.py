from rest_framework import serializers
from .models import payments


class paymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = payments
        fields = '__all__'
