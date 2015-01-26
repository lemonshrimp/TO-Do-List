# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tdl', '0002_auto_20150126_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='Content',
            field=models.TextField(max_length=250),
            preserve_default=True,
        ),
    ]
