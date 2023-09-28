from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

def validate_matriulation(value):
    if not value.isdigit():
        raise ValidationError('A matricula deve conter apenas números')
    
class Users(AbstractUser):
    curso = models.CharField(max_length=100)
    nome = models.CharField(max_length=200)
