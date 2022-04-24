# Generated by Django 4.0.4 on 2022-04-24 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0002_alter_weather_max_temp_alter_weather_min_temp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='applicable_date',
            field=models.DateTimeField(unique=True, verbose_name='applicable_date'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
