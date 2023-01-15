from rest_framework import serializers
from .models import Products, Discount, Product_Inventory, Product_Category


class productsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products, Discount, Product_Inventory, Product_Category
        fields = '__all__'
