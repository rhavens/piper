# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alexandra', '0027_remove_comments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_post',
            name='user',
        ),
    ]
