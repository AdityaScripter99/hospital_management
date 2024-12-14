from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('appointment/<int:appointment_id>/status/', views.update_appointment_status, name='update_appointment_status'),
]
