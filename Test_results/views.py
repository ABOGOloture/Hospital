from hashlib import pbkdf2_hmac
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RenalFunctionTestsSerializer, PersonalInformationSerializer
from .models import RenalFunctionTests, PersonalInformation
from rest_framework import status, permissions

class PersonalInformation_List(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        info = PersonalInformation.objects.all()
        serializer = PersonalInformationSerializer(info, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonalInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.savez()
            return Response(serializer.data, status=status.HTTP_201_CONTENT_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


class PersonalInformation_Details(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_PersonalInformation(self, pk):

        try:
            return PersonalInformation.objects.get(pk=pk)
        except:
            raise Http404

    
    def get(self, request, pk, format=None):
        info = self.get_PersonalInformation(pk)
        serializer = PersonalInformationSerializer(info)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        info = self.get_PersonalInformation(pk)
        serializer = PersonalInformationSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        info = self.get_PersonalInformation(pk)
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
            
            



class RenalFunctionTests_List(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        Test = RenalFunctionTests.objects.all()
        serializer = RenalFunctionTestsSerializer(Test, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RenalFunctionTestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.savez()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


class RenalFunctionTests_Details(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_RenalFunctionTests(self, pk):

        try:
            return RenalFunctionTests.objects.get(pk=pk)
        except:
            raise Http404

    
    def get(self, request, pk, format=None):
        test = self.get_RenalFunctionTests(pk)
        serializer = RenalFunctionTestsSerializer(test)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        test = self.get_RenalFunctionTests(pk)
        serializer = RenalFunctionTestsSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        test = self.get_RenalFunctionTests(pk)
        test.delete()
        return Response('information deleted successfully')