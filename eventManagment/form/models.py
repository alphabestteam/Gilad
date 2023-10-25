from django.db import models
from django.contrib.auth.models import User
from message.models import Message
import datetime


class BaseForm(models.Model):
    messages = models.ManyToManyField(
        "messages.Message", related_name="forms_with_messages", blank=True
    )
    files = models.ManyToManyField(
        "files.File", related_name="forms_with_files", blank=True
    )

    class Meta:
        abstract = True

    def create(self, validated_data):
        return BaseForm(**validated_data)


class Event(BaseForm):
    STATUS_CHOICES = (
        ("open", "Open"),
        ("closed", "Closed"),
        ("draft", "Draft"),
        ("archived", "Archived"),
    )

    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField(null=True, blank=True)
    event_status = models.CharField(
        max_length=8, choices=STATUS_CHOICES, default="closed"
    )
    is_draft = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    common_users = models.ManyToManyField(
        User, related_name="common_events", blank=True
    )
    incident_reporter = models.ForeignKey(
        User, related_name="reported_events", on_delete=models.CASCADE
    )

    def archive_event(self):
        self.event_status = "archived"
        self.is_archived = True
        self.save()

    def set_status_choice(self, new_status):
        """
        function that set attribute in the status choices.
        """
        if new_status == 'open':
            self.opening_date = datetime.datetime.now()
            self.event_status = new_status
            self.save()
        elif new_status == 'closed':
            self.closing_date = datetime.datetime.now()
            self.event_status = new_status
            self.save()
        else:
            self.event_status = new_status
            self.save()


    def __str__(self):
        return f"{self.title} - Status: {self.get_event_status_display()}"
    
    def create(self, validated_data):
        return Event(**validated_data)


class EventWithMessages(BaseForm):
    addressed = Event.incident_reporter
    name_addressee = models.ForeignKey(
        User, related_name="reported_events", on_delete=models.CASCADE
    )
    message = models.ForeignKey(Message)

    # This specialized form has a relationship to messages

    def create(self, validated_data):
        return EventWithMessages(**validated_data)


class EventWithFileSharing(BaseForm):

    # This specialized form has a relationship to files

    def create(self, validated_data):
        return EventWithFileSharing(**validated_data)
