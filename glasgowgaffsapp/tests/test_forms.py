from django.test import TestCase
from django.contrib.auth.models import User
from glasgowgaffsapp.forms import EventForm, UserForm
from glasgowgaffsapp.models import Location,Event
from django.utils import timezone
import uuid
from django.forms import fields as django_fields
import os
from glasgowgaffsapp import forms
from django.forms.models import ModelChoiceField as django_model_field

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

f"{FAILURE_HEADER} {FAILURE_FOOTER}"


class EventFormTests(TestCase):

    def setUp(self):
        self.location = Location.objects.create(name="Test Location", address="123 Test St")
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_Event_Form_Valid(self):
        form_data={
            "title":"valid check",
            "description":"event valid",
            "date":timezone.now().date(),
            "time":timezone.now().time(),
            "location":self.location.id,
        }
        form=EventForm(data=form_data)
        self.assertTrue(form.is_valid())


    def test_Event_Form_InValid(self):
        form_data={
            "title":"",
            "description":"event Invalid",
            "date":timezone.now().date(),
            "time":timezone.now().time(),
            "location":self.location.id,
        }
        form=EventForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title',form.errors)

    def test_Event_form_struc(self):
        """
        Tests whether EventForm is in the correct place, and whether the correct fields have been specified for it.
        """
        self.assertTrue('EventForm' in dir(forms), f"{FAILURE_HEADER}We couldn't find the EventForm class in glasgowgaffsapp's forms.py module. Did you create it in the right place?{FAILURE_FOOTER}")
        
        event_form = forms.EventForm()
        self.assertEqual(type(event_form.__dict__['instance']), Event, f"{FAILURE_HEADER}Your EventForm does not match up to the Event model. Check your Meta definition of EventForm and try again.{FAILURE_FOOTER}")

        fields = event_form.fields
        
        expected_fields = {
            'title': django_fields.CharField,
            'description': django_fields.CharField,
            'date': django_fields.DateField,
            'time': django_fields.TimeField,
            'location': django_model_field,
            }
        
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]

            self.assertTrue(expected_field_name in fields.keys(), f"{FAILURE_HEADER}The field {expected_field_name} was not found in the EventForm form. Check you have complied with the specification, and try again.{FAILURE_FOOTER}")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"{FAILURE_HEADER}The field {expected_field_name} in EventForm was not of the correct type. Expected {expected_field}; got {type(fields[expected_field_name])}.{FAILURE_FOOTER}")

class UserFormTests(TestCase):


    def test_User_Form_Valid(self):
        form_data={
        'username': "TestUser12", 
        'email': "TestUser12@gmail.com", 
        'password': "newPassword1"}
        form=UserForm(data=form_data)
        self.assertTrue(form.is_valid())

    
    def test_User_Form_InValid(self):
        form_data={
            "username":"",
            "email":"example@me.com",
            "password":"password123"
        }
        form=UserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("username",form.errors)

    def test_user_Form_dupEmail(self):
        User.objects.create_user(username='testuser',email="example@example.com", password='testpassword')

        form_data={
            "username":"newUser123",
            "email":"example@example.com",
            "password":"pass12345"
        }

        form=UserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("email",form.errors)
        self.assertIn("A user with this email already exists.",form.errors["email"])

    def test_user_form_structure(self):
        """
        Tests whether UserForm is in the correct place, and whether the correct fields have been specified for it.
        """
        self.assertTrue('UserForm' in dir(forms), f"{FAILURE_HEADER}We couldn't find the UserForm class in glasgowgaffsapp's forms.py module. Did you create it in the right place?{FAILURE_FOOTER}")
        
        user_form = forms.UserForm()
        self.assertEqual(type(user_form.__dict__['instance']), User, f"{FAILURE_HEADER}Your UserForm does not match up to the User model. Check your Meta definition of UserForm and try again.{FAILURE_FOOTER}")

        fields = user_form.fields
        
        expected_fields = {
            'username': django_fields.CharField,
            'email': django_fields.EmailField,
            'password': django_fields.CharField,
        }
        
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]

            self.assertTrue(expected_field_name in fields.keys(), f"{FAILURE_HEADER}The field {expected_field_name} was not found in the UserForm form. Check you have complied with the specification, and try again.{FAILURE_FOOTER}")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"{FAILURE_HEADER}The field {expected_field_name} in UserForm was not of the correct type. Expected {expected_field}; got {type(fields[expected_field_name])}.{FAILURE_FOOTER}")
