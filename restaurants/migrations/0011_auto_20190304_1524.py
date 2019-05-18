# Generated by Django 2.1.5 on 2019-03-04 15:24

from django.db import migrations, models
import restaurants.validator


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_restaurantlocation_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[restaurants.validator.validate_category]),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]