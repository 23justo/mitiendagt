# Django
from django.shortcuts import render
from django.contrib.auth import views as auth_views

# Models
from django.contrib.auth.models import User
from stores.models import Store

# Create your views here.

class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'