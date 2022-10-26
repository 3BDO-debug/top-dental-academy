# Generated by Django 3.1.1 on 2020-09-04 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350, verbose_name='Book Name')),
                ('category', models.CharField(max_length=350, verbose_name="Book's Category")),
                ('author', models.CharField(max_length=350, verbose_name='Book Author')),
                ('content', models.FileField(upload_to='', verbose_name='Book File ex:book.pdf')),
                ('short_desc', models.CharField(max_length=350, verbose_name="Book's Short Description")),
                ('book_thumbnail', models.ImageField(upload_to='', verbose_name='Book Thumbnail')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(verbose_name='Book Price')),
                ('is_downloadable', models.BooleanField(verbose_name='Can Be Downlaoded')),
            ],
        ),
    ]
