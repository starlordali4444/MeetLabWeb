from django.contrib import admin
from .models import Photos


class PhotosAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Photos._meta.fields]


admin.site.register(Photos,PhotosAdmin)
