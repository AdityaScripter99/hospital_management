from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)  # User's name
    email = models.EmailField()              # User's email 
    subject = models.CharField(max_length=200)  # Subject of the message
    message = models.TextField()             # Message content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of submission

    def __str__(self):
        return f"{self.name} - {self.subject}"

