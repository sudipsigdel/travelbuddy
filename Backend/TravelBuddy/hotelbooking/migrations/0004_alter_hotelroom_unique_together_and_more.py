# Generated by Django 5.0 on 2024-04-13 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0003_remove_hotel_rating'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hotelroom',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='hotelroom',
            name='roomDescription',
        ),
        migrations.RemoveField(
            model_name='hotelroom',
            name='roomImage',
        ),
        migrations.RemoveField(
            model_name='hotelroom',
            name='roomNo',
        ),
    ]
