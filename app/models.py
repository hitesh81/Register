from django.db import models

# Create your models here.
class registions(models.Model):
    
    firstname = models.CharField(max_length=200)
    lastname = models.TextField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
