from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompletionViewSet

router = DefaultRouter()
router.register(r'completion', CompletionViewSet, basename='completion')

urlpatterns = [
    path('', include(router.urls)),
]
