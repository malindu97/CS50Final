# Generated by Django 3.0.6 on 2020-05-21 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20200521_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='picture',
            field=models.ImageField(upload_to='media'),
        ),
    ]
