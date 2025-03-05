from django.urls import path
from glasgowgaffsapp import views
app_name = 'glasgowgaffsapp'
urlpatterns = [
    path('', views.index, name='index'),
]