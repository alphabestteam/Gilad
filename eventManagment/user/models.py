from django.db import models

# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    representative_name = models.CharField(max_length=50, unique=True)
    id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    unread_messages = models.IntegerField(default=0)

    def create(self, validated_data):
        return UserProfile(**validated_data)
        
    
    def __str__(self):
        return self.representative_name  # You can change this to display the user's name or username