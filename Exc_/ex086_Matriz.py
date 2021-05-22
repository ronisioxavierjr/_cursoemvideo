"""Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3
e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela,
com a formatação correta."""

matrix = [[], [], []]

for l in range (0, 3):
    for c in range (0, 3):
        matrix[l].append(int(input(f'Digite o termo {l + 1} | {c + 1} : ')))

print('A MATRIZ DIGITADA FOI:')
print('+=' * 12)
for l in range (0, 3):
    for c in range (0, 3):
        print(f'[{matrix[l][c] :^5}]', end = ' ')
    print()
print('+=' *12)