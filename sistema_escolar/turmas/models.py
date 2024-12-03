from django.db import models
from classe.models import Classe
from disciplinas.models import Disciplina

class Turma(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return f"{self.nome} - {self.classe}"
