
from random import randint

lista = list()


def sorteia(lista):
    for i in range (0, 5):
        lista.append(randint(1, 5))
    print(lista)

def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma +=i
    print(soma)

sorteia(lista)
somapar(lista)