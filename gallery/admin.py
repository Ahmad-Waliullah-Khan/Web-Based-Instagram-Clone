from django.contrib import admin

from .models import Gallery

#===============================================================================
# GalleryAdmin
#===============================================================================
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'photo', 'photo_size_240', 'photo_size_720', 'caption',
        'created_at', 'updated_at', 'user',
    )
