# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
