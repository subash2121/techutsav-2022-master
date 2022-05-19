from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


dept_choices = (
    ('FIRST YEAR', 'FIRST YEAR'),
    ('SECOND YEAR', 'SECOND YEAR'),
    ('THIRD YEAR', 'THIRD YEAR'),
    ('FOURTH YEAR', 'FOURTH YEAR'),
    ('FIFTH YEAR', 'FIFTH YEAR'),
)


deptsss_choices = (
    ('MECH', 'MECH'),
    ('MECHATRONICS', 'MECHATRONICS'),
    ('CIVIL', 'CIVIL'),
    ('EEE', 'EEE'),
    ('ECE', 'ECE'),
    ('CSE', 'CSE'),
    ('IT', 'IT'),
    ('MCA', 'MCA'),
    ('ARCH', 'ARCH'),
    ('BIOMEDICAL', 'BIOMEDICAL'),
    ('OTHERS', 'OTHERS'),
)


class Profile(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(
        null=True, choices=deptsss_choices, max_length=100)
    rollno = models.CharField(null=True, max_length=50)
    college = models.CharField(null=True, max_length=150)
    phno = models.CharField(null=True, max_length=20)
    year = models.CharField(null=True, choices=dept_choices, max_length=20)
    recievedkit=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user_name.username) + " " + str(self.phno)
