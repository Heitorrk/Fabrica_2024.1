from rest_framework.serializers import ModelSerializer
from ..models import PessoaBancoDeDado

class PessoaSerializer(ModelSerializer):
    class Meta:
        model = PessoaBancoDeDado
        fields = ['id','primeiroNome','segundoNome','idade']