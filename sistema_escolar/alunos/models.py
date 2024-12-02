from django.db import models

class Aluno(models.Model):
    # Campos do modelo
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)