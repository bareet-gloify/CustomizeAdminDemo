# Generated by Django 3.2.7 on 2021-10-05 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20211005_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='college',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='my_app.college'),
        ),
    ]
