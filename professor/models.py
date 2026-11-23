from django.db import models

# Create your models here.
class Professor(models.Model):
    cpf = models.CharField(max_length=11, unique=True, primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    siape = models.CharField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome