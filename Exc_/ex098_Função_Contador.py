"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três
contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
    if i > f:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p

inicio = int(input('Digite o Primeiro Termo: '))
fim = int(input('Digite o último termo: '))
passo = int(input('Digite o passo: '))
contador(inicio, fim, passo)
