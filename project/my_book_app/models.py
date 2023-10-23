from django.db import models
from django.core.exceptions import ValidationError


def validate_title(value):
    if len(value) > 100:
        raise ValidationError("Title cannot be more than 100 characters")

def validate_author(value):
    if len(value) > 50:
        raise ValidationError("Author cannot be more than 50 characters")
    
def validate_publication_year(value):
    if value < 1000 or value > 9999:
        raise ValidationError("Publication year must be a 4-digit year.")
    
def validate_isbn(value):
    if len(value) > 13:
        raise ValidationError("isbn cannot be more than 13 characters")


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title
    

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.username 

    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)