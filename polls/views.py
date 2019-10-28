from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    movies = Movie.objects.all()[:10]

    context = {
        'movies': movies
    }

    return render(request, 'index.html', context)

def details(request, title):
    movie = Movie.objects.get(title=title)
    reviews = Review.objects.filter(movie=title)

    context = {
        'movie': movie,
        'reviews': reviews
    }

    return render(request, 'details.html', context)
