from django.db import models

# Create your models here.
class Film(models.Model):
  name = models.CharField(max_length=200)
  age = models.IntegerField(max_length=5)
  contact = models.CharField(lenght=9)
