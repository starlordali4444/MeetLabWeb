from django.shortcuts import render,redirect,reverse
from .models import Contact,Slider
from services.models import Services
from photos.models import Photos
from .forms import ContactForm
from django.views import generic

class IndexPageView(generic.ListView):
    model=Services
    template_name = "main/index.html"
    query_set= Services.objects.all()
    context_object_name="services"

    def get_context_data (self, ** kwargs):
        context = super (). get_context_data (** kwargs)
        context ['sli'] = Slider.objects.all()
        context ['photos'] = Photos.objects.all()
        return context

class ContactCreateView(generic.CreateView):
    model = Contact
    template_name = "main/contact.html"
    form_class=ContactForm

    def get_success_url(self):
        return reverse('main:contact')
