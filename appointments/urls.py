from django.urls import path
from appointments.views import book_appointment,doctor_dashboard,patient_dashboard,update_appointment_status

urlpatterns = [
    path('book/',book_appointment, name='book_appointment'),
    path('doctor/dashboard/',doctor_dashboard, name='doctor_dashboard'),
    path('appointment/<int:appointment_id>/status/',update_appointment_status, name='update_appointment_status'),
    path('patient/dashboard/',patient_dashboard, name='patient_dashboard'),
]
