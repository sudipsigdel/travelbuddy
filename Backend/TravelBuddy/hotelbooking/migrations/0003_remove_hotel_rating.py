# Generated by Django 5.0 on 2024-04-11 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0002_hotelroombooking_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='rating',
        ),
    ]