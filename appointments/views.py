from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Appointment
from .forms import AppointmentForm, AppointmentStatusForm
from django.contrib.auth.models import User

@login_required
def doctor_dashboard(request):
    if request.user.profile.role != 'Doctor':
        return redirect('home')
    appointments = Appointment.objects.filter(doctor=request.user)
    return render(request, 'appointments/doctor_dashboard.html', {'appointments': appointments})

@login_required
def patient_dashboard(request):
    if request.user.profile.role != 'Patient':
        return redirect('home')
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'appointments/patient_dashboard.html', {'appointments': appointments})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('patient_dashboard')
    else:
        form = AppointmentForm()
        form.fields['doctor'].queryset = User.objects.filter(profile__role='Doctor')
    return render(request, 'appointments/book_appointment.html', {'form': form})

@login_required
def update_appointment_status(request, appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id)
    except Appointment.DoesNotExist:
        raise Http404("Appointment not found")
    if request.method == 'POST':
        form = AppointmentStatusForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('doctor_dashboard')
    else:
        form = AppointmentStatusForm(instance=appointment)
    return render(request, 'appointments/update_status.html', {'form': form})
