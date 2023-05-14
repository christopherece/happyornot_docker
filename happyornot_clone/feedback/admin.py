from django.contrib import admin
from .models import Feedback

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'rater',
        'comment',
        'rating',
        'feedback_date',
        'user',
        'trainingtitle',
    )
    list_display_links = ('id', 'rater')

admin.site.register(Feedback, FeedbackAdmin)
