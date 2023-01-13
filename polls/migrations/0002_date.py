# Generated by Django 4.1.5 on 2023-01-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('salary', models.FloatField(verbose_name='Оклад')),
                ('salary_currency', models.TextField(blank=True, verbose_name='Валюта')),
                ('area_name', models.TextField(blank=True)),
                ('published_at', models.DateTimeField(auto_now=True, verbose_name='Время публикации')),
            ],
        ),
    ]
