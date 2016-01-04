# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdayEmails', '0007_auto_20151226_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drchronoemail',
            name='sent_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
