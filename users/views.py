from django.shortcuts import render
from .serializers import UserSerializer
from .models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser

class MyAccountView(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    parser_classes = [MultiPartParser]

    def get_object(self, pk):
        try:
            return User.objects.filter(is_active = True).get(id = pk)
        except User.DoesNotExist:
            raise Http404

    def get(self ,request , pk = None , format = None):

        owner = self.get_object(pk)
        serialized_User = UserSerializer(owner)
        
        return Response({ "User-Info" : serialized_User.data, })
    
    def put(self, request, pk, format = None):

        owner = self.get_object(pk)
        serializer = UserSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class MyAccountDeleteView(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    parser_classes = [MultiPartParser]

    def get_object(self, pk):
        try:
            return User.objects.filter(is_active = True).get(id = pk)
        except User.DoesNotExist:
            raise Http404

    def get(self ,request , pk = None , format = None):

        owner = self.get_object(pk)
        serialized_User = UserSerializer(owner)
        return Response({ "User-Info" : serialized_User.data, })
    
    def delete(self, request, pk, format=None):
        owner = self.get_object(pk)
        owner.is_active = False
        owner.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

