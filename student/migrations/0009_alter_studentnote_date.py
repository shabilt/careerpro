# Generated by Django 4.1.3 on 2022-12-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_alter_student_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentnote',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
