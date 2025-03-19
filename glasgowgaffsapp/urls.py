from django.urls import path
from glasgowgaffsapp import views

app_name = 'glasgowgaffsapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create/', views.create, name='create'),
    path('contactus/', views.contact_us, name='contactus'),
    path('events/', views.events, name='events'),
    path('event/<uuid:event_id>/', views.event, name='event'),
    path('myevents/', views.myevents, name='myevents'),
    path('event/<uuid:event_id>/toggle_attendance/',views.toggle_attendance,name="toggle_attendance"),
]