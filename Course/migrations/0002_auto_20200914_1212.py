# Generated by Django 3.1.1 on 2020-09-14 12:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 14, 12, 12, 30, 781081, tzinfo=utc), verbose_name='Created At'),
        ),
    ]
