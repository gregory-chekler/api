# Generated by Django 2.2.5 on 2019-12-02 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0068_auto_20191125_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='calculator_action',
        ),
    ]
