# Generated by Django 4.1.4 on 2022-12-19 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("project", "0002_rename_contibutor_contributor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="contributor",
            name="role",
            field=models.CharField(
                choices=[("1", "Contributeur"), ("2", "Auteur")], max_length=25
            ),
        ),
        migrations.AlterField(
            model_name="issue",
            name="assignee",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="assignee",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="issue",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="issue",
            name="description",
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name="issue",
            name="priority",
            field=models.CharField(
                choices=[("1", "Faible"), ("2", "Moyenne"), ("3", "Élevée")],
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="issue",
            name="status",
            field=models.CharField(
                choices=[("1", "A faire"), ("2", "En cours"), ("3", "Fini")],
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="issue",
            name="tag",
            field=models.CharField(
                choices=[("1", "Bug"), ("2", "Amélioration"), ("3", "Tâche")],
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name="project",
            name="type",
            field=models.CharField(
                choices=[
                    ("1", "Back-End"),
                    ("2", "Front-End"),
                    ("3", "Ios"),
                    ("4", "Android"),
                ],
                max_length=25,
            ),
        ),
    ]
