# Generated by Django 4.1.3 on 2022-11-10 05:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_rename_user_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('auto_id', models.PositiveIntegerField(db_index=True, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.TextField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='Profile_pic')),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv')),
                ('cover_letter', models.FileField(blank=True, null=True, upload_to='cv')),
                ('cover_letter_two', models.FileField(blank=True, null=True, upload_to='cv')),
                ('linkedin_profile', models.FileField(blank=True, null=True, upload_to='cv')),
                ('company_cv', models.FileField(blank=True, null=True, upload_to='company_cv')),
                ('company_cv_two', models.FileField(blank=True, null=True, upload_to='company_cv_two')),
                ('linkedin_username', models.CharField(blank=True, max_length=30, null=True)),
                ('linkedin_password', models.CharField(blank=True, max_length=30, null=True)),
                ('university', models.CharField(blank=True, max_length=140, null=True)),
                ('university_dead_line', models.CharField(blank=True, max_length=140, null=True)),
                ('course_campus', models.CharField(blank=True, max_length=140, null=True)),
                ('course_title', models.CharField(blank=True, max_length=140, null=True)),
                ('course_start_date', models.CharField(blank=True, max_length=30, null=True)),
                ('course_end_date', models.CharField(blank=True, max_length=30, null=True)),
                ('company_name', models.CharField(blank=True, max_length=140, null=True)),
                ('designation', models.CharField(blank=True, max_length=140, null=True)),
                ('first_preferred_location', models.CharField(blank=True, max_length=140, null=True)),
                ('second_preferred_location', models.CharField(blank=True, max_length=140, null=True)),
                ('third_preferred_location', models.CharField(blank=True, max_length=140, null=True)),
                ('forth_preferred_location', models.CharField(blank=True, max_length=140, null=True)),
                ('working_type', models.CharField(blank=True, choices=[('Work', 'Work'), ('Internship', 'Internship')], max_length=80, null=True)),
                ('work_start_date', models.CharField(blank=True, max_length=80, null=True)),
                ('work_end_date', models.CharField(blank=True, max_length=80, null=True)),
                ('work_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('contract_submit_date', models.DateField(blank=True, null=True)),
                ('expr_certi_submit_date', models.DateField(blank=True, null=True)),
                ('first_job_sector', models.CharField(blank=True, max_length=50, null=True)),
                ('second_job_sector', models.CharField(blank=True, max_length=50, null=True)),
                ('third_job_sector', models.CharField(blank=True, max_length=50, null=True)),
                ('forth_job_sector', models.CharField(blank=True, max_length=50, null=True)),
                ('first_job_role', models.CharField(blank=True, max_length=50, null=True)),
                ('second_job_role', models.CharField(blank=True, max_length=50, null=True)),
                ('third_job_role', models.CharField(blank=True, max_length=50, null=True)),
                ('forth_job_role', models.CharField(blank=True, max_length=50, null=True)),
                ('course_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('visa_start_date', models.DateField(blank=True, null=True)),
                ('visa_end_date', models.DateField(blank=True, null=True)),
                ('fees_paid', models.BooleanField(default=False)),
                ('application_submitted', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student_account', to='account.account')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='account.account')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Student',
                'db_table': 'student',
                'ordering': ('-date_added',),
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(db_index=True, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Passed', 'Passed'), ('Not_assigned_yet', 'Not Assigned yet'), ('Ongoing', 'Ongoing'), ('Failed', 'Failed'), ('Submitted', 'Submitted'), ('Not_selected', 'Not selected')], max_length=30, null=True)),
                ('description', models.CharField(blank=True, max_length=140, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='account.account')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='specialization_student', to='student.student')),
            ],
            options={
                'verbose_name': 'specilizations',
                'verbose_name_plural': 'specilizations',
                'db_table': 'specilizations',
            },
        ),
    ]
