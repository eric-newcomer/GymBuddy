# not master urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('workout/', views.workout, name='workout'),
    path('feed/', views.feed, name='feed'),
]