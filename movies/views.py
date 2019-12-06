from django.shortcuts import *
from django.http import *
from .models import *
from .forms import *

import operator
from django.template.defaultfilters import slugify

from users.models import Usermodel
from movies.models import Review2

def index(request):
    movies = Movie.objects.all()
    searched = False
    search_term = "hi"

    if 'sort2' in request.GET:
        movies = sorted(movies, key=operator.attrgetter('title'))
    elif 'sort1' in request.GET:
        movies = sorted(movies, key=operator.attrgetter('critic_score'))
        movies = movies[::-1]

    if 'search' in request.GET:
        search_term = request.GET['search']
        movies = Movie.objects.all().filter(title__icontains=search_term)
        searched = True

    try:
        usermodel = Usermodel.objects.get(user_id=request.user.id)
    except:
        usermodel = None

    context = {
        'movies': movies,
        'usermodel' : usermodel,
        'searched' : searched,
        'term' : search_term
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
    user_reviews = list(reversed(Review2.objects.filter(movie=movie.title,review_type = False)))[:3]
    critic_reviews = list(reversed(Review2.objects.filter(movie=movie.title,review_type = True)))[:3]
    print(critic_reviews)
    print(user_reviews)
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
        link = slugify(request.POST['title'])

        if form.is_valid():
            obj = form.save(commit = False)
            obj.creator = request.user
            obj.link = slugify(link)
            obj.save()
            return redirect('..')
    else:
        form = MovieForm()
        context = {'form': form, 'usermodel' : usermodel}
        return render(request, 'submitMovie.html', context)

def submitReview(request,link):
    movie = Movie.objects.get(link=link)

    if not request.user.is_authenticated or request.user.is_superuser:
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

            if not usermodel.critic:

                movie.user_reviews += 1
                movie.user_aggScore += float(request.POST['score'])
                movie.user_score = movie.user_aggScore / movie.user_reviews
                movie.save()

            else:

                movie.critic_reviews += 1
                movie.critic_aggScore += float(request.POST['score'])
                movie.critic_score = movie.critic_aggScore / movie.critic_reviews
                movie.save()


            return redirect('../../details/' + movie.link);
        else:
            return redirect("/")
    else:
        form = ReviewForm()
        context = {'form': form, 'usermodel' : usermodel, 'movie' : movie, 'type' : "Critic" if usermodel.critic else "User"}
        return render(request, 'submitReview.html', context)

def nowplaying(request):
    movies = Movie.objects.all().filter(inTheater = True)
    searched = False
    search_term = "hi"

    if 'sort2' in request.GET:
        movies = sorted(movies, key=operator.attrgetter('title'))
    elif 'sort1' in request.GET:
        movies = sorted(movies, key=operator.attrgetter('critic_score'))
        movies = movies[::-1]


    if 'search' in request.GET:
        search_term = request.GET['search']
        movies = movies.filter(title__icontains=search_term)
        searched = True

    try:
        usermodel = Usermodel.objects.get(user_id=request.user.id)
    except:
        usermodel = None

    context = {
        'movies': movies,
        'usermodel' : usermodel,
        'searched' : searched,
        'term' : search_term
    }

    return render(request, 'nowplaying.html', context)

def allReviews(request,link,review_type):
    movie = Movie.objects.get(link=link)

    type_boolean = True if review_type == "critic" else False

    reviews = list(reversed(Review2.objects.filter(movie = movie,review_type = type_boolean)))
    print(reviews)

    try:
        usermodel = Usermodel.objects.get(user_id=request.user.id)
    except:
        usermodel = None

    context = {'usermodel' : usermodel, 'reviews' : reviews, 'movie' : movie, 'review_text' : "Critic" if review_type == "critic" else "User", 'review_type' : type_boolean}

    return render(request, 'allReviews.html', context)
