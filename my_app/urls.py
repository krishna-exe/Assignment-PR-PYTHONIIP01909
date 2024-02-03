from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path("", views.index, name='home'),
    path("contact", views.contact, name='contact'),
    path('data', views.data, name='data')
]