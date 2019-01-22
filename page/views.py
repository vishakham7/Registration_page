from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import User

def user_register(request):
    template = 'register.html'
    
    if request.method == 'POST':
        
        form = User(request.POST)
        
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Email already exists.'
                })
            elif User.objects.filter(password=form.cleaned_data['password']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'password already exists.'
                })
            if User.objects.filter(firstname=form.cleaned_data['first_name']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'firstname already exists.'
                })

            if User.objects.filter(lastname=form.cleaned_data['lastname']).exists():
                return render(request, template, {
                    'form': form,   
                    'error_message': 'lastname already exists.'
                })
            if User.objects.filter(MobileNumber=form.cleaned_data['MobileNumber']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'MobileNumber already exists.'
                })
            else:
                # Create the user: 
                user = User.objects.create_user(
                    form.cleaned_data['username'], 
                    form.cleaned_data['email'], 
                    form.cleaned_data['password']
                )
               
                
                user.username = form.cleaned_data['username']
                user.password = form.cleaned_data['password']
             
                user.email = form.cleaned_data['email']
                user.save()
      
                login(request, user)
                return render(request, 'success.html', {})
              

   
    else:
        form = User()

    return render(request, 'register.html', {'form': form})