from django.shortcuts import render

from .models import Usermodel
from .models import *

# Get users and display them

from django.contrib.auth import logout as auth_logout

def index(request):
   usermodels = Usermodel.objects.all()

   context = {
      'usermodels' : usermodels
   }

   return render(request, 'users/index.html', context)

def logout(request):
   logout(request)

def profile(request, link):
    usermodel = Usermodel.objects.get(user_name=link)

    context = {
        'usermodel': usermodel,
    }

    return render(request, 'profile.html', context)