"""Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado."""
from random import randint
from time import sleep
from operator import itemgetter

jogador = {"Jogador 1": randint(1, 6),
           "Jogador 2": randint(1, 6),
           "Jogador 3": randint(1, 6),
           "Jogador 4": randint(1, 6)
           }
#Teste de Impressão
for k, v in jogador.items():
    print(f'O Jogador {k}, tirou {v}.')
    sleep(1)
#Ordenação do Dicionário
ordena = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print("\n\n\n")
for k, v in enumerate(ordena):
    if k == 0:
        print(f'{k+1}º Colocado: {v[0]} com {v[1]} pontos. PARABÉNS!!!! FODÃO!!!!!')
    else:
        print(f'{k+1}º Colocado: {v[0]} com {v[1]} pontos. ')
