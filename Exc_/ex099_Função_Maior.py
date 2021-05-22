#Função para identificar o maior valor com uso de empacotamento.
from time import sleep
lista = list()


def maior(num):
    cont = maior = 0
    print(f'Analisando valores...')
    sleep(0.5)
    for i in num:
        print(f'{i} ', end = ' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = i
            cont += 1
        else:
            if maior < i:
                maior = i
            cont += 1
    print()
    print(f'Foram digitados {cont} valores, o maior é {maior}.')

def maiore(*num):
    cont = maior = 0
    print(f'Analisando valores...')
    sleep(0.5)
    for i in num:
        print(f'{i} ', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = i
            cont += 1
        else:
            if maior < i:
                maior = i
            cont += 1
    print()
    print(f'Foram digitados {cont} valores, o maior é {maior}.')

print('Análise de Numeros')
while True:
    num = int(input('Digite um número ou 999 para sair: '))
    if num == 999:
        break
    else:
        lista.append(num)
maior(lista)
maiore(2, 45, 25, 58, 63, 927)

