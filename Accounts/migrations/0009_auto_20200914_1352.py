# Generated by Django 3.1.1 on 2020-09-14 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_auto_20200914_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='purchased_courses',
            new_name='user_purchased_courses',
        ),
    ]
