from rest_framework import serializers
from .models import order_details, order_details


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = order_details, order_details
        fields = '__all__'
