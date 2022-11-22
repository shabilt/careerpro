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
    queryset = Student.objects.filter(is_deleted = False)
    filter_backends = [SearchFilter]
    search_fields = ['account__username']

    def destroy(self, request, *args, pk=None, **kwargs ):
        # try:
            instance = self.get_object()
            id = instance.id
            student = Student.objects.get(id=id)
            Student.objects.filter(id=id).update(is_deleted = True)
            Account.objects.filter(id=student.account.id).update(is_active=True)
            # instance.is_deleted = True
            # instance.save()
            # Student.objects.filter(id=id).update(is_deleted = True)
            data = {"response":"Successfully deleted"}
            return Response(data,status=status.HTTP_204_NO_CONTENT)
        # except:
        #         data = {"Access Denied !"}
        #         return Response(data,status=status.HTTP_204_NO_CONTENT)

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

    def destroy(self, request, *args, **kwargs):
        try:
            user = self.request.user
            instance = self.get_object()
            id = instance.id
            Specialization.objects.filter(id=id).update(is_deleted = True)
            data = {"response":"Successfully deleted"}
            return Response(data,status=status.HTTP_200_OK)

        except:
                data = {"Access Denied !"}
                return Response(data,status=status.HTTP_403_FORBIDDEN)  

# ============================================

