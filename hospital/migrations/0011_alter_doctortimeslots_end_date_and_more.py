# Generated by Django 4.0.5 on 2022-07-01 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_alter_appointments_doctor_time_slots_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctortimeslots',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='doctortimeslots',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
