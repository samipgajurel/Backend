from rest_framework.permissions import BasePermission

class IsSupervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
class IsIntern(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'intern')