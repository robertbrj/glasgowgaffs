from django.contrib import admin
from django.urls import path
from django.urls import include
from glasgowgaffsapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('glasgowgaffsapp/', include('glasgowgaffsapp.urls')),
    path('admin/', admin.site.urls),
]

