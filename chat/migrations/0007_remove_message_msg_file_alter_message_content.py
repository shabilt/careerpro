# Generated by Django 4.0 on 2023-01-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_messagefile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='msg_file',
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(),
        ),
    ]