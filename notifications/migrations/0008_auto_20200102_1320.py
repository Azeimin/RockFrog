# Generated by Django 2.2.7 on 2020-01-02 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_auto_20191231_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='not_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 2, 13, 20, 43, 871724), verbose_name='date published'),
        ),
    ]
