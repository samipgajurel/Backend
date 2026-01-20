from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.permission import IsIntern, IsSupervisor
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceViewSet(ModelViewSet):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'intern':
            return Attendance.objects.filter(intern=user)
        if user.role == 'supervisor':
            return Attendance.objects.all()
        return Attendance.objects.none()

    def perform_create(self, serializer):
        serializer.save(marked_by=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsSupervisor()]
        if self.request.method == 'GET':
            return [IsIntern() | IsSupervisor()]
        return super().get_permissions()
