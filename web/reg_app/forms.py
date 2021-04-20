from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from . import models

class UserRegistrationForm(UserCreationForm):

    # we can set html attributes in the input tag of these form fields as shown below
    # email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'size': 10,}))
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User # form for the User model
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2'] # attributes of User model to be shown in the form


class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Profile # form for the Profile model
        fields = ['role', 'college', 'id_number'] 
