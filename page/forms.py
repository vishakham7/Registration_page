from django import forms
from .models import User

class PersonForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

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