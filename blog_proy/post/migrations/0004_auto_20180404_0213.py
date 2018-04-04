# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 02:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20180404_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='empresa',
        ),
        migrations.AddField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='post.Blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='empresa',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empresas', to='empresa.Empresa'),
        ),
    ]
