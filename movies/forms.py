from django.forms import ModelForm
from django import forms
from .models import *

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title',
                  'director',
                  'image',
                  'star',
                  'runTime',
                  'rating',
                  'releaseDate',
                  'studio',
                  'link']

class TestMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title',)

class ReviewForm(ModelForm):

    score = forms.ChoiceField(choices=[(x, x) for x in range(0, 11)])

    class Meta:
        model = Review2
        fields = ['score', 'review']
        widgets = {
            'review' : forms.Textarea(attrs= {'class' : 'form-control', 'placeholder' : 'Enter text', 'style': 'depth: 500px'})
        }
