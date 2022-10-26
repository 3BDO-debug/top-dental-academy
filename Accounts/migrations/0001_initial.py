# Generated by Django 3.1.1 on 2020-09-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('full_name', models.CharField(max_length=500, verbose_name='Full Name')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last name')),
                ('email', models.EmailField(default='email@example.com', max_length=60, unique=True)),
                ('profile_pic', models.ImageField(blank=True, default='media/profile.jpeg', null=True, upload_to='')),
                ('mobile', models.CharField(blank=True, default='Phone Number', max_length=300, null=True)),
                ('number', models.CharField(blank=True, default='Address', max_length=350, null=True)),
                ('street', models.CharField(blank=True, default='Address', max_length=350, null=True)),
                ('city', models.CharField(blank=True, default='Address', max_length=350, null=True)),
                ('country', models.CharField(blank=True, default='Address', max_length=350, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False, verbose_name='Approve account')),
                ('status', models.CharField(default='Online', max_length=150)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
