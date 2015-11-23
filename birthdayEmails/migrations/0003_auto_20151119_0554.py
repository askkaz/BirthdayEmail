# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('birthdayEmails', '0002_drchronouser_tempuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drchronouser',
            name='id',
        ),
        migrations.AlterField(
            model_name='drchronouser',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
