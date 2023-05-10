from django.db import models

# Create your models here.
class Feedback(models.Model):
    user = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.CharField(choices=(('Bad', '😞'), ('Poor', '🙁'), ('Average', '😐'), ('Good', '🙂'), ('Excellent', '😀')), max_length=100)


    def __str__(self):
        return self.comment
    
