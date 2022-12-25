from django.db import models
from django.conf import settings


CHOICES_TYPES = [
    ("1", "Back-End"),
    ("2", "Front-End"),
    ("3", "Ios"),
    ("4", "Android"),
]

CHOICES_PERMISSION = [
    ("1", "Contributeur"),
    ("2", "Auteur"),
]

CHOICES_PRIORITY = [
    ("1", "Faible"),
    ("2", "Moyenne"),
    ("3", "Élevée"),
]

CHOICES_TAG = [
    ("1", "Bug"),
    ("2", "Amélioration"),
    ("3", "Tâche"),
]

CHOICES_STATUS = [
    ("1", "A faire"),
    ("2", "En cours"),
    ("3", "Fini"),
]


class Project(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(
        max_length=5000,
    )
    type = models.CharField(max_length=25, choices=CHOICES_TYPES)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=25, choices=CHOICES_PERMISSION)


class Issue(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=25)
    description = models.CharField(
        max_length=5000,
    )
    tag = models.CharField(max_length=25, choices=CHOICES_TAG)
    priority = models.CharField(max_length=25, choices=CHOICES_PRIORITY)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=CHOICES_STATUS)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="author",
    )
    assignee = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assignee",
    )


class Comment(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
