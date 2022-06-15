from rich import print
import os

VOTOS_BOLSONARO = 0
VOTOS_CANDIDATOB = 0

while True:
    # Apresentar os candidatos
    print('*'*25)
    print(f'[on green]TOTAL BOLSONARO:[/]{VOTOS_BOLSONARO}{os.linesep}[on red]TOTAL CANDIDATOB[/]: {VOTOS_CANDIDATOB}')
    print('*'*25)
    try:
        voto = int(input(f'Em qual candidato gostaria de votar?{os.linesep}1 - Bolsonaro{os.linesep}2 - CANDIDATOB{os.linesep}seu voto: '))
        if voto == 1:
            VOTOS_BOLSONARO += 1
        elif voto == 2:
            VOTOS_CANDIDATOB += 1
        elif voto == 10:
            break
        else:
            pass
    except:
        print('Digite apenas 1 ou 2')
    os.system('clear')