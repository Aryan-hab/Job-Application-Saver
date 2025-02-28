# Generated by Django 5.1 on 2024-08-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applied_jobs', '0005_job_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('PE', 'Pending'), ('INT', 'Interview Invitation'), ('RE', 'Rejected'), ('WI', 'Withdrawn by candidate')], default='PE', max_length=30),
        ),
    ]
