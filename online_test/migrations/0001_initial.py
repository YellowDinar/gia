# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('lecture', models.FileField(upload_to=b'lectures')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to=b'questions', blank=True)),
                ('answer1', models.CharField(max_length=40, blank=True)),
                ('answer2', models.CharField(max_length=40, blank=True)),
                ('answer3', models.CharField(max_length=40, blank=True)),
                ('answer4', models.CharField(max_length=40, blank=True)),
                ('correct_answer', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('about', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(to='online_test.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lecture',
            name='topic',
            field=models.ForeignKey(to='online_test.Topic'),
            preserve_default=True,
        ),
    ]
