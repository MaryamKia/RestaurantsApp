# Generated by Django 2.1.5 on 2019-02-12 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_restaurantlocation_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
