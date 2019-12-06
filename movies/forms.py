from django.forms import ModelForm
from django import forms
from .models import *

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title',
                  'director',
                  'star',
                  'studio',
                  'runTime',
                  'rating',
                  'releaseDate',
                  'inTheater',
                  'image']
        widgets = {
            'title' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Enter text', 'style': 'width: 300px'}),
            'director' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Enter text', 'style': 'width: 300px'}),
            'star' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Enter text', 'style': 'width: 300px'}),
            'runTime' : forms.NumberInput(attrs= {'class' : 'form-control', 'step': 5, 'style': 'width: 300px'}),
            'studio' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Enter text', 'style': 'width: 300px'}),
            'releaseDate' : forms.SelectDateWidget(attrs= {'class' : 'form-control', 'style': 'width: 300px'}),
            'inTheater' : forms.CheckboxInput(attrs= {'class' : 'form-control', 'style': 'width: 20px'}),
            'rating' : forms.Select(attrs= {'class' : 'form-control', 'style': 'height : 120px', 'style': 'width: 300px'}),
        }

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
