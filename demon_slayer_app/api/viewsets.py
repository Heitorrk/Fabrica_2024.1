from rest_framework.viewsets import ModelViewSet
from .serializer import DemonSerializer
from ..models import Demon
from rest_framework.response import Response
import requests

class DemonViewSet(ModelViewSet):
    serializer_class = DemonSerializer
    queryset = Demon.objects.all()

    def create(self, request):
        name = request.data.get("name", "")

        site = f"https://demon-slayer.cyclic.app/api/{name}"


        try:

            requisicao = requests.get(site)

            json = requisicao.json()
            

            name = json[0].get("name", "")
            race = json[0].get("race","")
            affiliation = json[0].get("affiliation","")
            skill = json[0].get("skill","")
            quote = json[0].get("quote","")

            dados_recebidos = {
                "name" : f"{name}",
                "race" : f"{race}",
                "affiliation" : f"{affiliation}",
                "skill" : f"{skill}",
                "quote" : f"{quote}",
            }

            meuserialiser = DemonSerializer(data = dados_recebidos)

            if meuserialiser.is_valid():

                demon_pesquisado = Demon.objects.filter(name=name)

                demon_pesquisado_existe = demon_pesquisado.exists()
                
                if demon_pesquisado_existe:
                    return Response({"Aviso":"seu personagem já existe no banco"})

                meuserialiser.save()
                return Response(meuserialiser.data)
            else:
                return Response({"aviso": f"Ocorreu um erro"})
        
        except:
            return Response({"aviso:": f"Personagem não faz parte do banco de dados"})

    def delete(self, pk=None):
        try:
            demon = Demon.objects.get(pk=pk)
        except Demon.DoesNotExist:
            return Response({"Aviso": "Personagem não encontrado"})

        demon.delete()
        return Response({"Aviso": "Personagem deletado com sucesso"})