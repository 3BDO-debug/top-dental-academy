# Generated by Django 3.1.1 on 2020-09-14 17:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0009_auto_20200914_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 14, 17, 1, 9, 745953, tzinfo=utc), verbose_name='Created At'),
        ),
    ]
