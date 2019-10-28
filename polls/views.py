from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    movies = Movie.objects.all()[:10]

    context = {
        'movies': movies
    }

    return render(request, 'index.html', context)

def details(request, link):
    movie = Movie.objects.get(link=link)
    reviews = Review.objects.filter(movie=movie.title)

    context = {
        'movie': movie,
        'reviews': reviews
    }

    return render(request, 'details.html', context)
