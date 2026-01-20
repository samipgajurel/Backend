from django.db import models
from accounts.models import User

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supervised_projects')
    start_date = models.DateField()
    end_date = models.DateField()