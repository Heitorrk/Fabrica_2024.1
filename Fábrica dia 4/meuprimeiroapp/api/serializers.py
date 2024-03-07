from rest_framework.serializers import ModelSerializer
from ..models import PessoaBancoDeDados, ViaCepModel

class ViaCepSerializer(ModelSerializer):
    class Meta:
        model = ViaCepModel
        fields = ['id', 'cep', 'logradouro', 'complemento', 'bairro', 'uf']


class PessoaSerializer(ModelSerializer): # ver no site do django rest serializer e viewsets
    class  Meta:
        model = PessoaBancoDeDados
        fields = ['id', 'primeiro_nome', 'segundo_nome', 'idade']