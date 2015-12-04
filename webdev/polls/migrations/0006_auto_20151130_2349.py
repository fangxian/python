# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_dailycomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailycontext',
            name='daily_image',
            field=models.ImageField(blank=True, upload_to='photo', null=True),
        ),
        migrations.AlterField(
            model_name='dailycomment',
            name='comment',
            field=models.ForeignKey(to='polls.DailyItem'),
        ),
    ]
