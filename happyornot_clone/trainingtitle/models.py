from django.db import models
from datetime import datetime


# Create your models here.

class Trainingtitle(models.Model):
    title = models.CharField(max_length=500)
    training_date = models.DateField(default=datetime.now)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title