# from django.conf import settings
# from django.db import models

# class Intern(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#     )

#     def __str__(self):
#         return self.user.username

# from django.db import models
# from django.utils import timezone


# class Intern(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=20, blank=True)
#     department = models.CharField(max_length=100, blank=True)

#     completed_tasks = models.PositiveIntegerField(default=0)

#     created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.name

from django.utils import timezone
from django.db import models

class Intern(models.Model):
    name = models.CharField(max_length=100, default="Unknown")
    email = models.EmailField(unique=True, default="temp@example.com")
    completed_tasks = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
