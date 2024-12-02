from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    codigo = models.CharField(max_length=10, unique=True)
    
    carga_horaria = models.IntegerField()
    
    descricao = models.TextField(blank=True, null=True)
    
    AREAS_CHOICES = [
        ('CD', 'Ciências com Desenho'),
        ('AM', 'Letra'),
        ('CB', 'Ciências com Biológia'),
        ('LB', 'Letras com Biológia'),
    ]
    area = models.CharField(max_length=20, choices=AREAS_CHOICES)
    
    semestre_recomendado = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    
    optativa = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.codigo} - {self.nome}"