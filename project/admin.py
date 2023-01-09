from django.contrib import admin

from .models import Project, Contributor, Issue, Comment

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title","type", "author",)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Comment)