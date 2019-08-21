from django.db import models

# Create your models here.
class Poll(models.Model):
    name = models.TextField()
    description = models.TextField()
    url = models.TextField()

class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    name = models.TextField()

class BrowserInstance(models.Model):
    ip = models.TextField()
    user_agent = models.TextField()

class Answer (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    browser_instance = models.ForeignKey(BrowserInstance, on_delete=models.CASCADE)

