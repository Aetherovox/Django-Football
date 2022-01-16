from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework import permissions,status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .api import CustomObtainTokenPairSerializer,CustomUserSerializer

@api_view(['GET'])
def current_user(request):
    """Determine Current User and return their data"""
    serializer = CustomUserSerializer(request.user)
    return Response(serializer.data)




class CustomObtainTokenPair(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomObtainTokenPairSerializer


class UserCreationView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self,request,format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)