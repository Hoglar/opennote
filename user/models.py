from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sendt_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    creation_time = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=512)
    is_read = models.BooleanField(default=False)

