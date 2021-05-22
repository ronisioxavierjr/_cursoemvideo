"""Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de
ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import date

cadastro = dict()
cadastro["Nome"] = input(str('Digite o Nome do Trabalhador: '))
cadastro["Ano_Nascimento"] = int(input('Digite o Ano de Nascimento: '))
cadastro["Idade"] = date.today().year - cadastro["Ano_Nascimento"]
cadastro["CTPS"] = int(input('Digite o Numero da Carteira de Trabalho: '))
if cadastro["CTPS"] != 0:
    cadastro["Ano_Contract"] =int(input('Digite o ANO de contratação: '))
    cadastro["rent"] = ((cadastro["Ano_Contract"]+35)-date.today().year)+cadastro["Idade"]
    cadastro["salary"] = float(input('Digite o Salário do Funcionário: '))
print(cadastro.items())
print(cadastro.values())
print(cadastro.keys())
print("-*-" *30)
for k, v in cadastro.items():
    print(f'O {k} é {v}.')
