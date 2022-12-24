# Generated by Django 4.1.4 on 2022-12-22 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_jobpost_job_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AddConstraint(
            model_name='author',
            constraint=models.UniqueConstraint(fields=('name', 'designation', 'company'), name='Author_unique_combination'),
        ),
        migrations.AddConstraint(
            model_name='joblocation',
            constraint=models.UniqueConstraint(fields=('city', 'state', 'country'), name='Job_location_unique_combination'),
        ),
    ]
