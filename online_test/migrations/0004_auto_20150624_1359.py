# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0003_auto_20150621_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '\u0412\u043e\u0441\u043f\u0440\u043e\u0441', 'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b'},
        ),
        migrations.AlterField(
            model_name='question',
            name='answer1',
            field=models.ImageField(upload_to=b'answers', verbose_name='\u041e\u0442\u0432\u0435\u0442 1'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer2',
            field=models.ImageField(upload_to=b'answers', verbose_name='\u041e\u0442\u0432\u0435\u0442 2'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer3',
            field=models.ImageField(upload_to=b'answers', verbose_name='\u041e\u0442\u0432\u0435\u0442 3'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer4',
            field=models.ImageField(upload_to=b'answers', verbose_name='\u041e\u0442\u0432\u0435\u0442 4'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='about',
            field=models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
    ]
