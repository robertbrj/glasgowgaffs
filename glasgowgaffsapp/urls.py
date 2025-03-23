from django.urls import path
from glasgowgaffsapp import views

app_name = 'glasgowgaffsapp'

urlpatterns = [
    path('', views.index, name='index'),  # home page
    path('register/', views.register, name='register'),  # register link page
    path('login/', views.user_login, name='login'),  # login link page
    path('logout/', views.user_logout, name='logout'),  # logout link page
    path('create/', views.create, name='create'),  # create event page
    path('contactus/', views.contact_us, name='contactus'),  # contact us form
    path('events/', views.events, name='events'),  # Events listing page
    path('event/<uuid:event_id>/', views.event, name='event'),  # Event page
    path('myevents/', views.myevents, name='myevents'),  # My Events page
    path('event/<uuid:event_id>/toggle_attendance/',
         views.toggle_attendance, name="toggle_attendance"),  # toggle attendance
]
