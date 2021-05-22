"""Exercício Python 102: Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique o número a calcular e
outro chamado show, que será um valor lógico (opcional) indicando se será
mostrado ou não na tela o processo de cálculo do fatorial."""

def fatorial(num, show=True):
    """
    Função para cálculo de fatorial com possibilidade de mostrar calculo
    :param num: termo
    :param show: mostra ou não o calculo
    :return: resultado
    """
    factor = num
    if show:
        print(num, end=' ')
    for i in range(num, 1, -1):
         factor = factor*(i-1)
         if show:
            print(f'x {i-1}', end=' ')
    return factor


factor = int(input('Digite um Numero para Cálculo de Fatorial: '))
resp = str(input('Deseja mostrar o cálculo? (s/n)')).upper().strip()
num2 = fatorial(factor, show = (resp == "S"))
print(f'\n\nO resultado é {num2}')
