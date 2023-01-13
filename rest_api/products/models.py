from django.db import models
from django.utils import timezone


# Create your models here.


class Product_Category(models.Model):
    name = models.CharField(max_length=20, default="", blank=True)
    description = models.TextField(max_length=255, default="", blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)


class Product_Inventory(models.Model):
    Quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)


class Discount(models.Model):
    name = models.CharField(max_length=20, default="", blank=True)
    description = models.TextField(max_length=255, default="", blank=True)
    discount_percent = models.DecimalField(
        max_digits=2, decimal_places=2, default="", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)


class Products(models.Model):
    name = models.CharField(max_length=20, default="", blank=True)
    description = models.TextField(max_length=255, default="", blank=True)
    SKU = models.CharField(max_length=10, default="", blank=True)
    category = models.ForeignKey(
        Product_Category, default="", verbose_name="category", on_delete=models.SET_DEFAULT)
    inventory = models.ForeignKey(
        Product_Inventory, default="", verbose_name="category", on_delete=models.SET_DEFAULT)
    discount = models.ForeignKey(
        Discount, default="", verbose_name="category", on_delete=models.SET_DEFAULT)
    price = models.IntegerField(default=0, verbose_name="price")
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
