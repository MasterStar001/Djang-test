from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    Phone = models.CharField(max_length=122)
    massage = models.CharField(max_length=200)
    date = models.TimeField()