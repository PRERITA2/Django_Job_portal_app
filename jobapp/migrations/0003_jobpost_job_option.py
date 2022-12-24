# Generated by Django 4.1.4 on 2022-12-22 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_jobpost_expiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='job_option',
            field=models.CharField(choices=[('F', 'Full time'), ('P', 'Part time')], default='F', max_length=1),
        ),
    ]