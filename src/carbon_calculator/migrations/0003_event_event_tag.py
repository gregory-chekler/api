# Generated by Django 3.0.5 on 2020-04-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_calculator', '0002_auto_20191202_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_tag',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]