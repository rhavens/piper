# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0015_auto_20150303_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(default=b'NULL', upload_to=b'Alexandra/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='text_content',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
