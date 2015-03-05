# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0019_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=b'NULL', upload_to=b'Alexandra'),
            preserve_default=True,
        ),
    ]
