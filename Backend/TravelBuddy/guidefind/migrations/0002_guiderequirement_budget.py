# Generated by Django 5.0 on 2024-04-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidefind', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guiderequirement',
            name='budget',
            field=models.IntegerField(null=True),
        ),
    ]
