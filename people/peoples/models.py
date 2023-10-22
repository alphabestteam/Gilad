from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    city = models.TextField(max_length=100)

class Parent(Person):
    work_place = models.TextField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    children = models.ManyToManyField(Person, related_name='parents', blank=True)
    