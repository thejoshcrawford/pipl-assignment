from django.db import models

# Create your models here.
class Poll(models.Model):
    name = models.TextField()
    description = models.TextField()

