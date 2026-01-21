# from rest_framework import generics, permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response

# from .models import Intern
# from .serializers import InternSerializer


# class InternListCreateView(generics.ListCreateAPIView):
#     queryset = Intern.objects.all()
#     serializer_class = InternSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class AttendanceView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         return Response({
#             "message": "Attendance endpoint working"
#         })

# class AnalyticsView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         return Response({
#             "message": "Analytics endpoint working"
#         })

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Intern
from .serializers import InternSerializer
from attendance.models import Attendance
from progress.models import Progress


class InternViewSet(viewsets.ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    permission_classes = [IsAuthenticated]


class AttendanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Attendance.objects.values(
            "intern__name", "date", "status"
        )
        return Response(data)


class AnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = []

        interns = Intern.objects.all()
        for intern in interns:
            attendance_count = Attendance.objects.filter(
                intern=intern, status="present"
            ).count()

            total_days = Attendance.objects.filter(
                intern=intern
            ).count()

            attendance_percent = (
                (attendance_count / total_days) * 100
                if total_days > 0 else 0
            )

            progress = Progress.objects.filter(
                intern=intern
            ).last()

            data.append({
                "intern": intern.name,
                "attendance": round(attendance_percent, 2),
                "progress": progress.status if progress else "Not Started",
                "completed_tasks": intern.completed_tasks
            })

        return Response(data)
