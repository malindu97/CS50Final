# Generated by Django 3.0.6 on 2020-05-25 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0007_images_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image_vote',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes_num', models.IntegerField(default=0)),
                ('imageid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='photo.images')),
                ('userid', models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
