from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('skills', views.skills, name="skills"),
    path('contact', views.contact, name="contact"),
]
