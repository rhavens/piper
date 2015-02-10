# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0002_auto_20150209_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts_comments',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.RemoveField(
            model_name='posts_comments',
            name='post',
        ),
        migrations.DeleteModel(
            name='Posts_comments',
        ),
        migrations.RemoveField(
            model_name='user_post',
            name='post',
        ),
        migrations.RemoveField(
            model_name='user_post',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='User_post',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-last_modified'], 'get_latest_by': 'last_modified'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
