# Generated by Django 3.1.1 on 2020-09-08 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='key',
            field=models.CharField(default='Secret Key', max_length=1500, verbose_name='User Secret Key'),
        ),
    ]
