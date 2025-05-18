from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileUpdateForm, CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import ProfileUpdateForm
from django.contrib.auth.views import PasswordChangeView
# Create your views here.

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('homepage')  # Redirect to home after signup

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('homepage')  # Redirect to home after login


# @login_required
# def profile_view(request):
#     if request.method == 'POST':
#         profile_form = ProfileUpdateForm(request.POST, instance=request.user)
#         password_form = CustomPasswordChangeForm(request.user, request.POST)

#         if profile_form.is_valid() and password_form.is_valid():
#             profile_form.save()
#             user = password_form.save()
#             update_session_auth_hash(request, user)  # Keep the user logged in
#             messages.success(request, 'Profile updated successfully.')
#             return redirect('profile')
#     else:
#         profile_form = ProfileUpdateForm(instance=request.user)
#         password_form = CustomPasswordChangeForm(request.user)

#     return render(request, 'user/profile.html', {
#         'profile_form': profile_form,
#         'password_form': password_form
#     })



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'user/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user



class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/update_password.html'
    success_url = reverse_lazy('profile')  # Redirect to profile after success

