from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Questions(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=600)

class Answers(models.Model):
    body = models.CharField(max_length=600)