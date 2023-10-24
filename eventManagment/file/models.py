from django.db import models
from django.contrib.auth.models import User


class File:
    upload_date = models.DateField()
    file_writer = models.ForeignKey(User, related_name='file_writer', on_delete=models.CASCADE)
    file = models.FileField()
