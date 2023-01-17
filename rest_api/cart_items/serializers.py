from rest_framework import serializers
from .models import cart_items


class cartSerializer(serializers.ModelSerializer):

    class Meta:
        model = cart_items
        fields = '__all__'
