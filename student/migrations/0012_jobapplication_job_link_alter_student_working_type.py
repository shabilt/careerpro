# Generated by Django 4.0 on 2023-01-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_alter_student_visa_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='job_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='working_type',
            field=models.CharField(blank=True, choices=[('Placement', 'Placement'), ('Internship', 'Internship')], max_length=80, null=True),
        ),
    ]
