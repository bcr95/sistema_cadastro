from django.db import models

class Agendamento(models.Model):
    nome = models.CharField(max_length=100)
    data_e_hora_agendamento = models.DateTimeField()
    telefone = models.CharField(max_length=15)
    diagnostico = models.TextField()

    def __str__(self):
        return self.nome
