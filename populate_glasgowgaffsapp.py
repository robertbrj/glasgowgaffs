import os
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasgowgaffs.settings')

import django
django.setup()
from glasgowgaffsapp.models import Event, Location

def populate():
    locations = [
        {'name': 'Firhill Court', 'address': '150 Firhill Road, Glasgow, G20 7BB'},
        {'name': 'Murano', 'address': '13 Caithness St, Glasgow G20 7SB'},
        {'name': 'Kelvinhaugh Street', 'address': '85 Kelvinhaugh St, Glasgow G3 8PE'},
    ]

    events = [
        {'title': 'Thursday Madness',
         'description': 'Come to Flat D9 at 22:00 to have the best time of your life! We got plenty to drink, society games and we want to make new friends!!',
         'date': '2025-03-06',
         'time': '22:00:00'},

        {'title': 'Friday Frenzy',
         'description': 'Flat 3B is the place to be this Friday at 22:30! Expect banging tunes, good vibes, and plenty of drinks to keep the night going. Bring your mates, meet new people, and let’s make it a night to remember!',
         'date': '2025-03-07',
         'time': '22:30:00'},

        {'title': 'Saturday Sessions',
         'description': 'Kicking off at 21:00, this gaff is bringing you non-stop fun, from classic drinking games to a top-tier playlist. Whether you’re here to dance, chat, or just vibe, we’ve got you covered. Don’t miss out!',
         'date': '2025-03-08',
         'time': '21:00:00'}
    ]

    location_objects = []
    for location in locations:
        l = add_location(name=location['name'], address=location['address'])
        location_objects.append(l)

    for i, event in enumerate(events):
        location = location_objects[i]  
        date = datetime.strptime(event['date'], '%Y-%m-%d').date()  
        time = datetime.strptime(event['time'], '%H:%M:%S').time()  
        add_event(title=event['title'], description=event['description'],
                  date=date, time=time, location=location)

def add_event(title, description, date, time, location):
    e = Event.objects.create(title=title, description=description, date=date, time=time, location=location)
    return e

def add_location(name, address):
    l = Location.objects.create(name=name, address=address)
    return l

populate()
