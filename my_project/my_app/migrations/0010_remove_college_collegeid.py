# Generated by Django 3.2.7 on 2021-10-05 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_alter_student_college'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='collegeId',
        ),
    ]
