from urllib import response
from django.shortcuts import get_object_or_404, render
# from main.permissions import IsUser
from student.serializers import SpecializationSerializer, StudentNoteSerializer, StudentSerializer,UpdateStudentSerializer,JobApplicationSerializer
from .models import *
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from  rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from main.functions import get_auto_id







# Create your views here.


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.filter(is_deleted = False)
    filter_backends = [SearchFilter]
    search_fields = ['account__username']
    permission_classes = [IsAuthenticated]


    def update(self, request, pk=None):
        instance = self.get_object()
        account_data = request.data['account']

        if(request.user.is_admin or (instance.account == request.user)):

            if((not Account.objects.filter(username=account_data["username"]).exists()) or Account.objects.filter(pk = instance.account.pk ,username=account_data["username"]).exists()):
                if((not Account.objects.filter(email=account_data["email"]).exists()) or Account.objects.filter(pk = instance.account.pk ,email=account_data["email"]).exists()):
                    account = Account.objects.get(pk=instance.account.pk)
                    account.full_name = account_data.get('full_name', account.full_name)
                    account.username = account_data.get('username', account.full_name)
                    account.email = account_data.get('email', account.full_name)
                    account.phone = account_data.get('phone', account.phone)
                    account.save()

            if(not request.user.is_admin):
                request.data["fees_paid"] = instance.fees_paid 

            serializer = UpdateStudentSerializer(instance=instance,data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                Specialization.objects.filter(student=instance).delete()
                for item in request.data['specializations']:
                    item["student"] = instance
                    Specialization.objects.create(
                         auto_id = get_auto_id(Specialization),
                         **item
                    )
        instance = Student.objects.get(pk=instance.pk)
        data = StudentSerializer(instance=instance).data
        return Response(data,status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, pk=None, **kwargs ):
        # try:
            user = self.request.user
            instance = self.get_object()
            if(user.is_admin or (instance.student.account == user)):
                Account.objects.filter(id=instance.account.id).delete()
                data = {"response":"Successfully deleted"}
            else:
                data = {"response":"Access denied"}

            return Response(data,status=status.HTTP_204_NO_CONTENT)

    
    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.get(pk=pk)
        serializer = StudentSerializer(queryset, context={'request': self.request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class SpecializationViewSet(ModelViewSet):
   
    queryset = Specialization.objects.all() 
    serializer_class = SpecializationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['student__user__username','student__user__first_name','student__user__last_name']

    def destroy(self, request, *args, **kwargs):
        try:
            user = self.request.user
            instance = self.get_object()
            if(user.is_admin or (instance.student.account == user)):
                instance.delete()
                data = {"response":"Successfully deleted"}
            else:
                data = {"response":"Access denied"}        
            return Response(data,status=status.HTTP_200_OK)
        except:
            data = {"Not found !"}
            return Response(data,status=status.HTTP_403_FORBIDDEN)  

class JobApplicationViewSet(ModelViewSet):
    serializer_class = JobApplicationSerializer
    queryset = JobApplication.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter]
    search_fields = ['student__user__username','student__user__first_name','student__user__last_name']
    


class StudentNoteViewSet(ModelViewSet):
    serializer_class = StudentNoteSerializer
    queryset = StudentNote.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter]
    search_fields = ['title']
    

