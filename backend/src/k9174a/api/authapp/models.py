from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    title = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.title


# class UserProfile(AbstractUser):
#     role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
