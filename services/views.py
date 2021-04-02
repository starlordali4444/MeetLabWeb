from django.shortcuts import render
from django.views import generic
from .models import Services

class ServicePageView(generic.ListView):
    model=Services
    template_name = "services/index.html"
    query_set= Services.objects.all()
    context_object_name="services"

    def get_context_data (self, ** kwargs):
        context = super (). get_context_data (** kwargs)
        return context