# Generated by Django 5.1 on 2024-08-24 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applied_jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
    ]
