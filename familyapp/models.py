from django.db import models
import datetime

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 50) 
    description = models.TextField(default = 'happy child')
    birth_date = models.DateField(default = datetime.date(2017,1,1))
    graduation_date = models.DateField(default = datetime.date(2017,1,1))
