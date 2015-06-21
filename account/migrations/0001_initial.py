# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(related_name=b'profile', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
                ('school', models.CharField(max_length=30, verbose_name='\u0428\u043a\u043e\u043b\u0430')),
                ('result', models.CharField(max_length=4, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
