# Generated by Django 4.0.1 on 2022-01-13 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent_de', models.CharField(blank=True, max_length=20)),
                ('continent_en', models.CharField(blank=True, max_length=20)),
                ('continent_sr', models.CharField(max_length=20)),
            ],
        ),
    ]
