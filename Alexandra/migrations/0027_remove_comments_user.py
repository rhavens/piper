# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0026_auto_20150426_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
    ]
