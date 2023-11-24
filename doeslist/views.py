from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView, LogoutView,
from django.http import HttpResponse
from.models import Job, Custom_User


# Create your views here.
