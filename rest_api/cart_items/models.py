from django.db import models
from products import models as products
from django.utils import timezone
# Create your models here.


class cart_items(models.Model):
    session = models.CharField(max_length=255)
    product = models.ForeignKey(products.Products, default="",
                                verbose_name="product", on_delete=models.SET_DEFAULT)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
