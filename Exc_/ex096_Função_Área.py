"""Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno."""

def largura(a, b):
    print(f'A área do terreno é: {a * b}')


l = int(input('Digite a largura do terreno: '))
c = int(input('Digite o comprimento do terreno: '))
largura(l, c)