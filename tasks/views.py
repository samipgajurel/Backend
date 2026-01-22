from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.permission import IsInternOrSupervisor, IsIntern, IsSupervisor

from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'intern':
            return Task.objects.filter(assigned_to=user)
        if user.role == 'supervisor':
            return Task.objects.all()
        return Task.objects.none()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated(), IsInternOrSupervisor()]
        if self.request.method in ['PUT', 'PATCH']:
            return [IsAuthenticated(), IsIntern()]
        if self.request.method in ['POST', 'DELETE']:
            return [IsAuthenticated(), IsSupervisor()]
        return [IsAuthenticated()]
