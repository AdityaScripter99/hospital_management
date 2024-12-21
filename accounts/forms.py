from django import forms
from .models import CustomUser

class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        user.role = 'doctor'
        if commit:
            user.save()
        return user

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        user.role = 'patient'
        if commit:
            user.save()
        return user
