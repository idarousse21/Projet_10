from rest_framework.serializers import ModelSerializer
from .models import Project, Contributor, Issue, Comment
from django.contrib.auth.models import User
from users.serializers import UserSerializer

class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["id", "project", "user", "role"]
    


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description", "type", "author"]


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "project",
            "status",
            "author",
            "assignee",
            "created_time",
        ]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "description", "author", "issue", "created_time"]
