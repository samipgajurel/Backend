from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Intern
from .serializers import InternSerializer


class InternListCreateView(generics.ListCreateAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    permission_classes = [permissions.IsAuthenticated]

class AttendanceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Attendance endpoint working"
        })

class AnalyticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Analytics endpoint working"
        })
