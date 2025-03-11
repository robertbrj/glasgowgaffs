from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=200)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default="Student Accommodation")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(User, related_name="attending_events", blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  
        if not self.attendees.exists():  
            self.attendees.add(self.created_by)

    def __str__(self):
        return self.title
    

# Signal to add the event creator to attendees after the Event is saved
@receiver(post_save, sender=Event)
def add_creator_to_attendees(sender, instance, created, **kwargs):
    if created:
        instance.attendees.add(instance.created_by)