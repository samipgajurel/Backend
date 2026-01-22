from rest_framework.permissions import BasePermission

class IsIntern(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'intern'

class IsSupervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'supervisor'
    
    from rest_framework.permissions import BasePermission

class IsIntern(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and getattr(request.user, "role", None) == "intern")

class IsSupervisor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and getattr(request.user, "role", None) == "supervisor")

class IsInternOrSupervisor(BasePermission):
    def has_permission(self, request, view):
        role = getattr(request.user, "role", None)
        return bool(request.user and request.user.is_authenticated and role in ["intern", "supervisor"])
