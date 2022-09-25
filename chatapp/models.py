from django.db import models

from django.contrib.auth.models import AbstractUser

STATUS_CHOICES = (
    (0, "delivered"),
    (1, "awaiting")
)

class MyUser(AbstractUser):
    pass

class Conversation(models.Model):
    initiator = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, related_name='initial_convo')
    receipient = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, related_name='receipient')
    time_created = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, related_name='message_sender' )
    text = models.CharField(max_length=200, blank=True)
    attachment = models.FileField(blank=True)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE, )
    time_sent = models.DateTimeField(auto_now_add=True)
    status = models.CharField(null=True, choices=STATUS_CHOICES, max_length=100)

    class Meta:
        ordering = ('-time_sent',)