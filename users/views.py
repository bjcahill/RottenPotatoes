from django.shortcuts import render

from .models import Usermodel
from .models import *
from django.apps import apps
Review = apps.get_model('movies', 'Review')

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
    reviews = Review.objects.filter(critic=link)

    context = {
        'usermodel': usermodel,
        'reviews': reviews
    }

    return render(request, 'profile.html', context)
