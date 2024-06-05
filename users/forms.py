
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# authentication/forms.py

#class LoginForm(forms.Form):
#    username = forms.CharField(max_length=63)
#    password = forms.CharField(max_length=63, widget=forms.PasswordInput)