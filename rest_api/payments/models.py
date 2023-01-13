from django.db import models
from django.utils import timezone
# from orders import models as orders
# Create your models here.


class payments(models.Model):
    # order_details = models.ForeignKey(orders.order_details, default="",
    #                                   verbose_name="order_details", on_delete=models.SET_DEFAULT)
    amount = models.IntegerField(default=0)
    provider = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
