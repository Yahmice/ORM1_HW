# Generated by Django 4.2.9 on 2024-01-10 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='slug',
        ),
    ]