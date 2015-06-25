# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20150624_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='result',
            field=models.IntegerField(null=True),
        ),
    ]
