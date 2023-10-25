from django.db import models
from django.contrib.auth.models import User


class Chat:
    id = models.IntegerField()

    def create(self, validated_data):
        return Chat(**validated_data)


class Message():
    text = models.TextField()
    send_date = models.DateField()
    message_sender = models.ForeignKey(User, related_name='file_writer', on_delete=models.CASCADE)
    chat = Chat.id

    def create(self, validated_data):
            return Message(**validated_data)
