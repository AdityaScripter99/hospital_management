from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import DoctorRegistrationForm, PatientRegistrationForm, LoginForm

def home(request):
    return render(request, 'home.html')

def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form, 'role': 'Doctor'})

def patient_register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PatientRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form, 'role': 'Patient'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'doctor':
                    return redirect('doctor_dashboard')
                elif user.role == 'patient':
                    return redirect('patient_dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

