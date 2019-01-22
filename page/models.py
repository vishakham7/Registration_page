# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.

class User(models.Model):
    first_name = forms.CharField(max_length=100, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=100, required=False, help_text='Optional.')
    user_name = forms.CharField(max_length=100, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=100, help_text='Required. Inform a valid email address.')
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    gender = forms.CharField(max_length=30, required=False)
    Address = forms.CharField(max_length=500, widget=forms.Textarea)
    MobileNumber = forms.CharField(max_length=15)
  