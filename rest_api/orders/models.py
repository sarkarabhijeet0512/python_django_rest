from django.db import models
from users import models as users
from products import models as products
from payments import models as payments
from django.utils import timezone
# Create your models here.


class order_details(models.Model):
    user = models.ForeignKey(users.Users, default="",
                             verbose_name="user", on_delete=models.SET_DEFAULT)
    total = models.DecimalField(
        max_digits=2, decimal_places=2, default="", blank=True, verbose_name="total")
    payment = models.ForeignKey(payments.payments, default="",
                                verbose_name="order", on_delete=models.SET_DEFAULT)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)


class order_items(models.Model):
    order = models.ForeignKey(order_details,  default="",
                              verbose_name="order", on_delete=models.SET_DEFAULT)
    product = models.ForeignKey(products.Products, default="",
                                verbose_name="product", on_delete=models.SET_DEFAULT)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
