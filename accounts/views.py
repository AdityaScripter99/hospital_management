from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import DoctorRegistrationForm, PatientRegistrationForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor registered successfully. Please log in.')
            return redirect('login_page')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form, 'role': 'Doctor'})

def patient_register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient registered successfully. Please log in.')
            return redirect('login_page')
    else:
        form = PatientRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form, 'role': 'Patient'})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

def logout_page(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login_page')
