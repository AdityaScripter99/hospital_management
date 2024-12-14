from django.urls import path
from . import views

urlpatterns = [
    path('register/doctor/', views.doctor_register, name='doctor_register'),
    path('register/patient/', views.patient_register, name='patient_register'),
    path('login/', views.user_login, name='login'),
]
