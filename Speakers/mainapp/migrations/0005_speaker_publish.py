# Generated by Django 3.1.6 on 2021-02-14 04:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210212_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
