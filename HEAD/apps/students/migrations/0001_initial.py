# Generated by Django 4.2.3 on 2023-07-24 12:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('university', models.CharField(blank=True, max_length=64, null=True)),
                ('professor', models.CharField(blank=True, max_length=64, null=True)),
                ('age', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
