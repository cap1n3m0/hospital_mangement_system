# Generated by Django 4.0.5 on 2022-06-23 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('hospital', '0005_alter_appointments_doctor_time_slots_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorservices',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.doctors'),
        ),
    ]
