# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-26 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsarticles', '0010_trained_coding_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainedLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('coding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsarticles.TrainedCoding')),
            ],
        ),
    ]
