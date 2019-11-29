from django.shortcuts import render, redirect, render_to_response

from django.contrib import messages

from .models import Usermodel
from .models import *
from django.apps import apps
Review2 = apps.get_model('movies', 'Review2')

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
    reviews = Review2.objects.filter(user=request.user)

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
    reviews = Review2.objects.filter(critic=link)

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

         form = NewUserForm(instance=usermodel)

         context = {'form': form, 'oldusermodel' : usermodel.user_name}
         return render(request, 'settings.html', context)

       form = NewUserForm(request.POST,instance=usermodel)

       if not form.is_valid():
         print(form.errors)

         context = {'form': form, 'message' : form.errors, 'oldusermodel' : usermodel.user_name}
         return render(request, 'settings.html', context)

       form.save()

       return redirect('/users/' + usermodel.user_name)
    else:
       return render(request, 'pages/accessdenied.html')
