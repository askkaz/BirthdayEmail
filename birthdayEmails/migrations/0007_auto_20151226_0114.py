# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdayEmails', '0006_drchronoemail_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drchronoemail',
            old_name='birthday',
            new_name='send_date',
        ),
        migrations.RemoveField(
            model_name='drchronoemail',
            name='year',
        ),
    ]
