from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
class CustomUser(AbstractUser):
    email=models.EmailField(_('email address'),unique=True)
    username=models.CharField(max_length=50)
    interest=models.TextField(max_length=200,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS=['username']
    USERNAME_FIELD='email'
    objects=CustomUserManager()

    def __str__(self):
        return self.username
