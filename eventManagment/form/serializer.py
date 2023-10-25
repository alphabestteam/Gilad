from rest_framework import serializers
from .models import *

class BaseFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseForm
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventWithMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventWithMessages
        fields = '__all__'

class EventWithFileSharingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventWithFileSharing
        fields = '__all__'