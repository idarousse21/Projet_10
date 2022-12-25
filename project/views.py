from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Project, Contributor, Issue, Comment
from .serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
)
from .permissions import (
    ProjectPermission,
    ContributorAndIssuePermissions,
    CommentPermission,
)
from django.db.models import Q


class ProjectView(ModelViewSet):
    permission_classes = [IsAuthenticated & ProjectPermission]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        projects = Project.objects.filter(
            Q(contributor__user=self.request.user) | Q(author=self.request.user)
        )
        return projects


class ContributorView(ModelViewSet):
    permission_classes = [IsAuthenticated, ContributorAndIssuePermissions]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        contributors = Contributor.objects.filter(project=self.kwargs["projects_pk"])
        return contributors


class IssueView(ModelViewSet):
    permission_classes = [IsAuthenticated, ContributorAndIssuePermissions]
    serializer_class = IssueSerializer

    def get_queryset(self):
        issues = Issue.objects.filter(project=self.kwargs["projects_pk"])
        return issues


class CommentView(ModelViewSet):
    permission_classes = [IsAuthenticated, CommentPermission]
    serializer_class = CommentSerializer

    def get_queryset(self):
        comments = Comment.objects.filter(issue=self.kwargs["issues_pk"])
        return comments
