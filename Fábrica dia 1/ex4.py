# ex4
# faça um programa que calcule a maioridade de uma pessoa

from datetime import date

dataAtual = date.today().year
#dataAno = '{}'.format(dataAtual.year)

anoNascimento = int(input("Digite o ano que você nasceu: "))

idade = dataAtual - anoNascimento

if idade >= 18:
    print(f"Você tem {idade} anos e é maior de idade")

else:
    print(f"Você tem {idade} anos e é menor de idade")