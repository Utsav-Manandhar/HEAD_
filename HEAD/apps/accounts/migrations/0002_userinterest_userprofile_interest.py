# Generated by Django 4.2.3 on 2023-07-24 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('normalized_name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='interest',
            field=models.ManyToManyField(blank=True, to='accounts.userinterest'),
        ),
    ]