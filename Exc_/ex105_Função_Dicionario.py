"""Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)"""


def resposta(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 5:
            r['Situação'] = 'Regular'
        else:
            r['Situação'] = 'Ruim'
    return r


resp = resposta(2.5, 3, 4.5, 7, 6.8, sit=True)
print(resp)