from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.permission import IsIntern, IsSupervisor
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackViewSet(ModelViewSet):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'intern':
            return Feedback.objects.filter(intern=user)

        if user.role == 'supervisor':
            return Feedback.objects.all()

        return Feedback.objects.none()

    def perform_create(self, serializer):
        serializer.save(supervisor=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsSupervisor()]
        if self.request.method == 'GET':
            return [IsIntern() | IsSupervisor()]
        return super().get_permissions()
