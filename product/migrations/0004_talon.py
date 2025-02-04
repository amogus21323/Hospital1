# Generated by Django 5.0.6 on 2024-07-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_appointment_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('appointmentDate', models.DateField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('symptoms', models.CharField(max_length=40, null=True)),
                ('_id', models.CharField(max_length=40, null=True)),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name': 'Талон',
                'verbose_name_plural': 'Талон',
            },
        ),
    ]
