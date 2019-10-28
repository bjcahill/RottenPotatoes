from django.shortcuts import render

from .models import Usermodel

# Get users and display them

from django.contrib.auth import logout as auth_logout

def index(request):
   return render(request, 'users/index.html')

def logout(request):
   logout(request)