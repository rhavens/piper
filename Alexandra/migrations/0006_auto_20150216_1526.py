# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0005_auto_20150216_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=filebrowser.fields.FileBrowseField(max_length=200, null=True, verbose_name=b'Image', blank=True),
            preserve_default=True,
        ),
    ]
