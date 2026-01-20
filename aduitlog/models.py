from django.db import models
from accounts.models import User

class AuditLog(models.Model):
    ACTION_CHOICES = (
        ('CREATE', 'CREATE'),
        ('UPDATE', 'UPDATE'),
        ('DELETE', 'DELETE'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=20)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    model = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} | {self.action} | {self.model}"
