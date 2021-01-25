from django.db import models

# Create your models here.

class Reklama(models.Model):
    prise = models.FloatField()
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    img = models.ImageField(upload_to=None)
    def __str__(self):
        return self.title