from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import NewUserForm

from users.models import Usermodel

def index(request):

  try:
    usermodel = Usermodel.objects.get(user_id=request.user.id)
  except:
    usermodel = None

  context = {
        'usermodel': usermodel,
  }
  
  return render(request, 'pages/index.html', context)

def signup(request):

    if not request.user.is_authenticated:
      return render(request, 'pages/notsignedin.html')

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
      
      form = NewUserForm(request.POST)

      if not form.is_valid():
        print(form.errors)
        return redirect('../movies')

      new_post = form.save(commit=False)
      new_post.user_id = request.user.id
      new_post.email = request.user.email
      new_post.save()

      return redirect('../')

    return render(request, 'pages/alreadyhaveaccount.html')
