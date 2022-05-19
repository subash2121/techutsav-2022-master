# Generated by Django 4.0.4 on 2022-05-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techutsav', '0004_rename_wid_workshop_eid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AlterField(
            model_name='project',
            name='no_of_participants',
            field=models.CharField(blank=True, default='Max 3', max_length=60, null=True),
        ),
    ]
