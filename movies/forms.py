from django.forms import ModelForm
from django import forms
from .models import *

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        year=['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000'
        , '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010'
            , '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
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
            'runTime' : forms.NumberInput(attrs= {'class' : 'form-control', 'step': 1, 'style': 'width: 300px'}),
            'studio' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Enter text', 'style': 'width: 300px'}),
            'releaseDate' : forms.SelectDateWidget(attrs= {'class' : 'form-control', 'style': 'width: 300px'}, years=year),
            'inTheater' : forms.CheckboxInput(attrs= {'class' : 'form-control', 'style': 'width: 20px'}),
            'rating' : forms.Select(attrs= {'class' : 'form-control', 'style': 'height : 120px', 'style': 'width: 300px'}),
        }
        labels = {
        "runTime": "Runtime",
        "releaseDate" : "Release Date",
        "inTheater" : "In Theaters?",
        "image" : "Movie Poster",
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
