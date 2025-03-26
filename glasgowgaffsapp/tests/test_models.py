from django.test import TestCase
from django.contrib.auth.models import User
from glasgowgaffsapp.models import Event, Location
from django.utils import timezone
import uuid


class LocationModelTests(TestCase):
    """
        unit tests for the Location model in the GlasgowGaffs models
    """
    def test_create_location(self):
        """
            tests that a Location object can be successfully created
            and the string representation matches its name
        """
        location = Location.objects.create(name="Test Location", address="123 Test St")
        self.assertEqual(location.name, "Test Location")
        self.assertEqual(location.address, "123 Test St")
        self.assertIsInstance(location.id, uuid.UUID)

    def test_location_str(self):
        """
            tests the __str__ method of the Location model
            returning the location's name
        """
        location = Location.objects.create(name="Test Location", address="123 Test St")
        self.assertEqual(str(location), "Test Location")


class EventModelTests(TestCase):
    """
       unit tests for the Event model
    """
    def setUp(self):
        """
            sets up a dummy user and location for use in Event model tests
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.location = Location.objects.create(name="Test Location", address="123 Test St")

    def test_create_event(self):
        """
            tests that an Event object can be created with valid inputs
            and string representation matches the event title
        """
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
        """
            test the __str__ method of the Event model
            returning the event's title
        """
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
        """
           tests that the event creator is automatically added to the attendees list
           via a post-save signal
           ensures the signal handler correctly appends the 'created_by' user
           to the event's ManyToMany 'attendees' field immediately after creation
        """
        event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            date=timezone.now().date(),
            time=timezone.now().time(),
            location=self.location,
            created_by=self.user
        )
        self.assertIn(self.user, event.attendees.all())
