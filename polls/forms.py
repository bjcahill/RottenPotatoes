from django.forms import ModelForm
from .models import *

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
