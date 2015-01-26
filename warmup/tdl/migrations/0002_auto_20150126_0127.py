# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tdl', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='list',
            name='Content',
            field=models.TextField(default='input'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
