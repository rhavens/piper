# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0020_auto_20150304_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=254)),
                ('birthday', models.IntegerField(verbose_name=8)),
                ('gender', models.CharField(default=b'O', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
