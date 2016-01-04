# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdayEmails', '0004_drchronoemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='drchronoemail',
            name='year',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]
