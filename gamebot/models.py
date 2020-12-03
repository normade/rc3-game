import uuid

from django.db import models


class CommunicationCategory(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=32)
    accepted_keywords = models.TextField(blank=True)
    bot_answer = models.TextField(blank=True)
    link_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
