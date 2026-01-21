from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.permission import IsIntern, IsSupervisor
from .models import Attendance
from .serializers import AttendanceSerializer


class AttendanceViewSet(ModelViewSet):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == "intern":
            return Attendance.objects.filter(intern=user)
        if user.role == "supervisor":
            return Attendance.objects.all()
        return Attendance.objects.none()

    def perform_create(self, serializer):
        serializer.save(marked_by=self.request.user)

    def get_permissions(self):
        """
        POST -> Supervisor only
        GET  -> Intern OR Supervisor
        Others -> default authenticated
        """
        if self.request.method == "POST":
            return [IsAuthenticated(), IsSupervisor()]

        if self.request.method == "GET":
            # ✅ IMPORTANT: we cannot do IsIntern() | IsSupervisor()
            # So we allow authenticated and then manually check in permission list:
            return [IsAuthenticated(), IsInternOrSupervisor()]

        return [IsAuthenticated()]


class IsInternOrSupervisor(IsAuthenticated):
    """
    Custom permission: allows both intern and supervisor.
    """

    def has_permission(self, request, view):
        user = request.user
        return bool(
            user
            and user.is_authenticated
            and getattr(user, "role", None) in ["intern", "supervisor", "INTERN", "SUPERVISOR", "Intern", "Supervisor"]
        )
