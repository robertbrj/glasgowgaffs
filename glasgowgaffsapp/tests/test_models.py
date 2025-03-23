from django.test import TestCase
from django.contrib.auth.models import User
from glasgowgaffsapp.models import Event, Location
from django.utils import timezone
import uuid

class LocationModelTests(TestCase):

    def test_create_location(self):
        location = Location.objects.create(name="Test Location", address="123 Test St")
        self.assertEqual(location.name, "Test Location")
        self.assertEqual(location.address, "123 Test St")
        self.assertIsInstance(location.id, uuid.UUID)  

    def test_location_str(self):
        location = Location.objects.create(name="Test Location", address="123 Test St")
        self.assertEqual(str(location), "Test Location")


class EventModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.location = Location.objects.create(name="Test Location", address="123 Test St")

    def test_create_event(self):
        event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            date=timezone.now().date(),
            time=timezone.now().time(),
            location=self.location,
            created_by=self.user
        )
        self.assertEqual(event.title, "Test Event")
        self.assertEqual(event.description, "Test Description")
        self.assertEqual(event.location, self.location)
        self.assertEqual(event.created_by, self.user)
        self.assertIn(self.user, event.attendees.all())  

    def test_event_str(self):
        event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            date=timezone.now().date(),
            time=timezone.now().time(),
            location=self.location,
            created_by=self.user
        )
        self.assertEqual(str(event), "Test Event")

    def test_add_creator_to_attendees_signal(self):
        event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            date=timezone.now().date(),
            time=timezone.now().time(),
            location=self.location,
            created_by=self.user
        )
        self.assertIn(self.user, event.attendees.all())  