from django.db import models
from django.contrib.auth import get_user_model

from datetime import datetime


class Topic(models.Model):
    name = models.CharField(max_length=256)
    creator = models.ForeignKey(to=get_user_model(), on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Theme(models.Model):
    topic = models.ForeignKey(to=Topic, on_delete=models.DO_NOTHING, related_name='themes')
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=1024, default="")
    creator = models.ForeignKey(to=get_user_model(), on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.topic.name + ' - ' + self.name


class Message(models.Model):
    theme = models.ForeignKey(to=Theme, on_delete=models.DO_NOTHING, related_name='messages')
    text = models.TextField(max_length=1024)
    sender = models.ForeignKey(to=get_user_model(), on_delete=models.DO_NOTHING)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.theme.topic.name + ' - ' + self.theme.name + ' - ' + self.text[:32] + '...'
