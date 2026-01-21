# from django.contrib.auth.models import AbstractUser
# from django.db import models

# # class User(AbstractUser):
# #     # Add custom fields here
# #     phone = models.CharField(max_length=20, blank=True, null=True)
# #     role = models.CharField(max_length=50, blank=True, null=True)

# #     # Avoid clashes with auth.User
# #     groups = models.ManyToManyField(
# #         'auth.Group',
# #         related_name='accounts_user_set',  # 🔑 change related_name
# #         blank=True,
# #         help_text='The groups this user belongs to.'
# #     )
# #     user_permissions = models.ManyToManyField(
# #         'auth.Permission',
# #         related_name='accounts_user_permissions_set',  # 🔑 change related_name
# #         blank=True,
# #         help_text='Specific permissions for this user.'
# #     )

# #     def __str__(self):
# #         return self.username
# class User(AbstractUser):
#     ROLE_CHOICES = (
#         ("INTERN", "Intern"),
#         ("SUPERVISOR", "Supervisor"),
#     )

#     role = models.CharField(
#         max_length=20,
#         choices=ROLE_CHOICES,
#         default="INTERN",   # ✅ IMPORTANT
#     )
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Supervisor', 'Supervisor'),
        ('Intern', 'Intern'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True)
