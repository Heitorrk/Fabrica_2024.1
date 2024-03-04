# ex2
# faça um programa que some a média de 5 alunos e faça a média aritmética entre eles

media = 0
nota = 0
while media < 5:

    notas = int(input("Digite sua nota: "))
    nota = nota + notas
    media = media + 1

mediaAritmetica = nota/5
print("A média dos 5 alunos é",mediaAritmetica)