# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_daily'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Daily',
            new_name='DailyItem',
        ),
    ]
