# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tdl', '0004_auto_20150126_0212'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Things_TO_Do',
            new_name='To_do',
        ),
    ]
