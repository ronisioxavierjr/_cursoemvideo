"""Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com idade {idade}, não é permitido votar!'
    if 16 <= idade <18 and idade > 65:
        return f'Com idade {idade}, o voto é OPCIONAL!'
    else:
        return f'Voto OBRIGATORIO!'

ano = int(input('Digite o Ano de Nascimento: '))
print(voto(ano))