from django.db import models
from user.models import Profile
import uuid


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=500, blank=True, null=True)
    image_link = models.CharField(max_length=200, null=True, blank=True)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=500, blank=True, null=True)
    image_link = models.CharField(max_length=200, null=True, blank=True)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
