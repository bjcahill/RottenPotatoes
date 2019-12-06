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

   try:
      usermodel = Usermodel.objects.get(user_id=request.user.id)
   except:
      usermodel = None

   if request.user.is_superuser:
      error_message = "As an Admin, you don't have a user profile and thus viewing this page is pointless."
      context = {'usermodel' : usermodel, 'error_message' : error_message}
      return render(request, 'pages/errormessage.html',context=context)

   if not request.user.is_authenticated:
      return redirect('..')
      # error_message = "You do not have permission to view this page. You need to sign in with Google first."
      # context = {'usermodel' : usermodel, 'error_message' : error_message}
      # return render(request, 'pages/errormessage.html', context=context)

   try:
      Usermodel.objects.get(user_id=request.user.id)
      has_profile = True
      usermodel = Usermodel.objects.get(user_id=request.user.id)
   except:
      has_profile = False
      usermodel = None

   if has_profile:

      usermodels = Usermodel.objects.all()

      context = {
         'usermodels' : usermodels,
         'usermodel' : usermodel
      }

      name = usermodel.user_name

      return redirect('../../../users/' + name)

   else:

      return redirect('../signup')

def logout(request):
   logout(request)

def profile(request, link):
    page_usermodel = Usermodel.objects.get(user_name=link.replace("%20", " "))
    page_user = page_usermodel.user
    reviews = list(reversed(Review2.objects.filter(user=page_user)))

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

       form = NewUserForm(request.POST,request.FILES, instance=usermodel)

       if not form.is_valid():
         context = {'form': form, 'oldusermodel' : usermodel.user_name}
         return render(request, 'settings.html', context)

       new_post = form.save(commit=False)
       current_username = new_post.user_name

       if " " in current_username:

         context = {'form': form, 'message' : "Username cannot have space in it", 'oldusermodel' : usermodel.user_name}
         return render(request, 'settings.html', context)

       new_post.save()

       return redirect('/users/' + usermodel.user_name)
    else:
      error_message = "You do not have access to this page. Unlucky."
      context = {'usermodel' : usermodel, 'error_message' : error_message}
      return render(request, 'pages/errormessage.html',context=context)
