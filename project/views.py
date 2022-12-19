from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.shortcuts import redirect
from django.conf import settings
from .models import Project, Contributor, Issue, Comment
from .serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


    

class ContributorView(ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

    

class IssueView(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
