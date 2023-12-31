# Generated by Django 4.1.7 on 2023-07-26 07:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indu', '0003_alter_coffy_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
