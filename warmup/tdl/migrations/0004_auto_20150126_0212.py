# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tdl', '0003_auto_20150126_0208'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='List',
            new_name='Things_TO_Do',
        ),
    ]
