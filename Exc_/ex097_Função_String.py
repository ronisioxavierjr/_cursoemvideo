"""Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva(‘Olá, Mundo!’)
    Saída:
    ~~~~~~~~~
    Olá, Mundo!
    ~~~~~~~~~"""

def titulo(string):
    print('~' * len(string))
    print(string)
    print('~' * len(string))


string = str(input('Digite o texto do título: '))
titulo(string)

