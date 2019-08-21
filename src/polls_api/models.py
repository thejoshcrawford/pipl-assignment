from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.TextField()

class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    title = models.TextField()

class BrowserInstance(models.Model):
    ip = models.TextField()
    user_agent = models.TextField()

class PollResponse(models.Model):
    poll_option = models.ForeignKey(PollOption, on_delete=models.CASCADE)
    browser_instance = models.ForeignKey(BrowserInstance, on_delete=models.CASCADE)

