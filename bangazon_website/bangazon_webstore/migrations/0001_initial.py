# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=30)),
                ('card_number', models.CharField(max_length=25)),
                ('cvv', models.CharField(max_length=4)),
                ('expiration', models.DateField()),
                ('name_on_card', models.CharField(max_length=55)),
            ],
            options={
                'verbose_name_plural': 'PaymentTypes',
            },
        ),
    ]