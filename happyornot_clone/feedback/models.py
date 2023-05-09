from django.db import models

# Create your models here.
class Feedback(models.Model):
    user = models.CharField(max_length=100)
    comment = models.TextField()
    # rating = models.IntegerField(choices=((1, '😞'), (2, '🙁'), (3, '😐'), (4, '🙂'), (5, '😀')))
    rating = models.CharField(choices=(('Bad', '😞'), ('Poor', '🙁'), ('Average', '😐'), ('Good', '🙂'), ('Excellent', '😀')))


    def __str__(self):
        return self.comment
    
