from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from speaker.models import Speaker



# Create your models here.

class Trainingtitle(models.Model):
    title = models.CharField(max_length=500)
    speaker = models.ForeignKey(Speaker, on_delete=models.DO_NOTHING, null=True)
    training_date = models.DateField(default=datetime.now)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title