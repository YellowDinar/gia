# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0015_auto_20150624_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.ImageField(upload_to=b'', verbose_name='\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442', choices=[(b'a', models.ImageField(upload_to=b'answers', verbose_name='\u041e\u0442\u0432\u0435\u0442 1')), (b'b', models.ImageField(upload_to=b'answers', verbose_name='\u041e\u0442\u0432\u0435\u0442 2')), (b'c', models.ImageField(upload_to=b'answers', verbose_name='\u041e\u0442\u0432\u0435\u0442 3')), (b'd', models.ImageField(upload_to=b'answers', verbose_name='\u041e\u0442\u0432\u0435\u0442 4'))]),
        ),
    ]
