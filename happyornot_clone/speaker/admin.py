from django.contrib import admin

# Register your models here.
from .models import Speaker

class SpeakerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'email',
      
    )
    list_display_links = ('id','name')

admin.site.register(Speaker, SpeakerAdmin)

