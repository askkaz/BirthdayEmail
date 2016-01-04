# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdayEmails', '0005_drchronoemail_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='drchronoemail',
            name='user',
            field=models.ForeignKey(to='birthdayEmails.DrchronoUser', default=1),
            preserve_default=False,
        ),
    ]
