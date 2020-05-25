from django.db import models


# Question-Answer
class QA(models.Model):
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=256)

    def __str__(self):
        return self.question
