# Generated by Django 2.2.9 on 2020-03-11 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0083_testimonial_other_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='deep_dive',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]
