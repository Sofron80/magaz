# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 03:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazin', '0010_auto_20160517_0326'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('slug',)]),
        ),
        migrations.AlterUniqueTogether(
            name='tovar',
            unique_together=set([('slug',)]),
        ),
    ]