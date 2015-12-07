# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='updated',
        ),
        migrations.AddField(
            model_name='signup',
            name='search',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
