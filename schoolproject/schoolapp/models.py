# models.py
from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200)
    materials = models.TextField()  # This could be a ManyToManyField if you have a Material model
