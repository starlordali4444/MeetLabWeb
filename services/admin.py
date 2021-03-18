from django.contrib import admin
from .models import Services

class ServicesAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Services._meta.fields]
    
admin.site.register(Services,ServicesAdmin)

