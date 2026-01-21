from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import InternViewSet, AttendanceView, AnalyticsView

router = DefaultRouter()
router.register(r"interns", InternViewSet, basename="interns")

urlpatterns = [
    # CRUD for Intern model (if you include this under /api/ this becomes /api/interns/interns/)
    path("", include(router.urls)),

    # Optional report endpoints inside interns app
    path("reports/attendance/", AttendanceView.as_view(), name="interns-attendance-report"),
    path("reports/analytics/", AnalyticsView.as_view(), name="interns-analytics-report"),
]
