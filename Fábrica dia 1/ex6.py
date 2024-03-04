# ex6
# faça um programa que pergunte um número e diga se ele é um número primo ou não

numb = int(input("Digite um número: "))

if numb >= 1:
    for i in range(2, numb):
        if numb % i == 0:
            print(f"O número {numb} não é primo")
            break
    else:
        print(f"O número {numb} é primo")

elif numb <= 0:
    print(f"O número {numb} é zero ou negativo")