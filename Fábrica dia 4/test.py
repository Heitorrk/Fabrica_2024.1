import requests

nome = requests.get("http://127.0.0.1:8000/api/pessoa/1")

json = nome.json()

print(json.get("primeiro_nome", "Nome não encontrado"))