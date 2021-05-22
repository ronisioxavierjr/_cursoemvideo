"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matrix = [[], [], []]
scol = soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l].append(int(input(f'Digite o termo {l + 1} | {c + 1} : ')))

print('A MATRIZ DIGITADA FOI:')
print('+=' * 12)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c] :^5}]', end=' ')
        if matrix[l][c] % 2 == 0:
            soma += matrix[l][c]
    print()
print('+=' * 12)

for c in range (0, 3):
    scol += matrix[c][2]

print(f'A soma dos valores da terceira linha é: {sum(matrix[2])}')
print(f'A soma da terceira coluna é: {scol}')
print(f'A soma dos pares é: {soma}')
print(f'O maior valor da segunda coluna é: {max(matrix[1])}')

