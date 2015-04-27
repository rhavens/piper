# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0023_auto_20150414_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=225)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
