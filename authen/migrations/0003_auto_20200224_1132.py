# Generated by Django 3.0.3 on 2020-02-24 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_auto_20200224_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=15, unique=True, verbose_name='Номер телефона'),
        ),
    ]
