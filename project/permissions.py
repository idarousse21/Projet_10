from rest_framework.permissions import BasePermission
from .models import Contributor, Project
from django.shortcuts import get_object_or_404


class ContributorAndIssuePermissions(BasePermission):
    def has_permission(self, request, view):
        project = get_object_or_404(Project, id=view.kwargs["projects_pk"])
        return (
            Contributor.objects.filter(project=project, user=request.user).exists()
            or project.author == request.user
        )

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return (
                Contributor.objects.filter(
                    project=obj.project, user=request.user
                ).exists()
                or obj.project.author == request.user
            )
        return obj.author == request.user


class ProjectPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return (
                Contributor.objects.filter(project=obj, user=request.user).exists()
                or obj.author == request.user
            )

        return obj.author == request.user


class CommentPermission(BasePermission):
    def has_permission(self, request, view):
        project = get_object_or_404(Project, id=view.kwargs["projects_pk"])
        return (
            Contributor.objects.filter(project=project, user=request.user).exists()
            or project.author == request.user
        )

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return (
                Contributor.objects.filter(
                    project=obj.issue.project, user=request.user
                ).exists()
                or obj.issue.project.author == request.user
            )
        return obj.author == request.user
