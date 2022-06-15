# Generated by Django 4.0 on 2022-06-07 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.DateTimeField(max_length=100, verbose_name='Урл фотографии')),
                ('sync_date', models.DateTimeField(auto_now=True, verbose_name='Синхронизированно')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Название картины')),
                ('description', models.CharField(blank=True, max_length=150, verbose_name='Описание картины')),
                ('category', models.CharField(blank=True, max_length=150, verbose_name='Наименование категории')),
            ],
        ),
    ]
