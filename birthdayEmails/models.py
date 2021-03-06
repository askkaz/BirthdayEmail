from django.db import models
from django.contrib.auth.models import User
import datetime, pytz
from .common.drchronoUtils import *

class DrchronoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    access_token = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    expires_timestamp = models.DateTimeField()
    def check_access_token(self):
        if self.expires_timestamp < datetime.datetime.now(pytz.utc) + datetime.timedelta(minutes=30):
            data = refreshDrchronoAccessToken(self.refresh_token)
            if data:
                self.access_token = data['access_token']
                self.refresh_token = data['refresh_token']
                self.expires_timestamp = data['expires_timestamp']
                self.save()
            else:
                pass #Could kick off a complete re-link, but for now, attempt to refresh again at next login.

class TempUser(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=100)
    expires_timestamp = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)

class DrchronoEmail(models.Model):
    send_date = models.DateTimeField()
    sent_date = models.DateTimeField(blank=True, null=True)
    subject = models.CharField(max_length=77)
    body = models.TextField()
    email_address = models.TextField()
    patient_id = models.IntegerField()
    user = models.ForeignKey(DrchronoUser, on_delete=models.CASCADE)
