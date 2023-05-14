from django.contrib import admin

# Register your models here.
from .models import Trainingtitle

class TrainingtitleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'training_date'

      
    )
    list_display_links = ('id','title')

admin.site.register(Trainingtitle, TrainingtitleAdmin)

