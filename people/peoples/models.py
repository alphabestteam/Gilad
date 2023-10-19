from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(max_length=10, primary_key=True)
    birth_date = models.DateField()
    city = models.TextField(max_length=100)
    