from django.test import TestCase
from django.contrib.auth.models import User
from glasgowgaffsapp.forms import EventForm, UserForm
from glasgowgaffsapp.models import Location
from django.utils import timezone
import uuid


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
