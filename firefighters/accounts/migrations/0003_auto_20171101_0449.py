# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 04:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170929_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('A', 'ACTIVE'), ('D', 'DEACTIVE'), ('E', 'ELIMINATED')], default='A', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='user',
            name='registration_date',
        ),
        migrations.AddField(
            model_name='user',
            name='document',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 11, 1, 4, 49, 29, 277979)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('A', 'ACTIVE'), ('D', 'DEACTIVE'), ('E', 'ELIMINATED')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
    ]
