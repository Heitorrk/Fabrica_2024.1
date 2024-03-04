# desafio
# faça uma lista e um dicionário, aplicando todos os tipos de variáveis (int, float, string e boolean)
# e depois imprima na tela e duas operações matemáticas, uma com inteiros e outra com fracionados


lista = ["Heitor", 19, 6.5, False]
dicionario = {"Nome": "Heitor", "Idade": 19, "Valor na conta bancária": 6.5, "Banca uma coxinha?": False}


numb1i = int(input("Digite um número inteiro para multiplicar: "))
numb2i = int(input("Digite outro número inteiro para multiplicar: "))

multiplicacao = numb1i * numb2i

print(f"A multiplicação de {numb1i} vezes {numb2i} é", multiplicacao)

numb1f = float(input("Digite um número decimal para somar: "))
numb2f = float(input("Digite outro número decimal para somar: "))

soma = numb1f + numb2f

print(f"A soma de {numb1f} mais {numb2f} é", soma)

print("A lista é", lista)
print("O dicionario é", dicionario)