# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0008_auto_20150216_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=datetime.datetime(2015, 2, 16, 20, 37, 10, 686672, tzinfo=utc), upload_to=b'images'),
            preserve_default=False,
        ),
    ]
