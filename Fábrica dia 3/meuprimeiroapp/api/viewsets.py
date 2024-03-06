from rest_framework.viewsets import ModelViewSet
from .serializer import PessoaSerializer
from ..models import PessoaBancoDeDado

class PessoaViewSet(ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = PessoaBancoDeDado.objects.all()