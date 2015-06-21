# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0002_auto_20150620_1604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecture',
            options={'verbose_name': '\u041b\u0435\u043a\u0446\u0438\u044f', 'verbose_name_plural': '\u041b\u0435\u043a\u0446\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441', 'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': '\u0422\u043e\u043f\u0438\u043a', 'verbose_name_plural': '\u0422\u043e\u043f\u0438\u043a\u0438'},
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecture',
            field=models.FileField(upload_to=b'lectures', verbose_name='\u041b\u0435\u043a\u0446\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer1',
            field=models.CharField(max_length=40, verbose_name='\u041e\u0442\u0432\u0435\u0442 1', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer2',
            field=models.CharField(max_length=40, verbose_name='\u041e\u0442\u0432\u0435\u0442 2', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer3',
            field=models.CharField(max_length=40, verbose_name='\u041e\u0442\u0432\u0435\u0442 3', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer4',
            field=models.CharField(max_length=40, verbose_name='\u041e\u0442\u0432\u0435\u0442 4', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(max_length=40, verbose_name='\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442'),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(upload_to=b'questions', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=300, verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
    ]
