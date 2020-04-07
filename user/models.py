from django.db import models
from django.contrib.auth.models import AbstractUser

class DnDUser(AbstractUser):
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.username