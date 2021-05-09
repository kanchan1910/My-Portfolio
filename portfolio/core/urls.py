from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('edu', views.education, name="edu"),
    path('skills', views.skills, name="skills"),
    path('programming', views.programming, name="programming"),
    path('projects', views.projects, name="projects"),
    path('ex', views.experience, name="ex"),
    path('resume', views.resume, name="resume"),
    path('github', views.github, name="github"),
    path('certi', views.certi, name="certi"),
    path('contact', views.contact, name="contact"),
]
