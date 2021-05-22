"""Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de
gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total
de gols feitos durante o campeonato."""

import statistics

jogador = dict()
jogo = list()
gol = list()
jogos = list()

jogador["Nome"] = str(input('Digite o nome do Jogador: '))
while True:
    cad_jogo = str(input('Deseja cadastrar informações sobre jogos? (S/N)')).upper().strip()
    if cad_jogo in "SN":
        break
if cad_jogo in "S":
    while True:
        jogo.append(input('Digite a Partida: '))
        gol.append(int(input('Digite o numero de gols da Partida: ')))
        while True:
            resp = str(input('Deseja continuar o cadastramento de Partidas? (S/N)')).upper().strip()
            if resp in "SN":
                break
        if resp in "N":
            break
jogos.append(jogo[:])
jogos.append(gol[:])
jogador["jogo"] = jogos[:]
# Impressão
print('*' * 30)
for k, v in jogador.items():
    if k == "Nome":
        print(f'Dados do Jogador {v}')
    if k == "jogo":
        print(f'Partidas Jogadas: {len(v[0])}')
        print(f'Saldo de Gols: {sum(v[1])}')
        print(f'Média de Gols por Partida: {statistics.mean(v[1])}')
        detalhe = input("Deseja detalhar os gols Realizados? ").upper().strip()
        if detalhe in 'S':
            for i in range(0, len(v[0])):
                print(f'Partida {v[0][i]} -- Gols: {v[1][i]}')
