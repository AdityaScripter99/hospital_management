from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Include auth URLs
    path('', accounts_views.home, name='home'),  # Home Page
    # path('accounts/', include('accounts.urls')),
    path('appointments/', include('appointments.urls')),
]
