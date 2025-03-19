from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from glasgowgaffsapp.models import Event, Location
from glasgowgaffsapp.forms import EventForm
from django.utils import timezone


class GlasgowGaffsAppTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')  

        self.location = Location.objects.create(name="Test Location", address="Test Address")

        self.event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            date=timezone.now().date(),  
            time=timezone.now().time(),
            location=self.location,
            created_by=self.user
        )


    def test_index_view(self):
        response = self.client.get(reverse('glasgowgaffsapp:index'))
        self.assertEqual(response.status_code, 200)


    def test_create_event_view_get(self):
        response = self.client.get(reverse('glasgowgaffsapp:create'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], EventForm)

    def test_create_event_view_post(self):
        data = {
            'title': 'New Event',
            'description': 'New Description',
            'date': timezone.now().date(),
            'time': timezone.now().time(),
            'location': self.location.id,  
        }
        response = self.client.post(reverse('glasgowgaffsapp:create'), data=data)
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('glasgowgaffsapp:index'))
        self.assertTrue(Event.objects.filter(title='New Event').exists())


    def test_events_view(self):
        response = self.client.get(reverse('glasgowgaffsapp:events'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Event") 


    def test_event_detail_view(self):
        response = self.client.get(reverse('glasgowgaffsapp:event', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Event")
        self.assertContains(response, "Test Description")


    def test_myevents_view(self):
        response = self.client.get(reverse('glasgowgaffsapp:myevents'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Event") 
