# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationTable',
            fields=[
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=128)),
                ('phone_num', models.IntegerField()),
            ],
        ),
    ]