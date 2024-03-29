# Generated by Django 4.1.4 on 2023-01-04 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("project", "0004_alter_issue_assignee"),
    ]

    operations = [
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
    ]
