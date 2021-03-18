from django.contrib import admin
from django.urls import path
from . import views
app_name='services'

urlpatterns = [
    path('', views.ServicesPageView.as_view(), name="Services"),
    # path('Contact-Us', views.contact, name="contact"),
]
