from django.shortcuts import render, get_object_or_404
from . import models
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.contrib.auth import mixins
from django.urls import reverse
from django.contrib.auth.models import User
import os

# Create your views here.

@login_required
def home(request):
    context = {}
    context['posts'] = 'fofo' #models.Post.objects.all()
    return render(request, 'home.html', context)