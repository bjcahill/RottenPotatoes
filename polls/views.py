from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    movies = Movie.objects.all()[:10]

    context = {
        'movies': movies
    }

    return render(request, 'index.html', context)

def details(request, id):
    movie = Movie.objects.get(id=id)

    context = {
        'movie': movie
    }

    return render(request, 'details.html', context)
