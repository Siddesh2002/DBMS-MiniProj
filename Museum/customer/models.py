from django.db import models

# Create your models here.

class Event(models.Model):
    name=models.CharField(max_length=200)
    des=models.TextField()
    img=models.ImageField(upload_to='pics')
    offer=models.BooleanField(default=False)
    price=models.FloatField(default=0)

