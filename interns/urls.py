from django.urls import path
from .views import (
    InternListCreateView,
    AttendanceView,
    AnalyticsView,
)

urlpatterns = [
    path("interns/", InternListCreateView.as_view(), name="intern-list"),
    path("attendance/", AttendanceView.as_view(), name="attendance"),
    path("analytics/", AnalyticsView.as_view(), name="analytics"),
]
