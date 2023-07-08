# Generated by Django 4.2.1 on 2023-06-18 15:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.CharField(max_length=255, verbose_name='Почта')),
                ('comment', ckeditor.fields.RichTextField(blank=True, verbose_name='Комментарий')),
            ],
        ),
    ]
