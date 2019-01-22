from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class User(forms.Form):
    first_name = forms.CharField(max_length=500, required = True)

    last_name = forms.CharField(max_length=500,required = True)
    username = forms.CharField(max_length=500, required = True) 
    password = forms.CharField(widget = forms.PasswordInput())
    email = forms.EmailField(label='Enter email', required = True)
    SAMPLE_CHOICES = ['Male', 'female']
    Gender = forms.MultipleChoiceField(choices=SAMPLE_CHOICES, widget=forms.CheckboxSelectMultiple)
    Address = forms.CharField(widget=forms.Textarea)
    # validators should be a list
    MobileNumber = forms.CharField(max_length=12)


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email
 
    def clean_password(self):
        if re.search('[A-Z]', password)==None and re.search('[0-9]', password)==None and re.search('[^A-Za-z0-9]', password)==None:
            raise ValidationError(
                _("This password is not strong."),
                code='password_is_weak',
            )
   

    def clean_mobile(MobileNumber):

        valid_number_pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')

        is_valid = re.match(valid_number_pattern, MobileNumber)

        if not is_valid:
            return False
        else:
            return True

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
            self.cleaned_data['MobileNumber'],
        )
        return User