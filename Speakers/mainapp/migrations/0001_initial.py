# Generated by Django 3.1.6 on 2021-02-12 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speakerid', models.CharField(db_index=True, max_length=64, verbose_name='id')),
                ('radius', models.IntegerField(max_length=64, verbose_name='радиус звукопокрытия')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=64, verbose_name='широта')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=64, verbose_name='долгота')),
                ('address', models.TextField(max_length=64, verbose_name='адрес размещения')),
                ('speaker_type', models.IntegerField(choices=[(1, 'Сирена'), (2, 'Громкоговоритель')], verbose_name='тип устройства')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
