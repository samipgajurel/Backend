from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.permission import IsIntern, IsSupervisor
from .models import Completion
from .serializers import CompletionSerializer

class CompletionViewSet(ModelViewSet):
    queryset = Completion.objects.all()
    serializer_class = CompletionSerializer
    permission_classes = [IsAuthenticated, IsSupervisor]
