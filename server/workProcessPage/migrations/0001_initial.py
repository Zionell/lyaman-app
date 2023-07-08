# Generated by Django 4.2.1 on 2023-06-18 15:43

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkProcessPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Процесс работы', max_length=255, verbose_name='Заголовок страницы')),
            ],
            options={
                'verbose_name': 'Процесс работы',
                'verbose_name_plural': 'Процесс работы',
            },
        ),
        migrations.CreateModel(
            name='WorkProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', ckeditor.fields.RichTextField(blank=True, verbose_name='Описание')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='workProcessPage.workprocesspage', verbose_name='Процесс работы')),
            ],
            options={
                'verbose_name': 'Процесс выполнения',
                'verbose_name_plural': 'Процесс выполнения',
                'ordering': ('order',),
            },
        ),
    ]