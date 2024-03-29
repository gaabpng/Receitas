from django.db import models

# Create your models here.

class receita(models.Model):

    DIFICULDADE_CHOICES = [
        (1, 'Fácil'),
        (2, 'Moderado'),
        (3, 'Intermediário'),
        (4, 'Difícil'),
        (5, 'Muito difícil'),
    ]

    nome = models.CharField(max_length = 100)
    ingredientes = models.TextField()
    tempo = models.IntegerField()
    dificuldade = models.IntegerField(choices=DIFICULDADE_CHOICES)
    instrucoes = models.TextField(default = '')

    def __str__(self):
        return self.nome
    
class users(models.Model):
    email = models.CharField(max_length = 300)
    user = models.CharField(max_length = 100)
    senha = models.CharField(max_length = 100)