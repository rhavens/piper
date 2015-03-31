# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0006_auto_20150216_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(null=True, upload_to=b'images'),
            preserve_default=True,
        ),
    ]
