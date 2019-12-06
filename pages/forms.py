from django import forms

from users.models import Usermodel

class NewUserForm(forms.ModelForm):
    class Meta:
        model = Usermodel
        fields = ['user_name', 'first_name','last_name', 'email', 'image','critic']
        widgets = {
            'user_name' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Enter text', 'style': 'width: 300px'}),
            'first_name' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Enter text', 'style': 'width: 300px'}),
            'last_name' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Enter text', 'style': 'width: 300px'}),
            'email' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Enter text', 'style': 'width: 300px'})
        }
        labels = {
        "image" : "Profile Picture",
        "critic" : "Certified Critic?"
                 }