from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import NewUserForm

from users.models import Usermodel
from movies.models import Movie
from django.contrib.auth.models import User

import operator

def index(request):

  try:
    usermodel = Usermodel.objects.get(user_id=request.user.id)
  except:
    usermodel = None

  movies = Movie.objects.all()

  top_critic_movies = sorted(movies, key=operator.attrgetter('critic_score'))
  top_critic_movies = top_critic_movies[::-1][:3]
  top_user_movies = sorted(movies, key=operator.attrgetter('user_score'))
  top_user_movies = top_user_movies[::-1][:3]

  top_critic = top_critic_movies[0]
  top_user = top_user_movies[0]

  top_critic_image = top_critic_movies[0].image.url
  top_user_image = top_user_movies[0].image.url

  print(top_user_image)

  context = {
        'usermodel': usermodel,
        'top_critic_movies' : top_critic_movies,
        'top_user_movies' : top_user_movies,
        'top_critic' : top_critic,
        'top_user' : top_user,
        'top_critic_image' : top_critic_image,
        'top_user_image' : top_user_image,
  }
  
  return render(request, 'pages/newindex.html', context)

def signup(request):

    if not request.user.is_authenticated:
      error_message = "You do not have permission to view this page. You need to sign in with Google first."
      context = {'error_message' : error_message}
      return render(request, 'pages/errormessage.html',context=context)

    if request.user.is_superuser:
      error_message = "As an admin, you don't need to create an account!"
      context = {'error_message' : error_message}
      return render(request, 'pages/errormessage.html',context=context)

    try:
      currentUser = Usermodel.objects.get(user_id=request.user.id)
    except:

      if not request.method == "POST":
        form = NewUserForm(initial={'user_name': '',
                                    'first_name' : request.user.first_name,
                                    'last_name' : request.user.last_name,
                                    'email' : request.user.email})
        context = {'form': form}
        return render(request, 'pages/signup.html', context)
      
      form = NewUserForm(request.POST,request.FILES)

      if not form.is_valid():
        print(form.errors)
        context = {'form': form}
        return render(request, 'pages/signup.html', context)

      new_post = form.save(commit=False)
      new_post.user_id = request.user.id
      new_post.email = request.user.email

      current_username = new_post.user_name

      if " " in current_username:
        print(form.errors)
        context = {'form': form, 'message' : "Username cannot have space in it"}
        return render(request, 'pages/signup.html', context)

      new_post.save()

      return redirect('../')
    try:
      usermodel = Usermodel.objects.get(user_id=request.user.id)
    except:
      usermodel = None

    error_message = "There is no need for you to sign up! You already have an account here."
    context = {'usermodel' : usermodel, 'error_message' : error_message}
    return render(request, 'pages/errormessage.html',context=context)
