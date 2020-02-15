from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):
    friend_one = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='friend_one')
    friend_two = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.TextField()

class Message(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()