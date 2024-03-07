from rest_framework.viewsets import ModelViewSet
from ..models import PessoaBancoDeDados, ViaCepModel
from .serializers import PessoaSerializer, ViaCepSerializer
from rest_framework.response import Response
import requests

class ViaCepViewSet(ModelViewSet):
    queryset = ViaCepModel.objects.all()
    serializer_class = ViaCepSerializer


    
    def create(self, request):
        cep = request.data.get("cep", "00000000")

        site = f"https://viacep.com.br/ws/{cep}/json/"

        requisicao = requests.get(site)

        json = requisicao.json()
        
        cep = json.get("cep", "")
        logradouro = json.get("logradouro","")
        complemento = json.get("complemento","")
        bairro = json.get("bairro","")
        localidade = json.get("localidade","")
        uf = json.get("uf","")

        dados_recebidos = {
            "cep" : f"{cep}",
            "logradouro" : f"{logradouro}",
            "complemento" : f"{complemento}",
            "bairro" : f"{bairro}",
            "localidade" : f"{localidade}",
            "uf": f"{uf}"
        }

        meuserialiser = ViaCepSerializer(data = dados_recebidos)

        if meuserialiser.is_valid():

            cep_pesquisado = ViaCepModel.objects.filter(cep=cep)

            cep_pesquisado_existe = cep_pesquisado.exists()
            
            if cep_pesquisado_existe:
                return Response({"Aviso":"seu cep já existe no banco"})

            meuserialiser.save()
            return Response(meuserialiser.data)
        else:
            return Response({"aviso":f"{"Ocorreu um erro"}"})


class PessoaViewSet(ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = PessoaBancoDeDados.objects.all() # puxa todas as pessoas do models