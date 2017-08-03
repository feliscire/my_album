# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, default='No title')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('favorite', models.BooleanField(default=False)),
                ('comment', models.CharField(blank=True, max_length=200)),
                ('category', models.ForeignKey(blank=True, null=True, to='album.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
