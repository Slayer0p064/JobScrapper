# Generated by Django 4.2.6 on 2024-12-21 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('View', '0002_job_employement_job_location_type_job_update_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='update_date',
        ),
    ]
