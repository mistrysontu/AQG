from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.models import User

# Create your views here.

def register(request):

    if request.method == 'POST':
        u_form = forms.UserRegistrationForm(request.POST) # get the form data user has filled for User model
        p_form = forms.ProfileRegistrationForm(request.POST) # adding another form for extra profile info! Save in Profile model
        
        if u_form.is_valid() and p_form.is_valid():
            user_info = u_form.save() # save info in the User model
            profile_info = p_form.save(commit=False) # get the profile info. but dont save it as we need to link the user to the profile
            profile_info.user = user_info # link the user to the profile
            profile_info.save() # finally, save the info in the Profile model

            uname = u_form.cleaned_data.get('username') # get the data in the 'username' field
            messages.success(request, f'Account created successfully for {uname}. You can log in now!')
            return redirect('aqg-home')
    
    else: # initial access. form not filled yet.
        u_form = forms.UserRegistrationForm()
        p_form = forms.ProfileRegistrationForm() # another form for Profile model
    
    return render(request, "reg.html", {'registration_form': u_form, 'profile_form': p_form})
