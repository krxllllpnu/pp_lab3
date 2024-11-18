from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['flight', 'passenger', 'seat_number', 'booking_time']
        widgets = {
            'flight': forms.Select(attrs={'class': 'form-control'}),
            'passenger': forms.Select(attrs={'class': 'form-control'}),
            'seat_number': forms.TextInput(attrs={'class': 'form-control'}),
            'booking_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

from django.contrib.auth.models import User
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match")

        return cleaned_data