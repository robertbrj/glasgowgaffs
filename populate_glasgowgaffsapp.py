import os
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasgowgaffs.settings')

import django
django.setup()
from glasgowgaffsapp.models import Event, Location
from django.contrib.auth.models import User

def populate():
    locations = [
    {'name': 'Firhill Court', 'address': '150 Firhill Road, Glasgow, G20 7BB'},
    {'name': 'Murano', 'address': '13 Caithness St, Glasgow G20 7SB'},
    {'name': 'Kelvinhaugh Street', 'address': '85 Kelvinhaugh St, Glasgow G3 8PE'},
    {'name': 'Gibson Street', 'address': 'Gibson Street, Glasgow G12 8SY'},
    {'name': 'Merchant Studios', 'address': '6 Havannah Street, Glasgow G4 0AJ'},
    {'name': 'Buchanan View', 'address': '33-35 Calgary Street, Glasgow G4 0XG'},
    {'name': 'The Cube', 'address': '10 Dixon Street, Glasgow G1 4AX'}, 
    {'name': 'Sandyford Court', 'address': 'Sandyford Place, Glasgow G3 7ND'}, 
    {'name': 'Crown Place', 'address': 'Crown Place, Glasgow G1 2AA'}, 
    {'name': 'Collegelands', 'address': '100 Cathedral Street, Glasgow G4 0QD'}, 
    {'name': 'Castle Court', 'address': 'Castle Street, Glasgow G4 0QR'} 

]

    events = [
    {'title': 'Thursday Madness',
     'description': 'Come to Flat D9 at 22:00 to have the best time of your life! We got plenty to drink, society games and we want to make new friends!!',
     'date': '2024-05-02',
     'time': '22:00:00'},

    {'title': 'Friday Frenzy',
     'description': 'Flat 3B is the place to be this Friday at 22:30! Expect banging tunes, good vibes, and plenty of drinks to keep the night going. Bring your mates, meet new people, and let’s make it a night to remember!',
     'date': '2024-05-03',
     'time': '22:30:00'},

    {'title': 'Saturday Sessions',
     'description': 'Kicking off at 21:00, this gaff is bringing you non-stop fun, from classic drinking games to a top-tier playlist. Whether you’re here to dance, chat, or just vibe, we’ve got you covered. Don’t miss out!',
     'date': '2024-05-04',
     'time': '21:00:00'},

    {'title': 'Mayday Mayhem',
     'description': 'Massive party at the Murano building!  DJ, drinks, and dancing all night long.  Get your tickets early!',
     'date': '2024-05-01',
     'time': '21:00:00'},

    {'title': 'Chill Vibes Wednesday',
     'description': 'Relaxed evening with board games and chilled music at Flat 1A.  BYOB!',
     'date': '2024-05-08',
     'time': '19:00:00'},

    {'title': 'Karaoke Night!',
     'description': 'Show off your vocal talents (or lack thereof!).  Free entry!',
     'date': '2024-05-15',
     'time': '20:00:00'},

    {'title': 'Garden Party',
     'description': 'Outdoor party with BBQ and good music.  Weather permitting!',
     'date': '2024-05-22',
     'time': '18:00:00'},

    {'title': 'Merchant City Mixer',
     'description': 'Meet new people at this social event.  Games and drinks!',
     'date': '2024-05-29',
     'time': '21:00:00'},

    {'title': 'Film Night',
     'description': 'Casual movie night with popcorn and snacks.  Bring your favourite film!',
     'date': '2024-05-09',
     'time': '20:00:00'},

    {'title': 'The Cube Club Night',
     'description': 'Dance the night away at this club night. Expect a great atmosphere and top DJs!',
     'date': '2024-05-23',
     'time': '22:00:00'},


    {'title': 'Board Game Bonanza',
     'description': 'Bring your favourite board games and join us for an evening of fun and friendly competition!',
     'date': '2024-05-11',
     'time': '19:30:00'},
]

    location_objects = []
    for location in locations:
        l = add_location(name=location['name'], address=location['address'])
        location_objects.append(l)

    admin = User.objects.get(username="team8b")

    for i, event in enumerate(events):
        location = location_objects[i]  
        date = datetime.strptime(event['date'], '%Y-%m-%d').date()  
        time = datetime.strptime(event['time'], '%H:%M:%S').time()  
        e = add_event(title=event['title'], description=event['description'],
                  date=date, time=time, location=location, created_by=admin)

def add_event(title, description, date, time, location, created_by):
    e = Event.objects.create(title=title, description=description, date=date, time=time, location=location, created_by = created_by)
    return e

def add_location(name, address):
    l = Location.objects.create(name=name, address=address)
    return l

populate()
