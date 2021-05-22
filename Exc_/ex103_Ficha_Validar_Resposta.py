
def ficha(jogador='<Desconhecido>', gol = 0):
    print(f'O Jogador {jogador} fez {gol} gols.')

name = str(input('Digite o Nome do Jogador: '))
#leitura de variável como string para realizar teste isnumeric() e validar
gols = str(input('Digite a quantidade de Gols no Campeonato: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if name.strip() == '':
    ficha(gol = gols)
else:
    ficha(name, gols)


