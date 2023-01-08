from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Project, Contributor, Issue, Comment
from .serializers import (
    ProjectPostSerializer,
    ProjectSerializer,
    ContributorSerializer,
    ContributorPostSerializer,
    IssueSerializer,
    IssuePostSerializer,
    CommentSerializer,
    CommentPostSerializer,
)
from .permissions import (
    ProjectPermission,
    IssuePermissions,
    CommentPermission,
    ContributorPermissions,
)
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import User


METHOD_POST_PUT = ["POST", "PUT", "PATCH"]


class MyMixinSaveAuthor:
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context


class ProjectView(MyMixinSaveAuthor, ModelViewSet):
    permission_classes = [IsAuthenticated, ProjectPermission]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        projects = Project.objects.filter(
            Q(contributor__user=self.request.user) | Q(author=self.request.user)
        ).distinct()
        return projects

    def get_serializer_class(self):
        if self.request.method in METHOD_POST_PUT:
            return ProjectPostSerializer
        else:
            return ProjectSerializer

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)


class ContributorView(ModelViewSet):
    permission_classes = [IsAuthenticated, ContributorPermissions]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        contributors = Contributor.objects.filter(
            project=self.kwargs["projects_pk"])
        return contributors

    def get_serializer_class(self):

        if self.request.method in METHOD_POST_PUT:
            return ContributorPostSerializer
        else:
            return ContributorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = get_object_or_404(Project, pk=kwargs["projects_pk"])
        if not Contributor.objects.filter(
            user=request.data["user"], project=kwargs["projects_pk"]
        ).exists():
            user = get_object_or_404(User, pk=request.data["user"])
            serializer.save(user=user, project=project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            message = f"L'ID de l'utilisateur {request.data['user']} est déjâ lié au project ID {kwargs['projects_pk']}"
            return Response({"message": message},
                            status=status.HTTP_400_BAD_REQUEST)


class IssueView(MyMixinSaveAuthor, ModelViewSet):
    permission_classes = [IsAuthenticated, IssuePermissions]
    serializer_class = IssueSerializer

    def get_queryset(self):
        issues = Issue.objects.filter(project=self.kwargs["projects_pk"])
        return issues

    def get_serializer_class(self):
        if self.request.method in METHOD_POST_PUT:
            return IssuePostSerializer
        else:
            return IssueSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            project = get_object_or_404(Project, pk=kwargs["projects_pk"])
            project_id = kwargs["projects_pk"]
            if "assignee" not in serializer.validated_data:
                serializer.save(assignee=request.user, project=project)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED)
            elif not Contributor.objects.filter(
                user=request.data["assignee"], project=project
            ).exists():
                message = f"L'ID de l'utilisateur {request.data['assignee']} ne fait pas parti des contributeur du project ID {project_id}"
                return Response(
                    {"message": message}, status=status.HTTP_400_BAD_REQUEST
                )
            else:
                serializer.save(project=project)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs["pk"])
        serializer = self.get_serializer(
            issue, data=request.data, partial=True)
        project = get_object_or_404(Project, pk=kwargs["projects_pk"])
        project_id = kwargs["projects_pk"]
        if serializer.is_valid(raise_exception=True):
            if "assignee" not in serializer.validated_data:
                serializer.save(project=project)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif not Contributor.objects.filter(
                user=request.data["assignee"], project=project
            ).exists():
                message = f"L'ID de l'utilisateur {request.data['assignee']} ne fait pas parti des contributeur du project ID {project_id}"
                return Response(
                    {"message": message}, status=status.HTTP_400_BAD_REQUEST
                )
            else:
                serializer.save(project=project)
                return Response(serializer.data, status=status.HTTP_200_OK)


class CommentView(MyMixinSaveAuthor, ModelViewSet):
    permission_classes = [IsAuthenticated, CommentPermission]
    serializer_class = CommentPostSerializer

    def get_queryset(self):
        comments = Comment.objects.filter(issue=self.kwargs["issues_pk"])
        return comments

    def get_serializer_class(self):
        if self.request.method in METHOD_POST_PUT:
            return CommentPostSerializer
        else:
            return CommentSerializer

    def create(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs["issues_pk"])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(issue=issue)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
