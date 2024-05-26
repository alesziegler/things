from django.db import models

# Create your models here.
class Customer(models.Model):
  name = models.CharField(max_length=200)
  age = models.IntegerField()
  contact = models.CharField(max_length=20)

  
    

  def __str__(self):
    return f"{self.name}, {self.age}, {self.contact}"
