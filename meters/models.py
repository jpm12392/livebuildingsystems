from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


## User Model class.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True)
    is_staff = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
   
    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['email',]),
        ]


## Meters Models.
class Meter(models.Model):
    name = models.CharField(max_length=200, unique=True)  ## meter label name.

    class Meta:
        db_table = 'meters'
        indexes = [
            models.Index(fields=['name',]),
        ]


## Meter Data Models
class MeterData(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)  ## Meter ForeignKey.
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()

    class Meta:
        db_table = 'meter_data'
        indexes = [
            models.Index(fields=['meter',]),
        ]
