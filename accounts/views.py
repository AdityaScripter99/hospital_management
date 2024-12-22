from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm
from .models import Profile
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('contact')  # Redirect to the same page or a thank-you page
    else:
        form = ContactForm()
    return render(request, 'accounts/contact.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Assign role to the user
            role = form.cleaned_data['role']
            Profile.objects.create(user=user, role=role)

            messages.success(request, f"Registration successful as {role}.")
            return redirect('login_page')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'accounts/login.html')

def logout_page(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login_page')
