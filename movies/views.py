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
        form = MovieForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = MovieForm()
        context = {'form': form}
        return render(request, 'submitMovie.html', context)

