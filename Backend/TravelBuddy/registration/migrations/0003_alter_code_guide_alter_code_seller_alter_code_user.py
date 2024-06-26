# Generated by Django 5.0 on 2024-04-12 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_guide_verify_seller_sellertype_seller_verify_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='guide',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.guide'),
        ),
        migrations.AlterField(
            model_name='code',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.seller'),
        ),
        migrations.AlterField(
            model_name='code',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.user'),
        ),
    ]
