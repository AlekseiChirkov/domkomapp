# Generated by Django 2.2 on 2020-03-31 02:23

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
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256, verbose_name='Адрес')),
                ('house_number', models.CharField(max_length=16, verbose_name='Номер дома')),
                ('people', models.IntegerField(blank=True, default=0, null=True, verbose_name='Кол-во жителей')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
            },
        ),
        migrations.CreateModel(
            name='UsersInHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people_count', models.IntegerField(default=None, verbose_name='Кол-во жителей')),
                ('house', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='housereg.House', verbose_name='Дом')),
                ('person', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL, verbose_name='Житель')),
            ],
            options={
                'verbose_name': 'Житель',
                'verbose_name_plural': 'Все жители',
            },
        ),
    ]
