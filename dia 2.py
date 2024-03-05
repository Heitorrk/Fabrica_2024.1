# função que retorna um valor

# def valor(x, y):
#     x = int(x)
#     y = int(y)
#     return print(x + y)
    
# valor1 = int(input("Digite um valor: "))
# valor2 = int(input("Digite outro valor: "))
    
# valor(valor1, valor2)


# par ou ímpar

# valor = int(input("Digite um valor inteiro: "))

# if valor % 2:
#     print(f"O valor {valor} é ímpar")

# else:
#     print(f"O valor {valor} é par")


# while

# valor = float(input("Digite um valor: "))

# while valor >= 5:
#     valor = float(input("O valor é maior ou igual a 5\nDigite outro valor: "))

# print(f"O valor {valor} é menor que 5")


# for

# for i in range(7):
#     print("Olá mundo")


# função sem retorno

# def texto():
#     print("Olá mundo")

# texto()


# classe

# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
    
#     def ligar(self):
#         print("Seu veículo ligou", self.marca, self.modelo, self.ano)

# class SmartCar(Carro):
#     def localizar(self):
#         print(f"{self.modelo} esta localizado em João Pessoa")

# meuCarro = Carro("Peugeot", "207", 2010)
# meuCarro.ligar()
# carroVizinho = SmartCar("BMW", "320", 2024)
# carroVizinho.ligar()


# Desafio

class Animal:
    def __init__(self, nome, porte):
            self.nome = nome
            self.porte = porte

class Gato(Animal):
    def miar(self):
        print(f"O gato {self.nome} de {self.porte} faz miau")

class Cachorro(Animal):
    def latir(self):
        print(f"O cachorro {self.nome} de {self.porte} porte late")

class Pato(Animal):
    def quack(self):
        print(f"O pato {self.nome} faz quack")


meuGato = Gato("Sávio", "pequeno")
meuGato.miar()

meuCachorro = Cachorro("Doug", "médio")
meuCachorro.latir()

meuPato = Pato("Josenildo", "")
meuPato.quack()