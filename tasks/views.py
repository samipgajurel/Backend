from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.permission import IsIntern, IsSupervisor

from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'intern':
            return Task.objects.filter(assigned_to=user)
        return Task.objects.all()

    def get_permissions(self):
        if self.request.method in ['GET', 'PUT', 'PATCH']:
            return [IsIntern()]
        if self.request.method in ['POST', 'DELETE']:
            return [IsSupervisor()]
        return super().get_permissions()
