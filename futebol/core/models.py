from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.nome