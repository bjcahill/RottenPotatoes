from django.forms import ModelForm
from .models import *

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title',
                  'director',
                  'image',
                  'star',
                  'score',
                  'runTime',
                  'rating',
                  'releaseDate',
                  'studio',
                  'link']

class TestMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title',)
