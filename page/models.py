# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100, blank=False,default="vish")
    last_name = models.CharField(max_length=100, blank=False)
    user_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=10, blank=False)
    gender = models.CharField(max_length=30, blank=False)
    Address = models.CharField(max_length=500, blank=False)
    MobileNumber = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.user_name
  
class BankDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    AccountNumber = models.CharField(max_length=16, validators=[MinLengthValidator(14)], blank=False)
    AcoountType = models.CharField(max_length=20, blank=False)
    Region = models.CharField(max_length=100, blank=False)
    IFSCCode = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.user.user_name


    
