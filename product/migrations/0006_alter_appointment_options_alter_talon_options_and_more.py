# Generated by Django 5.0.6 on 2024-07-28 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_appointment_talon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Встреча', 'verbose_name_plural': 'Встречи'},
        ),
        migrations.AlterModelOptions(
            name='talon',
            options={'verbose_name': 'Талон', 'verbose_name_plural': 'Талоны'},
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctorName',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patientName',
        ),
        migrations.RemoveField(
            model_name='talon',
            name='appointmentDate',
        ),
        migrations.RemoveField(
            model_name='talon',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='talon',
            name='doctorName',
        ),
        migrations.RemoveField(
            model_name='talon',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='talon',
            name='patientName',
        ),
        migrations.RemoveField(
            model_name='talon',
            name='symptoms',
        ),
    ]
