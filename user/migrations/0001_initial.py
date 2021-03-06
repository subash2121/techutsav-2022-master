# Generated by Django 4.0.4 on 2022-05-08 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('MECH', 'MECH'), ('MECHATRONICS', 'MECHATRONICS'), ('CIVIL', 'CIVIL'), ('EEE', 'EEE'), ('ECE', 'ECE'), ('CSE', 'CSE'), ('IT', 'IT'), ('MCA', 'MCA'), ('ARCH', 'ARCH'), ('BIOMEDICAL', 'BIOMEDICAL'), ('OTHERS', 'OTHERS')], max_length=100, null=True)),
                ('rollno', models.CharField(max_length=50, null=True)),
                ('college', models.CharField(max_length=150, null=True)),
                ('phno', models.CharField(max_length=20, null=True)),
                ('year', models.CharField(choices=[('FIRST YEAR', 'FIRST YEAR'), ('SECOND YEAR', 'SECOND YEAR'), ('THIRD YEAR', 'THIRD YEAR'), ('FOURTH YEAR', 'FOURTH YEAR'), ('FIFTH YEAR', 'FIFTH YEAR')], max_length=20, null=True)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
