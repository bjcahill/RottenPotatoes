from django.shortcuts import *
from django.http import *
from .models import *
from .forms import *

def index(request):
    if 'search' in request.GET:
        search_term = request.GET['search']
        movies = Movie.objects.all().filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()

    context = {
        'movies': movies
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
    reviews = Review.objects.filter(movie=movie.title)

    context = {
        'movie': movie,
        'reviews': reviews
    }

    return render(request, 'details.html', context)

def submitMovie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('..')
    else:
        form = MovieForm()
        context = {'form': form}
        return render(request, 'submitMovie.html', context)

def submitReview(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../details/' + Movie.objects.get(title=request.POST['movie']).link);
    else:
        form = ReviewForm()
        context = {'form': form}
        return render(request, 'submitReview.html', context)
