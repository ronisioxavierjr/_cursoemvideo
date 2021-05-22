"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
   guardando tudo em uma lista. No final, mostre:
   A) Quantas pessoas foram cadastradas.
   B) Uma listagem com as pessoas mais pesadas.
   C) Uma listagem com as pessoas mais leves."""

pessoa = list()
pessoas = list()
gordo = magro = 0

#Inicio da leitura dos dados
while True:
    pessoa.append(str(input('Digite o Nome da Pessoa: ')))
    pessoa.append(int(input('Digite o peso da Pessoa:' )))
#Classificaçao conforme o peso
    if len(pessoas) == 0:
        magro = gordo = pessoa[1]
    else:
        if gordo < pessoa[1]:
            gordo = pessoa[1]
        if magro > pessoa[1]:
            magro = pessoa[1]
    pessoas.append(pessoa[:])
    while True:
        resp = str(input('Deseja Sair: (S/N): ')).upper().strip()
        if resp in "SN":
            break
    if resp == 'S':
        break
    pessoa.clear()

#RESULTADO NA TELA

print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'Gordos: {pessoas.count(gordo)}, magros {pessoas.count(magro)}')
print("*-*" *20)
if pessoas.count(gordo) > 0:
    print('O mais gordo é: ')
else:
    print('Os mais gordos são: ')
for p in pessoas:
    if p[1] == gordo:
        print(f'{p[0]}, ', end = ' ')
print(f'com {gordo} quilos....')
print("*-*" *20)
print()


for p in pessoas:
    if p[1] == magro:
        print(f'{p[0]}, ', end = ' ')
print(f'Com {magro} quilos')
print("*-*" *20)






