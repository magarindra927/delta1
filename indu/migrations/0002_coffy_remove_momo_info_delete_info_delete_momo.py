# Generated by Django 4.1.7 on 2023-07-25 16:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('photo', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
            ],
        ),
        migrations.RemoveField(
            model_name='momo',
            name='info',
        ),
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.DeleteModel(
            name='Momo',
        ),
    ]
