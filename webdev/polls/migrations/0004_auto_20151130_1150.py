# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20151130_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyContext',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('daily_context', models.TextField(max_length=10000)),
            ],
        ),
        migrations.RemoveField(
            model_name='dailyitem',
            name='daily_body',
        ),
        migrations.AddField(
            model_name='dailycontext',
            name='body',
            field=models.ForeignKey(to='polls.DailyItem'),
        ),
    ]
