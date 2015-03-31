# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0003_auto_20150210_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_key',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images'),
            preserve_default=True,
        ),
    ]
