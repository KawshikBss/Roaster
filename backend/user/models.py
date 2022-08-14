import uuid
from django.db import models


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    email = models.CharField(unique=True, max_length=200)
    username = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200)
    image_link = models.CharField(max_length=200, null=True, blank=True)
    verified = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
