from django.contrib import admin
from django.contrib.auth.models import User
from glasgowgaffsapp.models import Event, Location

# register event and location models to appear in Django admin
admin.site.register(Event)
admin.site.register(Location)

if not admin.site.is_registered(User):
    admin.site.register(User)