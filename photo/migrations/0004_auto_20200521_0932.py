# Generated by Django 3.0.6 on 2020-05-21 04:02

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20200521_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='picture',
            field=models.ImageField(upload_to=django.contrib.auth.models.User),
        ),
    ]