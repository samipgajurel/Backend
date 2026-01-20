from django.db import models
from accounts.models import User

class Completion(models.Model):
    intern = models.OneToOneField(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    certificate_generated = models.BooleanField(default=False)