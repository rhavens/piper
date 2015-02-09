# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=60)),
                ('content', models.CharField(max_length=1024)),
                ('timestamp', models.DateTimeField(verbose_name=b'Posted: ')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text_content', models.CharField(max_length=200)),
                ('image_key', models.CharField(max_length=1024)),
                ('timestamp', models.DateTimeField(verbose_name=b'Posted: ')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Posts_comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(to='Alexandra.Comment')),
                ('post', models.ForeignKey(to='Alexandra.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=254)),
                ('birthday', models.IntegerField(verbose_name=8)),
                ('gender', models.CharField(default=b'O', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post', models.ForeignKey(to='Alexandra.Post')),
                ('user', models.ForeignKey(to='Alexandra.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
