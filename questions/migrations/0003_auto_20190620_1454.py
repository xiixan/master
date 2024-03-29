# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-20 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20190620_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u9898\u76ee\u7ea7\u522b')),
            ],
            options={
                'verbose_name': '\u7ea7\u522b',
                'verbose_name_plural': '\u7ea7\u522b',
            },
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '\u6807\u7b7e', 'verbose_name_plural': '\u6807\u7b7e'},
        ),
        migrations.AlterField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(to='questions.Tag', verbose_name='\u6807\u7b7e'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u9898\u76ee\u6807\u7b7e'),
        ),
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.ManyToManyField(to='questions.Level', verbose_name='\u7ea7\u522b'),
        ),
    ]
