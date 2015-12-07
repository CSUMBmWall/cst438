# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20151113_2256'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
