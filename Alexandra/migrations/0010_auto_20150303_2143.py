# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0009_auto_20150216_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image_key',
            field=models.ImageField(default=b'', upload_to=b'Alexandra'),
            preserve_default=True,
        ),
    ]
