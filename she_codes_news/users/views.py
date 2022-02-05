from multiprocessing import context
from re import template
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()
# Create your views here.
class ProfileView(generic.DetailView):
    model = USER_MODEL
    template_name = 'users/profile.html'
    context_object_name = 'user'
