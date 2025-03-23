from django import forms
from django.contrib.auth.models import User
from glasgowgaffsapp.models import Event, Location
from django.utils import timezone

class UserForm(forms.ModelForm):
    """
        form used for registering a new user.
        includes username, email, and password with styled widgets
        also checks for existing email during validation
    """
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
        }

    def clean_email(self):
        """
            form for creating or editing an Event
            includes fields for title, description, date, time, and location
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    

class EventForm(forms.ModelForm):
    """
        form for creating or editing an Event.
        includes fields: title, description, date, time and location
    """
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event Description'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_date(self):
        """
            validates that the selected event date is not in the past
        """
        event_date = self.cleaned_data.get('date')
        if event_date and event_date < timezone.localdate():
            raise forms.ValidationError("The event date cannot be in the past.")
        return event_date
