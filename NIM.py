def computador_escolhe_jogada(n, m):
    computadorR = 1

    while computadorR != m:
        if(n - computadorR) % (m+1) == 0:
            return computadorR
        else:
            computadorR += 1
    return computadorR

def usuario_escolhe_jogada(n, m):
    jogadaV = False

    while not jogadaV:
        jogadorR = int(input("Quantas peças voce vai tirar? "))
        if jogadorR > m or jogadorR < 1:
            print("Oops! Jogada inválida! Tente novamente.")
        else:
            jogadaV = True
    return jogadorR

def campeonato():
    numeroR= 1
    while numeroR <= 3:
        print("**** Rodada", numeroR, "****")
        partida()
        numeror += 1

    print("Placar: Você 0 X 3 Computador") 


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    vezdopc = False
    if n % (m + 1) == 0:
        print("Você começa!")
    else:
        print("Computador começa!")
        vezdopc = True

    while n > 0:
        if vezdopc:
            computadorR= computador_escolhe_jogada(n, m)
            n = n - computadorR
            if computadorR == 1:
                print("O computador tirou uma peça")
            else:
                print("O computador tirou", computadorR , "peças")
            vezdopc = False

        else:
            jogadorR = usuario_escolhe_jogada(n, m)
            n = n - jogadorR
            if jogadorR == 1:
                print("voce tirou uma peça")
            else:
                print("voce tirou", jogadorR, "peças")
            vezdopc= True
        if n ==1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            if n != 0:
                print("Agora resta", n, "peças no tabuleiro.")

    print("Fim do jogo! O computador ganhou!")
                

print("Bem-vindo ao jogo do NIM! Escolha:")

escolha1= print("1 - para jogar uma partida isolada")
escolha2= print("2 - para um campeonato 2")

escolhaDele=int(input("digite sua escolha: "))
if escolhaDele == 1:
    print("Voce escolheu uma partida isolada!")
    partida()
else:
    print("Voce escolheu um campeonato!")
    campeonato()

    




