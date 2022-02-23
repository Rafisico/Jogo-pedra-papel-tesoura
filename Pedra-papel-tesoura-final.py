import random
x=0 #Placar jogador
y=0 #Placar computador
rodada=1


while (x+y)<5 or rodada<5:
    print('-------------------------') #Separador
    print(f'placar:{x}x{y}', end='  ') #Placar
    print(f'rodada:{rodada}')          #Rodada

    Jogador=input('pedra, papel ou tesoura? Digite sua jogada: ') #Input Jogador
    Jogador= Jogador.lower()

    lista = ['pedra', 'papel', 'tesoura']  # Lista computador

    if Jogador in lista:
        Computador=random.choice(lista)
        print(f'Jogada do computador: {Computador}')

        if Jogador == Computador:
           print('Empatou.')
           rodada+=1
        elif Jogador == 'pedra' and Computador == 'papel':
           print('Você perdeu.')
           y+=1
           rodada += 1
        elif Jogador == 'pedra' and Computador == 'tesoura':
           print('Você ganhou!')
           x+=1
           rodada += 1
        elif Jogador == 'papel' and Computador == 'pedra':
           print('Você ganhou!')
           x+=1
           rodada += 1
        elif Jogador == 'papel' and Computador == 'tesoura':
           print('Você perdeu.')
           y+=1
           rodada += 1
        elif Jogador == 'tesoura' and Computador == 'pedra':
           print('Você perdeu!')
           y+=1
           rodada += 1
        elif Jogador == 'tesoura' and Computador == 'papel':
           print('Você ganhou!.')
           x+=1
           rodada += 1
        else:
            continue
    else:
         print('Você digitou errado, jogue novamente!')
         continue
else:
    print('O jogo acabou!')