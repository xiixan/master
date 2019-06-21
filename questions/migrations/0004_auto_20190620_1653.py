# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-20 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20190620_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='level',
        ),
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.Level', verbose_name='\u7ea7\u522b'),
        ),
    ]