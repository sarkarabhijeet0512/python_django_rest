from django.db import models
from django.utils import timezone


# Create your models here.


class Users(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=5000)
    username = models.CharField(max_length=255, unique=True)
    telephone = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField("is_active", null=False,
                                    blank=False)
    created_at = models.DateTimeField("created_at", default=timezone.now)
    updated_at = models.DateTimeField("updated_at", default=timezone.now)

    def __str__(self):
        return self

    class Meta:
        verbose_name_plural = "Users"
        ordering = ['-created_at']
