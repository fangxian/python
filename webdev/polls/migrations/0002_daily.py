# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('daily_item', models.CharField(max_length=200)),
                ('daily_body', models.TextField(max_length=10000)),
                ('pub_date', models.DateTimeField(verbose_name='date publish')),
            ],
        ),
    ]
