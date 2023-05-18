from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from trainingtitle.models import Trainingtitle
from speaker.models import Speaker


# Create your models here.
class Feedback(models.Model):
    rater = models.CharField(max_length=100)
    speaker = models.ForeignKey(Speaker, on_delete=models.DO_NOTHING, null=True)
    trainingtitle = models.ForeignKey(Trainingtitle, on_delete=models.DO_NOTHING, null=True)
    comment = models.TextField()
    rating = models.CharField(choices=(('Bad', '😞'), ('Poor', '🙁'), ('Average', '😐'), ('Good', '🙂'), ('Excellent', '😀')), max_length=100)
    feedback_date = models.DateField(default=datetime.now)


    def __str__(self):
        return self.comment
    
