from django.db import models
from django.contrib.auth.models import AbstractUser

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Users(AbstractUser):
    curso = models.ForeignKey(Curso, null= True, on_delete= models.DO_NOTHING)
    nome = models.CharField(max_length=200)



