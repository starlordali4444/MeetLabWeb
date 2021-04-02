from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.shortcuts import render,redirect,reverse
from .models import Contact,Slider
from services.models import Services
from photos.models import Photos
from .forms import ContactForm
from django.views import generic
from django.conf import settings



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

class AboutPageView(generic.ListView):
    model=Services
    template_name = "main/about.html"
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

    def form_valid(self, form):
        cd=form.clean()
        html_content=render_to_string("email/contactAdmin.html",cd)
        text_content=strip_tags(html_content)
        email=EmailMultiAlternatives(
            "New Query",
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL]
        )
        email.attach_alternative(html_content,"text/html")
        email.send()
        return super(ContactCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('main:contact')
