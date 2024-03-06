from django.db import models

# Create your models here.

class PessoaBancoDeDado(models.Model):

    primeiroNome = models.CharField(verbose_name="Meu primeiro nome", max_length=20)
    segundoNome = models.CharField(verbose_name="Meu segundo Nome", max_length=25)
    idade = models.IntegerField(verbose_name="Minha idade", blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.primeiroNome} {self.segundoNome}"
    