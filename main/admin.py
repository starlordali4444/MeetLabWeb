from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import Contact,Slider

class ContactAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Contact._meta.fields]

class SliderAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Slider._meta.fields]

admin.site.unregister(Group)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Slider,SliderAdmin)


