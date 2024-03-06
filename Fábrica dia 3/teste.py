import requests

manaira = requests.get("https://viacep.com.br/ws/58038420/json/")

json = manaira.jason()


json.get("cep","Não tem cep")
print(json.get("cep","Não tem cep"))