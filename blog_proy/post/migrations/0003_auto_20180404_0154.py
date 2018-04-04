# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 01:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
        ('post', '0002_comments_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='empresas', to='empresa.Empresa')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empresas_blog', to='empresa.Empresa'),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draf', 'borrador'), ('published', 'publicado')], default='draf', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(choices=[('D', 'Deportes'), ('F', 'Finanzas'), ('C', 'Cultura')], db_index=True, default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='blog',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='post.Post'),
        ),
    ]