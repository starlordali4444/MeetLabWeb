from django.shortcuts import render
from django.views import generic

class ServicesPageView(generic.TemplateView):
    template_name = "services/index.html"
