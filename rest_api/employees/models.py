from django.db import models

# Create your models here.


class employees(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    emp_id = models.IntegerField(default=0)

    def __str__(self):
        return self.firstname
