from urllib import response
from django.shortcuts import get_object_or_404, render
# from main.permissions import IsUser
from student.serializers import SpecializationSerializer, StudentSerializer
from .models import *
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from  rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated







# Create your views here.


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['account__username']

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.account.id
            Account.objects.filter(id=id).update(is_active = False)
            instance.is_deleted = True
            instance.save()
            data = {"response":"Successfully deleted"}
            return Response(data,status=status.HTTP_204_NO_CONTENT)
        except:
                data = {"Access Denied !"}
                return Response(data,status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.get(pk=pk)
        serializer = StudentSerializer(queryset, context={'request': self.request})
        return Response(serializer.data, status=status.HTTP_200_OK)

#  ========================================

class SpecializationViewSet(ModelViewSet):
   
    queryset = Specialization.objects.all() 
    serializer_class = SpecializationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['student__user__username','student__user__first_name','student__user__last_name']

# ============================================

# class AdminViewSet(ModelViewSet):

#     queryset = Account.objects.filter(role ='admin',is_active = True)
#     serializer_class = AdminSerializer
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         # self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)
#         data = {}
#         if serializer.is_valid(): 

#             serializer.save()
#             data = serializer.data
#             return Response(data=data)
#         else:
#             data = serializer.errors
#             data['response'] = 'Error'
#             data['error_message'] = 'Data Not Valid'
#         return Response(data = data, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, *args, **kwargs):
#         # self.object = self.get_object()
#         serializer = self.get_serializer(self.get_object(),data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             data = serializer.data
#             return Response(data=data)
#         else:
#             data = serializer.errors
#             data['response'] = 'Error'
#             data['error_message'] = 'Data Not Valid'
#         return Response(data = data, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         id = instance.id
#         Account.objects.filter(id=id).update(is_active = False)
#         data = {"response":"Successfully deleted"}
#         return Response(data,status=status.HTTP_204_NO_CONTENT)
