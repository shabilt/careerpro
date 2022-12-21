# Generated by Django 4.1.3 on 2022-12-12 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0005_alter_specialization_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentNote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(db_index=True, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='student.student')),
            ],
            options={
                'verbose_name': 'Student_Note',
                'verbose_name_plural': 'Student_Note',
                'db_table': 'student_note',
                'ordering': ('-date_added',),
            },
        ),
    ]