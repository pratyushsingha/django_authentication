from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm

def registration_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                if User.objects.filter(username=form.cleaned_data['username']).exists():
                    messages.error(request, 'Username already exists')
                    return render(request, 'yourapp/register.html', {'form': form})
                
                if User.objects.filter(email=form.cleaned_data['email']).exists():
                    messages.error(request, 'Email already registered')
                    return render(request, 'yourapp/register.html', {'form': form})

                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                
                authenticated_user = authenticate(
                    request,
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    backend='django.contrib.auth.backends.ModelBackend'
                )
                
                if authenticated_user is not None:
                    login(request, authenticated_user)
                    messages.success(request, 'Registration successful!')
                    return redirect('login')
                else:
                    messages.error(request, 'Authentication failed after registration')
                    return render(request, 'yourapp/register.html', {'form': form})
                
            except Exception as e:
                messages.error(request, f'Registration failed: {str(e)}')
                return render(request, 'yourapp/register.html', {'form': form})
        else:
            if 'turnstile' in form.errors:
                messages.error(request, 'Please complete the Turnstile verification')
            else:
                messages.error(request, 'Please correct the errors below')
    else:
        form = RegisterForm()
    
    return render(request, 'yourapp/register.html', {'form': form})

@login_required
def profile_view(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Please login to view your profile.')
        return redirect('login')
    return render(request, 'yourapp/profile.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    messages.error(request, 'Invalid email or password')
                    return render(request, 'yourapp/login.html', {'form': form})
                
                user = authenticate(username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successful!')
                    return redirect('profile')
                else:
                    messages.error(request, 'Invalid email or password')
            except Exception as e:
                messages.error(request, f'Login failed: {str(e)}')
        else:
            if 'turnstile' in form.errors:
                messages.error(request, 'Please complete the Turnstile verification')
            else:
                messages.error(request, 'Please correct the errors below')
    else:
        form = LoginForm()
    
    return render(request, 'yourapp/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'yourapp/home.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')


