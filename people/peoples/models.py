from django.db import models
from datetime import date
import unittest

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    city = models.TextField(max_length=100)

    def is_over_18(self):
        """
        function that check if person is over 18 years
        """
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age >= 18

class Parent(Person):
    work_place = models.TextField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    children = models.ManyToManyField(Person, related_name='parents', blank=True)
    