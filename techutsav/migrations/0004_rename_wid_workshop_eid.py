# Generated by Django 4.0.4 on 2022-05-16 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techutsav', '0003_rename_workshop_extra_workshop_event_extra_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workshop',
            old_name='wid',
            new_name='eid',
        ),
    ]
