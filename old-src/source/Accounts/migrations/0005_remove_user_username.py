# Generated by Django 3.1.1 on 2020-09-09 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
