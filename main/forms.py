from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Contact

class ContactForm(ModelForm):
    class Meta:        
        cls='form-control input-group mb-3'  
        model= Contact
        fields='__all__'
        labels={
            'name':_(""),
            'email':_(""),
            'no':_(""),
            'msg':_(""),
            'address':_(""),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':cls,'placeholder':'Enter Name'}),
            'email': forms.TextInput(attrs={'class':cls,'placeholder':'Enter Email'}),            
            'no': forms.TextInput(attrs={'class':cls,'placeholder':'Enter Mobile No'}),
            'address': forms.Textarea(attrs={'class':cls,'rows':3,'placeholder':'Enter Address'}),
            'msg': forms.Textarea(attrs={'class':cls,'placeholder':'Message/Requirement'}),
        }
        help_texts:{
            'name':_('John Doe')
        }    
        error_messages:{
            'name':{
                'max_length':_("Name should be 60 words")
            }
        }

