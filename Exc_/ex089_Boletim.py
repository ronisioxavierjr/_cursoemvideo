"""Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente."""

aluno = []
classe = []

print(f'{"CADASTRAMENTO DE NOTAS V.1.0" :-^40}')
while True:
    print('\33[1;31;40mMODULO CADASTRAMENTO: \33[m \n')
    aluno.append(str(input('Digite o Nome do Aluno: ')).upper().strip())
    aluno.append(int(input('Digite a nota [1]: ')))
    aluno.append(int(input('Digite a nota [2]: ')))
    classe.append(aluno[:])
    aluno.clear()
    print('\n\n\n')
    while True:
        resp = str(input('Deseja encerrar o processo de cadastramento? (s/n) ')).upper().strip()
        if resp in "SN":
            break
    if resp in "S":
        break
for i in classe:
    i.append((i[1]+i[2])/2)

print(f'{"BOLETIM" :-^44}')
print("-" * 44)
for pos, i in enumerate(classe):
    print(f'Aluno [{pos+1 :2}]: {i[0] :15}  ||  Média: {i[3] :2}')
    print("-" * 44)

n = int(input("Digite o Número do Aluno para Detalhamento de Notas: "))
print(f'O Aluno {classe[n-1][0]} teve as seguintes notas: Nota 1: {classe[n-1][1]}, Nota 2:{classe[n-1][2]}')