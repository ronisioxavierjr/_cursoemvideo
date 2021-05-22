"""Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

pessoa = dict()
cadastro = list()
soma = 0

while True:
    pessoa["Nome"] = str(input('Nome: ')).strip()
    while True:
        pessoa["Sexo"] = str(input('M/F: ')).upper().strip()
        if pessoa["Sexo"] not in "MF":
            print('Erro! Digite M (Masculino) ou F (Femenino)')
        if pessoa["Sexo"] in "MF":
            break
    pessoa["Idade"] = int(input('Digite a Idade: '))
    cadastro.append(pessoa.copy())
    while True:
        resp = str(input("Deseja Continuar? (S/N)")).upper().strip()
        if resp not in "SN":
            print('Erro! Digite S-Sim ou N-Não')
        if resp in "SN":
            break
    if resp in "N":
        break
print(cadastro)
print('*-*'*30)
print(f'Foram Cadastradas {len(cadastro)} pessoas.')
for i in cadastro:
    soma += i["Idade"]
print(f'A média das idades é {soma / len(cadastro)}')
print('As mulheres cadastradas são: ')
for i in cadastro:
    if i["Sexo"] in "F":
        print(f'{i["Nome"]} com {i["Idade"]} anos')
print('As pessoas com idade acima da média são: ')
for i in cadastro:
    if i["Idade"] > soma / len(cadastro):
        print(f'{i["Nome"]} com {i["Idade"]} anos')
