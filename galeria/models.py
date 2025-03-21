from django.db import models
from datetime import datetime

OPCOES_CATEGORIA = [
    ("NEBULOSA","Nebulosa"),
    ("GALAXIA", "Galáxia"),
    ("ESTRELA", "Estrela"),
    ("PLANETA", "Planeta"),
]

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null = False, blank = False)
    legenda = models.CharField(max_length=150, null = False, blank = False)
    categoria = models.CharField(max_length=100, choices = OPCOES_CATEGORIA, default = '')
    descricao = models.TextField(null = False, blank = False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default = False)
    data_publicacao = models.DateTimeField(default=datetime.now(), blank= False)



    #função que retorna cada um dos itens da classe
    def __str__(self):
        return self.nome