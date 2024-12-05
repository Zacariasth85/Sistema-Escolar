from django.db import models

class Classe(models.Model):
    Classe_CHOICES = [
        (7, '7º Classe'),
        (8, '8º Classe'),
        (9, '9º Classe'),
        (10, '10º Classe'),
        (11, '11º Classe'),
        (12, '12º Classe'),
        # Pode se adicionar mais classes.
    ]
    
    numero = models.IntegerField(choices=Classe_CHOICES, unique=True)
    
    def __str__(self):
        return f"{self.get_numero_display()}"
        