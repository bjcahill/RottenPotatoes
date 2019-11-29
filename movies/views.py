from django.shortcuts import *
from django.http import *
from .models import *
from .forms import *

from users.models import Usermodel

def index(request):
    if 'search' in request.GET:
        search_term = request.GET['search']
        movies = Movie.objects.all().filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()

    try:
        usermodel = Usermodel.objects.get(user_id=request.user.id)
    except:
        usermodel = None

    context = {
        'movies': movies,
        'usermodel' : usermodel
    }

    return render(request, 'index.html', context)

def search(request, term):
    movies = Movie.objects.all()

    context = {
        'movies': movies
    }

    return (render, 'index.html', context)


def details(request, link):
    movie = Movie.objects.get(link=link)
    user_reviews = Review2.objects.filter(movie=movie.title,review_type = False)
    critic_reviews = Review2.objects.filter(movie=movie.title,review_type = True)
    try:
        usermodel = Usermodel.objects.get(user_id=request.user.id)
    except:
        usermodel = None

    context = {
        'movie': movie,
        'user_reviews' : user_reviews,
        'critic_reviews' : critic_reviews,
        'usermodel' : usermodel
    }

    return render(request, 'details.html', context)

def submitMovie(request):
    try:
        usermodel = Usermodel.objects.get(user_id=request.user.id)
    except:
        usermodel = None

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('..')
    else:
        form = MovieForm()
        context = {'form': form, 'usermodel' : usermodel}
        return render(request, 'submitMovie.html', context)

def submitReview(request,link):
    movie = Movie.objects.get(link=link)

    if not request.user.is_authenticated:
        return render(request, 'pages/accessdenied.html')

    try:
        usermodel = Usermodel.objects.get(user_id=request.user.id)
    except:
        usermodel = None

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():

            movie = Movie.objects.get(link=link)

            new_post = form.save(commit=False)
            new_post.movie = movie
            new_post.critic = usermodel.user_name
            new_post.user_id = request.user.id
            new_post.review_type = True if usermodel.critic else False
            new_post.save()

            movie.reviews += 1
            movie.aggScore += float(request.POST['score'])
            movie.score = movie.aggScore / movie.reviews
            movie.save()

            return redirect('../../details/' + movie.link);
        else:
            return redirect("/")
    else:
        form = ReviewForm()
        context = {'form': form, 'usermodel' : usermodel, 'movie' : movie, 'type' : "Critic" if usermodel.critic else "User"}
        return render(request, 'submitReview.html', context)

def nowplaying(request):

    try:
        usermodel = Usermodel.objects.get(user_id=request.user.id)
    except:
        usermodel = None

    context = {'usermodel' : usermodel,}

    return render(request, 'nowplaying.html', context)
