from django.shortcuts import render, redirect

from .models import Usermodel
from .models import *
from django.apps import apps
Review = apps.get_model('movies', 'Review')

from pages.forms import NewUserForm

# Get users and display them

from django.contrib.auth import logout as auth_logout

def index(request):

   if request.user.is_superuser:
      return render(request, 'pages/nopoint.html')

   if not request.user.is_authenticated:
      return render(request, 'pages/notsignedin.html')

   try:
      Usermodel.objects.get(user_id=request.user.id)
      has_profile = True
      print("user has a profile")
      usermodel = Usermodel.objects.get(user_id=request.user.id)
   except:
      has_profile = False
      print("user does not have a profile")
      usermodel = None

   if has_profile:

      usermodels = Usermodel.objects.all()

      context = {
         'usermodels' : usermodels,
         'usermodel' : usermodel
      }

      return render(request, 'userdefault.html', context)

   else:

      return redirect('../signup')

def logout(request):
   logout(request)

def profile(request, link):
    page_usermodel = Usermodel.objects.get(user_name=link)
    reviews = Review.objects.filter(critic=link)

    try:
      usermodel = Usermodel.objects.get(user_id=request.user.id)
    except:
      usermodel = None

    context = {
        'page_usermodel': page_usermodel,
        'usermodel' : usermodel,
        'reviews': reviews
    }

    return render(request, 'profile.html', context)

def settings(request, link):

    page_usermodel = Usermodel.objects.get(user_name=link)
    reviews = Review.objects.filter(critic=link)

    try:
      usermodel = Usermodel.objects.get(user_id=request.user.id)
    except:
      usermodel = None

    context = {
        'page_usermodel': page_usermodel,
        'usermodel' : usermodel,
        'reviews': reviews
    }

    if page_usermodel == usermodel:
       if not request.method == "POST":
         form = NewUserForm(initial={'user_name': usermodel.user_name,
                                    'first_name' : usermodel.first_name,
                                    'last_name' : usermodel.last_name,
                                    'email' : usermodel.email,
                                    'image' : usermodel.image})
         context = {'form': form}
         return render(request, 'settings.html', context)
      
       form = NewUserForm(request.POST)

       if not form.is_valid():
         print(form.errors)
         return redirect('../')

       form.save()

       return redirect('../')
    else:
       return render(request, 'pages/accessdenied.html')

    

