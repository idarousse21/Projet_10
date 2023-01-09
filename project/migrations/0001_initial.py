# Generated by Django 4.1.4 on 2022-12-13 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=25)),
                ("description", models.CharField(blank=True, max_length=5000)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Back-End", "Back-End"),
                            ("Front-End", "Front-End"),
                            ("Ios", "Ios"),
                            ("Android", "Android"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Issue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=25)),
                ("description", models.CharField(blank=True, max_length=5000)),
                (
                    "tag",
                    models.CharField(
                        choices=[
                            ("Bug", "Bug"),
                            ("Amélioration", "Amélioration"),
                            ("Tâche", "Tâche"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("Faible", "Faible"),
                            ("Moyenne", "Moyenne"),
                            ("Élevée", "Élevée"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("A faire", "A faire"),
                            ("En cours", "En cours"),
                            ("Fini", "Fini"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "assignee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assignee",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="auteur",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project.project",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contibutor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("Contributeur", "Contributeur"),
                            ("Autheur", "Autheur"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project.project",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("description", models.CharField(max_length=500)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "issue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="project.issue"
                    ),
                ),
            ],
        ),
    ]