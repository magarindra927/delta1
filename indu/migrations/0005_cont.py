# Generated by Django 4.1.7 on 2023-07-26 07:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indu', '0004_tea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
