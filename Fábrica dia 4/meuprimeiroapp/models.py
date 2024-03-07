from django.db import models

# Create your models here.

class ViaCepModel(models.Model):
    cep = models.CharField(verbose_name = "Cep do Usuário", max_length = 20)
    logradouro = models.CharField(verbose_name = "Logradouro do Usuário", max_length = 100, blank=True, null = True)
    complemento = models.CharField(verbose_name = "Complemento do Usuário", max_length = 100, blank=True, null = True)
    bairro = models.CharField(verbose_name = "Localidade do Usuário", max_length = 100, blank=True, null = True)
    uf = models.CharField(verbose_name = "Estado do Usuário", max_length = 100, blank=True, null = True)
    
    def __str__(self) -> str:
        return f"{self.cep}"
    



class PessoaBancoDeDados(models.Model):
    
    primeiro_nome = models.CharField(verbose_name = "Meu primeiro nome", max_length = 20)
    segundo_nome = models.CharField(verbose_name = "Meu segundo Nome", max_length = 25)
    idade = models.IntegerField(verbose_name="Minha idade", blank = True, null = True)

    
    def __str__(self) -> str:
        return f"{self.primeiro_nome} {self.segundo_nome}"