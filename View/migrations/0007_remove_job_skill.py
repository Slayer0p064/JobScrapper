# Generated by Django 4.2.6 on 2024-12-21 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('View', '0006_job_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='skill',
        ),
    ]
