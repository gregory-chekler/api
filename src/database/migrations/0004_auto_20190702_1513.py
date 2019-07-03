# Generated by Django 2.2.2 on 2019-07-02 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20190702_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailcategory',
            options={'verbose_name_plural': 'Email Categories'},
        ),
        migrations.AlterModelOptions(
            name='eventattendees',
            options={'verbose_name_plural': 'Event Attendees'},
        ),
        migrations.AlterModelOptions(
            name='policy',
            options={'ordering': ('name',), 'verbose_name_plural': 'Legal Policies'},
        ),
        migrations.RemoveField(
            model_name='tagcollection',
            name='tags',
        ),
    ]
