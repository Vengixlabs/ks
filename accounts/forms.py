from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupform(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                ' class': 'form-control',
                'placeholder': 'Name',
                'type':'text'
            }
        )
    )
    email= forms.EmailField(
          max_length=254,
        widget=forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Email',
                'type':'text'
            }
        )
    )
    password1 = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                ' class': 'form-control',
                'placeholder': 'Password',
                'type':'password'
            }
        )
    )
    password2 = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                ' class': 'form-control',
                'placeholder': 'password confirm',
                'type':'password'
            }
        )
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )