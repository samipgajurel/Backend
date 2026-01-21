from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.permission import IsIntern, IsSupervisor

from .models import Progress
from .serializers import ProgressSerializer

class ProgressViewSet(ModelViewSet):
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'intern':
            return Progress.objects.filter(intern=user)
        return Progress.objects.all()

    def get_permissions(self):
        if self.request.method in ['GET', 'POST', 'PUT', 'PATCH']:
            return [IsIntern() | IsSupervisor()]
        return super().get_permissions()
