# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(blank=True, max_length=40, choices=[(b'A', models.CharField(max_length=40, blank=True)), (b'B', models.CharField(max_length=40, blank=True)), (b'C', models.CharField(max_length=40, blank=True)), (b'D', models.CharField(max_length=40, blank=True))]),
        ),
    ]
