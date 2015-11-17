from django.db import models
from django.contrib.auth.models import User


class DrchronoUser(models.Model):
    user = models.OneToOneField(User)
    access_token = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    expires_timestamp = models.DateTimeField()