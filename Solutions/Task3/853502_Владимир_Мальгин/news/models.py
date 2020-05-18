from datetime import datetime
from django.db import models


class Post(models.Model):
    header = models.CharField(max_length=50)
    text = models.TextField()
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.header
