# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdayEmails', '0008_auto_20151227_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='drchronoemail',
            name='email_address',
            field=models.TextField(default='adamkaz@gmail.com'),
            preserve_default=False,
        ),
    ]
