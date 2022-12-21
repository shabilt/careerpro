from rest_framework import serializers
# from careerpro import student
from account.models import Account
from account.serializers import AccountSerializer, RegistrationSerializer
from main.functions import get_auto_id, password_generater, send_common_mail
from student.models import Specialization, Student,JobApplication
from chat.models import Chat,ChatMember,Message
from django.db import transaction

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            'id',
            'name',
            'is_group'
        ]


class ChatMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMember
        fields = [
            'id',
            'chat',
            'account'
        ]
        extra_kwargs = {
            'account':{'read_only': True},
            'id':{'read_only': True},
        }

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'chat',
            'sender',
            'content',
            'timestamp',
            'read'
        ]



