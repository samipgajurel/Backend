from django.utils.deprecation import MiddlewareMixin
from auditlog.models import AuditLog

class AuditLogMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        request._audit_action = None
        if request.method == 'POST':
            request._audit_action = 'CREATE'
        elif request.method in ['PUT', 'PATCH']:
            request._audit_action = 'UPDATE'
        elif request.method == 'DELETE':
            request._audit_action = 'DELETE'

    def process_response(self, request, response):
        if (
            hasattr(request, '_audit_action') and
            request._audit_action and
            request.user.is_authenticated and
            response.status_code < 400
        ):
            AuditLog.objects.create(
                user=request.user,
                role=request.user.role,
                action=request._audit_action,
                model=request.resolver_match.app_name
            )
        return response
