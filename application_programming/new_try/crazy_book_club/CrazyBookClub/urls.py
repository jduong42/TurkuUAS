# Defines URL patterns for CrazyBookClub.

from django.urls import path

from . import views

app_name = 'CrazyBookClub'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),    
]