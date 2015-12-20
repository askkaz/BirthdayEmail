# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdayEmails', '0003_auto_20151119_0554'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrchronoEmail',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('birthday', models.DateTimeField()),
                ('sent_date', models.DateTimeField(blank=True)),
                ('subject', models.CharField(max_length=77)),
                ('body', models.TextField()),
                ('patient_id', models.IntegerField()),
            ],
        ),
    ]
