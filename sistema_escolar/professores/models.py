from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    numero = models.IntegerField()
    email = models.EmailField()
    area_de_atuacao = models.CharField(max_length=100)
    tempo_de_experiencia = models.IntegerField()