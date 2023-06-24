from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    ROLES = (
        ('learner', 'زبان آموز'),
        ('teacher', 'مربی'),
    )

    name = models.CharField(max_length=31)
    role = models.CharField(max_length=20, choices=ROLES)
    # Adding related_name to resolve clashes
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    def __str__(self):
        return self.username
