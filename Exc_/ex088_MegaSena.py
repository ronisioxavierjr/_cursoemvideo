"""Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para
 cada jogo, cadastrando tudo em uma lista composta."""
from random import randint
from time import sleep

jogo = []
jogos = []

print(f'{"MEGA SENA - JOGOS AUTOMÁTICOS" :-^40}')

njogos = int(input('Quantos Jogos você deseja fazer? '))

for i in range (0, njogos):
    for j in range (0, 6):
        jogo.append(randint(1,60))
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
print()
print(f'{"REALIZANDO OS PALPITES - AGUARDE" :-^40}')
for i in range(0, len(jogos)):
    print(f'Jogo {i+1} - {jogos[i]}')
    sleep(1)
print(f'BOA SORTE!!!!!')