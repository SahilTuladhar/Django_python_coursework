from django.db import models

# Create your models here.

class Feature(models.Model):
 name  = models.CharField(max_length=100)
 age = models.IntegerField()
 details = models.CharField(max_length=100)
 is_age =  models.BooleanField() # Check whether 18 plus or not


class Posts(models.Model): 
 title = models.CharField(max_length=100)
 description = models.CharField(max_length=200)
 
  