from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(
        max_length= 150,
        validators=[UnicodeUsernameValidator, ],
        unique= True
    )
    email = models.EmailField(
        max_length= 150,
        unique= True
    )
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    
    class Meta:
        ordering =['-date_joined']


class Message(models.Model):
    name = models.CharField(
        max_length=150
    )
    email = models.EmailField(
        max_length=150
    )
    message = models.TextField(
        max_length= 150
    ) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
       