# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sim',
            fields=[
                ('sim_id', models.AutoField(serialize=False, primary_key=True)),
                ('number', models.CharField(default=b'No Number', max_length=20)),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('operate', models.CharField(max_length=10, null=True, choices=[(b'1', b'\xe4\xb8\xad\xe8\x8f\xaf\xe9\x9b\xbb\xe4\xbf\xa1'), (b'2', b'\xe9\x81\xa0\xe5\x82\xb3\xe9\x9b\xbb\xe4\xbf\xa1'), (b'3', b'\xe5\x8f\xb0\xe7\x81\xa3\xe5\xa4\xa7\xe5\x93\xa5\xe5\xa4\xa7'), (b'4', b'\xe5\x8f\xb0\xe7\x81\xa3\xe4\xb9\x8b\xe6\x98\x9f'), (b'5', b'\xe4\xba\x9e\xe5\xa4\xaa\xe9\x9b\xbb\xe4\xbf\xa1')])),
                ('status', models.CharField(max_length=2, null=True, choices=[(b'1', b'\xe5\xb7\xa5\xe4\xbd\x9c\xe6\xb8\xac\xe8\xa9\xa6\xe7\x94\xa8'), (b'2', b'\xe5\x80\x9f\xe4\xbe\x86\xe6\x89\x93\xe5\x80\x8b\xe9\x9b\xbb\xe8\xa9\xb1'), (b'3', b'\xe8\x87\xa8\xe6\x99\x82\xe5\x80\x9f\xe7\x94\xa8'), (b'99', b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'SimCards',
            },
        ),
    ]
