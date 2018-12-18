from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


#have to register the user first, profile will be automatically created.
class UserRegisterForm(UserCreationForm):
#login: test123, password: louisliu1
    class Meta:
        model = User
        fields = ['username']
        widgets = {'username': forms.TextInput(attrs={'width': 10})}

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['linkedin', 'position']
