from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm, AppointmentStatusForm

# @login_required
def patient_dashboard(request):
    # Retrieve all appointments for the logged-in patient
    appointments = Appointment.objects.filter(patient=request.user)

    context = {
        'appointments': appointments,
    }
    return render(request, 'appointments/patient_dashboard.html', context)

# @login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.status = 'pending'
            appointment.save()
            return redirect('patient_dashboard') 
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})

# @login_required
def doctor_dashboard(request):
    appointments = Appointment.objects.filter(doctor=request.user)
    return render(request, 'appointments/doctor_dashboard.html', {'appointments': appointments})

# @login_required
def update_appointment_status(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == 'POST':
        form = AppointmentStatusForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('doctor_dashboard')
    else:
        form = AppointmentStatusForm(instance=appointment)
    return render(request, 'appointments/update_status.html', {'form': form, 'appointment': appointment})
