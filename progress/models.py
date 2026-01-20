from django.db import models
from accounts.models import User
from projects.models import Project

class Progress(models.Model):
    intern = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)