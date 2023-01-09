from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
from project.models import Project, Contributor, Issue, Comment


METHOD_FIELDS = SerializerMethodField


class Mixin:
    def save(self, **kwargs):
        object = super().save(**kwargs)
        object.author = self.context["user"]
        object.save()
        return object


class DisplayString:
    def get_user(self, obj):
        return obj.user.username

    def get_type(self, obj):
        return obj.get_type_display()

    def get_role(self, obj):
        return obj.get_role_display()

    def get_tag(self, obj):
        return obj.get_tag_display()

    def get_priority(self, obj):
        return obj.get_priority_display()

    def get_status(self, obj):
        return obj.get_status_display()

    def get_assignee(self, obj):
        return obj.assignee.username


class ContributorSerializer(DisplayString, ModelSerializer):
    role = METHOD_FIELDS()
    user = METHOD_FIELDS()

    class Meta:
        model = Contributor
        fields = ["id", "user", "project", "role"]


class ContributorPostSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["user", "role"]


class ProjectSerializer(DisplayString, ModelSerializer):
    type = METHOD_FIELDS()

    class Meta:
        model = Project
        fields = ["id", "title", "description", "type", "author"]


class ProjectPostSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ["title", "description", "type"]

    def save(self, **kwargs):
        project = super().save(**kwargs)
        project.author = self.context["user"]
        project.save()
        Contributor.objects.update_or_create(
            project=project, user=self.context["user"], role="2"
        )
        return project


class IssueSerializer(DisplayString, ModelSerializer):
    tag = METHOD_FIELDS()
    priority = METHOD_FIELDS()
    status = METHOD_FIELDS()
    assignee = METHOD_FIELDS()

    class Meta:
        model = Issue
        fields = "__all__"


class IssuePostSerializer(Mixin, ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "title",
            "description",
            "tag",
            "priority",
            "status",
            "assignee",
        ]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentPostSerializer(Mixin, ModelSerializer):
    class Meta:
        model = Comment
        fields = ["description"]
