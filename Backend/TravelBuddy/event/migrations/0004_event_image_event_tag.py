# Generated by Django 5.0 on 2024-03-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to='event'),
        ),
        migrations.AddField(
            model_name='event',
            name='tag',
            field=models.TextField(null=True),
        ),
    ]