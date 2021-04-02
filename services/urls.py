from django.contrib import admin
from django.urls import path
from . import views
app_name='services'

urlpatterns = [
    path('', views.ServicePageView.as_view(), name="index"),
]
