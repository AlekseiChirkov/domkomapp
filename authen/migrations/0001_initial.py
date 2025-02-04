# Generated by Django 2.2 on 2020-03-31 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=15, unique=True, verbose_name='Номер телефона')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Админ')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Персонал')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Суперпользователь')),
            ],
            options={
                'verbose_name': 'Регистрация номера',
                'verbose_name_plural': 'Регистрация номеров',
            },
        ),
    ]
