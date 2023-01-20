from django.db import models
from rest_framework import serializers
from account.models import Account
from main.functions import  password_generater, send_common_mail






class RegistrationSerializer(serializers.ModelSerializer):

    # password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email','username','phone','password','full_name','role']
        extra_kwargs = {
                'password': {'write_only': True},
        }    


    def save(self):

        user = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            phone=self.validated_data['phone'],
            full_name=self.validated_data['full_name'],
            role = self.validated_data['role']
            
        )
        password = self.validated_data['password']
        # password2 = self.validated_data['password2']
        # if password != password2:
        #     raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class AccountPropertiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['pk', 'email']

class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','email', 'phone','full_name',]

# ===================================================================================

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','full_name','email','phone',]

    def create(self, validated_data):
        password = password_generater(8)
        validated_data["password"] = password
        validated_data["password2"] = password
        validated_data["role"] = "admin"
        if(not Account.objects.filter(email=validated_data["email"]).exists()):
            account_serializer = RegistrationSerializer(data=validated_data)
            if account_serializer.is_valid():
                account = account_serializer.save()
                # from_email = "mail.osperb@gmail.com"
                to_email = account.email
                subject = "admin Registration Completed"
                html_context = {
                    "title":"admin Registration Completed",
                    "data":[
                        {
                            "label":"username",
                            "value":account.username
                        },
                        {
                            "label":"First Name",
                            "value":account.full_name
                        },
                        {
                            "label":"email",
                            "value":account.email
                        },
                        {
                            "label":"phone",
                            "value":account.phone
                        },
                        {
                            "label":"password",
                            "value":password
                        }
                    ]
                }
                text_content = str(html_context)
                send_common_mail(html_context,to_email,subject)
        else:
            raise serializers.ValidationError({'email': 'Email already exists !'})
        
      
        return account

    def update(self, instance, validated_data):
        instance.save()

        try:
            email = validated_data["email"]
        except:
            username = ""
            email = ""
        if((not Account.objects.filter(email=email).exists()) or Account.objects.filter(pk = instance.pk ,email=email).exists()):
            account = Account.objects.get(pk=instance.pk)
            account.full_name = validated_data.get('full_name', account.full_name)
            account.email = validated_data.get('email', account.full_name)
            account.phone = validated_data.get('phone', account.phone)
            account.save()
    
            return account
        else:
            raise serializers.ValidationError({'error_message': 'Email already exists !'})
       