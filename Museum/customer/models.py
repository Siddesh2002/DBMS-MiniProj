from django.db import models

# Create your models here.

class Event(models.Model):
    name=models.CharField(max_length=200)
    des=models.TextField()
    img=models.ImageField(upload_to='pics')
    offer=models.BooleanField(default=False)
    price=models.FloatField(default=0)

class Ticket(models.Model):
    Username=models.CharField(max_length=500)
    Date=models.DateField()
    Amount=models.FloatField()
    No_of_persons=models.IntegerField(default=1)
    E_name=models.CharField(max_length=200)


