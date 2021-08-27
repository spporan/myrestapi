from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.db.models import query
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
# Create your models here.

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permissiona_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_classs = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
