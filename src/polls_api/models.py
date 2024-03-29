import random
import string
from django.db import models

def create_url(): 
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(8))

# Create your models here.
class Poll(models.Model):
    title = models.TextField()
    url = models.TextField(unique=True, default=create_url)
    date = models.DateTimeField(auto_now_add=True)

class PollOption(models.Model):
    poll = models.ForeignKey(Poll, related_name='options', on_delete=models.CASCADE)
    title = models.TextField()

class PollResponse(models.Model):
    poll_option = models.ForeignKey(PollOption, related_name='response', on_delete=models.CASCADE)
    ip = models.TextField()
    user_agent = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


