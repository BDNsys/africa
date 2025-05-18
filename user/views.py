from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth.views import LoginView
# Create your views here.

class SignUpView(generic.CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name='user/signup.html'

class CustomLoginView(LoginView):
    authentication_form=CustomAuthenticationForm
    template_name = 'user/login.html'

