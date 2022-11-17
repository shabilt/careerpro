from rest_framework import serializers
# from careerpro import student
from account.models import Account
from account.serializers import AccountSerializer, RegistrationSerializer
from main.functions import get_auto_id, password_generater, send_common_mail
from student.models import Specialization, Student


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = [
            'id',
            'title',
            'status',
            'description',
            'student'
        ]

        extra_kwargs = {
        'auto_id':{'read_only': True},
        }
    def create(self, validated_data):
        specialization = Specialization.objects.create(
            **validated_data,
            auto_id = get_auto_id(Specialization),
            # creator = self.context['request'].user
            # creator = self.context['request'].user
        )
        # print("ser",self.context['request'].user)
        # print("sessr",self.context['request'])

        return specialization
        
    # def create(self, validated_data):
    #     specialization = Specialization.objects.create(
    #         **validated_data,
    #         auto_id = get_auto_id(Specialization),
    #         creator = self.context['request'].user
    #     )
    #     return specialization

    
    # def create(self, validated_data):
    #     specialization = Specialization.objects.create(
    #         **validated_data,
    #         auto_id = get_auto_id(Specialization),
    #         creator = self.context['request'].user
    #     )
    #     return specialization




    class AccountSerializer(serializers.ModelSerializer):
        class Meta:
            model = Account
            fields = ['email', 'username', 'phone','full_name','role']




      

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)
    full_name = serializers.CharField(write_only=True)
    account = AccountSerializer(read_only=True)
    class Meta:
        model = Student
        fields =  [
            'full_name',
            'username',
            'email',
            'phone',
            'account',
            'id',
            'account',
            'address',
            'dob',
            'profilepic',
            'cv',
            'cover_letter',
            'cover_letter_two',
            'linkedin_profile',
            'company_cv',
            'company_cv_two',
            'linkedin_username',
            'linkedin_password',
            'university',
            'university_dead_line',
            'course_campus',
            'course_title',
            'course_start_date',
            'course_end_date',
            'company_name',
            'designation',
            'first_preferred_location',
            'second_preferred_location',
            'third_preferred_location',
            'forth_preferred_location',
            'working_type',
            'work_start_date',
            'work_end_date',
            'work_duration',
            'contract_submit_date',
            'expr_certi_submit_date',
            'first_job_sector',
            'second_job_sector',
            'third_job_sector',
            'forth_job_sector',
            'first_job_role',
            'second_job_role',
            'third_job_role',
            'forth_job_role',
            'course_duration',
            'visa_start_date',
            'visa_end_date',
            'fees_paid',
            'application_submitted']


    def create(self, validated_data):
        password = password_generater(8)
        validated_data["password"] = password
        validated_data["password2"] = password
        validated_data["role"] = "student"
        if(not Account.objects.filter(username=validated_data["username"]).exists()):
            if(not Account.objects.filter(email=validated_data["email"]).exists()):
                account_serializer = RegistrationSerializer(data=validated_data)
                if account_serializer.is_valid():
                    account = account_serializer.save()
                    student = Student.objects.create(
                        account = account,
                        auto_id = get_auto_id(Student),
                    )
                    # from_email = "mail.osperb@gmail.com"
                    to_email = account.email
                    subject = "Student Registration Completed"
                    html_context = {
                        "title":"Student Registration Completed",
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
                raise serializers.ValidationError({'error_message': 'Email already exists !'})
        else:
            if(not Account.objects.filter(email=validated_data["email"]).exists()):
                raise serializers.ValidationError({'error_message': 'Username already exists !'})
            else:
                raise serializers.ValidationError({'error_message': 'Username and Email already exists !'})

        return student

    def update(self, instance, validated_data):
        try:
            username = validated_data["username"]
            email = validated_data["email"]
        except:
            username = ""
            email = ""
            
        if((not Account.objects.filter(username=username).exists()) or Account.objects.filter(pk = instance.account.pk ,username=username).exists()):
            if((not Account.objects.filter(email=email).exists()) or Account.objects.filter(pk = instance.account.pk ,email=email).exists()):
                account = Account.objects.get(pk=instance.account.pk)
                account.full_name = validated_data.get('full_name', account.full_name)

                account.username = validated_data.get('username', account.full_name)
                account.email = validated_data.get('email', account.full_name)
                account.phone = validated_data.get('phone', account.phone)
                account.save()
                return instance
            else:
                raise serializers.ValidationError({'error_message': 'Email Username already exists !'})
        else:
            if((not Account.objects.filter(email=validated_data["email"]).exists()) or Account.objects.filter(pk = instance.account.pk ,email=validated_data["email"]).exists()):
                raise serializers.ValidationError({'error_message': 'Username already exists !'})
            else:
                raise serializers.ValidationError({'error_message': 'Email and Username already exists !'})



   

# class AdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = ['id','full_name','username','email','phone',]

#     def create(self, validated_data):
#         password = password_generater(8)
#         validated_data["password"] = password
#         validated_data["password2"] = password
#         validated_data["role"] = "admin"
#         if(not Account.objects.filter(username=validated_data["username"]).exists()):
#             if(not Account.objects.filter(email=validated_data["email"]).exists()):
#                 account_serializer = RegistrationSerializer(data=validated_data)
#                 if account_serializer.is_valid():
#                     account = account_serializer.save()
#                     # from_email = "mail.osperb@gmail.com"
#                     to_email = account.email
#                     subject = "admin Registration Completed"
#                     html_context = {
#                         "title":"admin Registration Completed",
#                         "data":[
#                             {
#                                 "label":"username",
#                                 "value":account.username
#                             },
#                             {
#                                 "label":"First Name",
#                                 "value":account.full_name
#                             },
#                             {
#                                 "label":"email",
#                                 "value":account.email
#                             },
#                             {
#                                 "label":"phone",
#                                 "value":account.phone
#                             },
#                             {
#                                 "label":"password",
#                                 "value":password
#                             }
#                         ]
#                     }
#                     text_content = str(html_context)
#                     send_common_mail(html_context,to_email,subject)
#             else:
#                 raise serializers.ValidationError({'email': 'Email already exists !'})
#         else:
#             if(not Account.objects.filter(email=validated_data["email"]).exists()):
#                 raise serializers.ValidationError({'username': 'Username already exists !'})
#             else:
#                 raise serializers.ValidationError({'error_message': 'Username and Email already exists !'})
#         return account

#     def update(self, instance, validated_data):
#         instance.save()

#         try:
#             username = validated_data["username"]
#             email = validated_data["email"]
#         except:
#             username = ""
#             email = ""
#         if((not Account.objects.filter(username=username).exists()) or
#             Account.objects.filter(pk = instance.pk ,username=username).exists()):
#                 if((not Account.objects.filter(email=email).exists()) or Account.objects.filter(pk = instance.pk ,email=email).exists()):



#                     account = Account.objects.get(pk=instance.pk)
#                     account.full_name = validated_data.get('full_name', account.full_name)
#                     account.username = validated_data.get('username', account.full_name)
#                     account.email = validated_data.get('email', account.full_name)
#                     account.phone = validated_data.get('phone', account.phone)
#                     account.save()
            
#                     return account
#                 else:
#                     raise serializers.ValidationError({'error_message': 'Email Username already exists !'})
#         else:
#             if((not Account.objects.filter(email=validated_data["email"]).exists()) or Account.objects.filter(pk = instance.account.pk ,email=validated_data["email"]).exists()):
#                 raise serializers.ValidationError({'error_message': 'Username already exists !'})
#             else:
#                 raise serializers.ValidationError({'error_message': 'Email and Username already exists !'})
        
    
  

