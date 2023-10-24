from django.db import models
from django.contrib.auth.models import User


class Chat:
    id = models.IntegerField()


class Message():
    text = models.TextField()
    send_date = models.DateField()
    message_sender = models.ForeignKey(User, related_name='file_writer', on_delete=models.CASCADE)
    chat = Chat.id