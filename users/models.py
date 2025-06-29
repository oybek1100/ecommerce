from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True)
    

    def __str__(self):
        return self.username
