# Generated by Django 4.0.4 on 2022-04-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='max_temp',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='weather',
            name='min_temp',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='weather',
            name='the_temp',
            field=models.FloatField(default=0),
        ),
    ]