"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from interns.views import InternViewSet, AttendanceView, AnalyticsView

router = DefaultRouter()
router.register(r"interns", InternViewSet, basename="intern")

urlpatterns = [
    path("admin/", admin.site.urls),

    # JWT Auth (SimpleJWT default)
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Custom auth endpoints (your accounts app)
    path("api/accounts/", include("accounts.urls")),

    # Router endpoints
    path("api/", include(router.urls)),  # /api/interns/

    # App routers (these were missing)
    path("api/attendance/", include("attendance.urls")),  # /api/attendance/attendance/
    path("api/projects/", include("projects.urls")),      # /api/projects/projects/
    path("api/progress/", include("progress.urls")),      # /api/progress/progress/
    path("api/tasks/", include("tasks.urls")),            # /api/tasks/tasks/
    path("api/feedback/", include("feedback.urls")),      # /api/feedback/feedback/

    # Reports endpoints (renamed to avoid conflict)
    path("api/reports/attendance/", AttendanceView.as_view(), name="attendance_report"),
    path("api/reports/analytics/", AnalyticsView.as_view(), name="analytics_report"),
]

