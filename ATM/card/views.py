

from django.shortcuts import render, redirect
from django.contrib.auth import logout

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import CustomUser


def home(request):
    context = CustomUser.objects.all()
    return render(request, 'webpage/home.html', {'context': context})

def profile(request): 
    context = CustomUser.objects.all()
    return render(request, 'webpage/profile.html', {'context': context})

def contact(request): 
    context = CustomUser.objects.all()
    return render(request, 'webpage/contact.html', {'context': context})

def base(request):
    return render(request, 'base.html')

def buy_data(request):
    return render(request, 'webpage/buy_data.html')

def buy_airtime(request):
    return render(request, 'webpage/buy_airtime.html')

def fund_account(request):
    return render(request, 'webpage/fund_account.html') 

def signup(request):
  if request.method == 'POST':
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      username = request.POST['username']
      email = request.POST['email']
      birthday_date = request.POST['birthday_date']
      location = request.POST['location']
      password = request.POST['password']
      confirm_password = request.POST['confirm_password']

      if password == confirm_password:
          if User.objects.filter(email=email).exists():
              messages.info(request, 'Email Already Used')
              return redirect('signup')
          elif User.objects.filter(username=username).exists():
              messages.info(request, 'Username Already Used')
              return redirect('signup')
          else:
              user = User.objects.create_user(username=username, password=password, last_name=last_name, first_name=first_name)
              user.save()
              return redirect('login')
      else:
          messages.info(request, 'Password Not The Same')
          return redirect('signup')
  else:
      return render(request, 'authentication/signup.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.info(request, 'invalid credentials')
        return redirect('login')
  else:
    return render(request, 'authentication/login.html')


def sign_out(request):
    auth.logout(request)
    return redirect('/')