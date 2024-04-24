"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
  # path to index/home page
    path('', views.index, name='index'),
  # path to random dog pictures
    path('dog/', views.dog_view, name='dog_view'),
  # this will generate new facts and incriment the count
    path('generate_dogs/', views.generete_dog, name='generete_dog'),
  # path to random facts
   path('fact/', views.fact_view, name='fact_view'),
  # this will generate coont and new facts
    path('generate_facts/', views.generate_facts, name='generate_facts'),
  # path to rando student page 
    path('student/', views.random_student, name='random_student'),
  # this is a path to generate random student function
  # when its called the function executes
    path('generate_random_student/',
         views.generate_random_student,
         name='generate_random_student')
]
