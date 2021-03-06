# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-25 03:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hood', '0003_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='email_address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Neighborhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
