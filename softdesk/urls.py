"""softdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework_nested import routers
from django.contrib import admin
from django.urls import path, include
from users.views import SignupView
from project.views import ProjectView, ContributorView, IssueView, CommentView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register(r"projects", ProjectView, basename="projects")


contributor_router = routers.NestedSimpleRouter(router, r"projects", lookup="projects")
contributor_router.register(r"users", ContributorView, basename="users")

issues_router = routers.NestedSimpleRouter(router, r"projects", lookup="projects")
issues_router.register(r"issues", IssueView, basename="issues")

comments_router = routers.NestedSimpleRouter(issues_router, r"issues", lookup="issues")
comments_router.register(r"comments", CommentView, basename="comments")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("", include(router.urls)),
    path("", include(contributor_router.urls)),
    path("", include(issues_router.urls)),
    path("", include(comments_router.urls)),

]
