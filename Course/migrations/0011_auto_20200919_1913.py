# Generated by Django 3.1.1 on 2020-09-19 19:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0010_auto_20200914_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 19, 19, 13, 29, 736523, tzinfo=utc), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='courses_video',
            name='video',
            field=models.TextField(default='Lecture.mp4', verbose_name='Video Name'),
        ),
    ]
