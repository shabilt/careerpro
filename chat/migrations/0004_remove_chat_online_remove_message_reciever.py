# Generated by Django 4.1.3 on 2022-12-13 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chat_chatmember_alter_message_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='online',
        ),
        migrations.RemoveField(
            model_name='message',
            name='reciever',
        ),
    ]
