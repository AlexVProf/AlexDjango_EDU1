import os

from django.db import models

# Create your models here.
class ModelAlex(models.Model):
    name = models.TextField()
    password = models.TextField()
