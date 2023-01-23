# Generated by Django 4.0 on 2023-01-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_account_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=60, unique=True, verbose_name='email'),
        ),
    ]