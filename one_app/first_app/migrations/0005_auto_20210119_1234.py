# Generated by Django 2.2 on 2021-01-19 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20210119_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateField(default=datetime.datetime(2021, 1, 19, 12, 34, 54, 19015), verbose_name='date published'),
        ),
    ]
