"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente."""

num = [[], []]
for i in range (0, 7):
    x = int(input('Digite um Número: '))
    if x % 2 == 0:
        num[0].append(x)
    else:
        num[1].append(x)
print('Numeros pares:')
print(f'{num[0]}')
print('Numeros Impares:')
print(f'{num[1]}')
