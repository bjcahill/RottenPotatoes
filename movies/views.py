from django.shortcuts import *
from django.http import *
from .models import *
from .forms import *

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

def submitMovie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            #Movie.objects.create(
            #    title=request.POST.get('title'),
            #    director=request.POST.get('director'),
            #    image=request.FILES.get('file'),
            #    star=request.POST.get('star'),
            #    score=request.POST.get('score'),
            #    runTime=request.POST.get('runTime'),
            #    rating=request.POST.get('rating'),
            #    releaseDate=request.POST.get('releaseDate'),
            #    studio=request.POST.get('studio'),
            #    link=request.POST.get('link'))
            form.save()
            return redirect('index')
    else:
        form = MovieForm()
        context = {'form': form}
        return render(request, 'submitMovie.html', context)
