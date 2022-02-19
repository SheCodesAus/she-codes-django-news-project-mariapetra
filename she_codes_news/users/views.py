# from multiprocessing import context
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
from django.views import generic
from django.contrib.auth import get_user_model
from news.models import NewsStory
from .forms import CustomUserChangeForm
USER_MODEL = get_user_model()
# Create your views here.
class ProfileView(generic.DetailView):
    model = USER_MODEL
    template_name = 'users/profile.html'
    context_object_name = 'customuser'  

class CreateAccountView(generic.CreateView):
     form_class = CustomUserCreationForm
     success_url = reverse_lazy('login')
     template_name = "users/createAccount.html"

class AmmendProfileView(generic.UpdateView):
    model = USER_MODEL
    form_class = CustomUserChangeForm
    template_name = "users/ammendProfile.html"
    def get_success_url(self) -> str:
        return reverse_lazy('users:profile', kwargs={'pk':self.object.id})