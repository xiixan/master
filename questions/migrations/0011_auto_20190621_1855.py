# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-21 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_tag_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='level',
        ),
        migrations.AddField(
            model_name='level',
            name='level',
            field=models.IntegerField(blank=True, choices=[(1, '\u9752\u94dc'), (2, '\u767d\u94f6'), (3, '\u9ec4\u91d1'), (4, '\u5927\u4f6c')], default=1, null=True, verbose_name='\u7b49\u7ea7'),
        ),
    ]
