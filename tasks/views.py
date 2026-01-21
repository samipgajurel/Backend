from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.permission import IsIntern, IsSupervisor

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Intern  -> sees only their own tasks
        Supervisor/Admin -> sees all tasks
        """
        user = self.request.user

        if user.role == "intern":
            return Task.objects.filter(assigned_to=user)

        return Task.objects.all()

    def get_permissions(self):
        """
        Permissions by role and method:

        GET        -> Intern + Supervisor
        PUT/PATCH  -> Intern (update their own task)
        POST       -> Supervisor (create task)
        DELETE     -> Supervisor (delete task)
        """
        base_permissions = [IsAuthenticated()]

        # ✅ Intern + Supervisor can VIEW tasks
        if self.request.method == "GET":
            return base_permissions + [IsIntern() | IsSupervisor()]

        # ✅ Intern can update task status
        if self.request.method in ["PUT", "PATCH"]:
            return base_permissions + [IsIntern()]

        # ✅ Supervisor can create or delete tasks
        if self.request.method in ["POST", "DELETE"]:
            return base_permissions + [IsSupervisor()]

        return base_permissions
