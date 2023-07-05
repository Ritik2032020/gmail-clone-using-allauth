from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired URL name

    password_reset_form = PasswordResetForm()
    if request.method == 'POST' and 'reset_password' in request.POST:
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': default_token_generator,
                'from_email': None,
                'email_template_name': 'registration/password_reset_email.html',
                'subject_template_name': 'registration/password_reset_subject.txt',
                'request': request,
            }
            password_reset_form.save(**opts)
            return redirect('password_reset_done')  # Replace 'password_reset_done' with your desired URL name

    return render(request, 'registration/login.html', {'password_reset_form': password_reset_form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now login.')
            return redirect('login')  # Replace 'login' with the appropriate URL name for the login page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def home_view(request):
    return redirect('home')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('password_reset_done')  # Replace 'password_reset_done' with the appropriate URL name for the password reset done page

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')  # Replace 'password_reset_complete' with the appropriate URL name for the password reset complete page

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'