from django.db import models

# Create your models here.
class convertir(models.Model):
    numeroDecimal=models.IntegerField()
    numeroBinario=models.IntegerField()
    numeroOctal=models.IntegerField()
    numeroHexadecimal=models.IntegerField()
    #funcion=models.TextField(help_text='escribe la funcion')
    def _unicode_(self):
        return self.numero
