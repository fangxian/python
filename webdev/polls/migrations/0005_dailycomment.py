# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20151130_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyComment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comment_context', models.CharField(max_length=500)),
                ('comment', models.ForeignKey(to='polls.DailyContext')),
            ],
        ),
    ]
