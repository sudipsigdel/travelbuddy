# Generated by Django 4.1.7 on 2024-04-09 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideHire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('status', models.CharField(default='ongoing', max_length=50)),
                ('day', models.IntegerField()),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hireguide', to='registration.guide')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hireuser', to='registration.user')),
            ],
        ),
    ]
