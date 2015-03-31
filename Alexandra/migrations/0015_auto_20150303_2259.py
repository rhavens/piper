# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0014_auto_20150303_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text_content',
            field=models.FileField(max_length=200, upload_to=b''),
            preserve_default=True,
        ),
    ]
