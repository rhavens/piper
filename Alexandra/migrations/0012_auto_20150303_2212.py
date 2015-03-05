# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0011_auto_20150303_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image_key',
            field=models.ImageField(default=b'NULL', max_length=1024, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='text_content',
            field=models.ImageField(max_length=200, upload_to=b''),
            preserve_default=True,
        ),
    ]
