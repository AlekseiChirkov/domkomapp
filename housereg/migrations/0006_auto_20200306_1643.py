# Generated by Django 3.0.3 on 2020-03-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housereg', '0005_auto_20200306_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='people',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
