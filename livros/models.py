from django.db import models
from datetime import date
# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
        
    def __str__(self) -> str:
        return self.nome
    

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    data_cadastro = models.DateField(default = date.today)
    leitor = models.CharField(max_length=50, blank = True)
    data_inicio_leitura = models.DateTimeField(blank = True, null = True)
    data_final_leitura = models.DateTimeField(blank = True, null = True)
        
    def __str__(self) -> str:
        return self.titulo

   