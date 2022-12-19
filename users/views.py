
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import redirect


class SignupView(CreateAPIView):
    serializer_class = UserSerializer
    

   

   
