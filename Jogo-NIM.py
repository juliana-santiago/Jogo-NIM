def computador_escolhe_jogada(n, m):    
    if n <= m:
        return n
    else:
        if n % (m+1) > 0:
            return n % (m+1)
        return m

def usuario_escolhe_jogada(n, m):
    valor = int(input("\nQuantas peças você deseja tirar? "))
    while valor > m or valor <= 0 or valor > n:    
        print("\nOpa! Jogada inválida! Tente novamente.")
        valor = int(input("\nQuantas peças você deseja tirar? "))
        
    return valor

def partida():
    n = int(input("\nDeseja jogar com quantas peças no tabuleiro? "))
    m = int(input("\nQual o limite de peças por jogada?"))
    while m < 1:
        print("\nA quantidade de peças por jogadas deve ser menor ou igual as peças totais do jogo")
        m = int(input("\nQual o limite de peças por jogada? "))
    
    valor = 0
    jogada = 0
    if (n % (m+1)) == 0:
        print("\nVoce começa!")
        jogada = 1 #Vez do usuario
        while n > 0:
            if jogada == 1:
                valor = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", valor, "peça(s).")
                n = n - valor
                print("\nAgora tem apenas", n, "peças no tabuleiro.")
                jogada = 2
            else:
                valor = computador_escolhe_jogada(n, m)
                print("\nA maquina tirou", valor, "peça(s)")
                n = n - valor
                print("\nAgora tem apenas", n, "peças no tabuleiro.")
                jogada = 1
                
        if jogada == 1:
            print("\nFim de jogo! A maquina VENCEU!\n")
            return 2 #ponto para o computador
        else:
            print("\nFim do jogo! Você VENCEU!\n")
            return 1 #ponto para o usuario
                
    else:
        print("\nA maquina começa!")
        jogada = 2 #vez do computador
        while n > 0:
            if jogada == 2:
                valor = computador_escolhe_jogada(n, m)
                print("\nA maquina tirou", valor, "peça(s)")
                n = n - valor
                print("\nAgora tem apenas", n, "peças no tabuleiro.")
                jogada = 1
            else:
                valor = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", valor, "peça(s).")
                n = n - valor
                print("\nAgora tem apenas", n, "peças no tabuleiro.")
                jogada = 2
                
        if jogada == 1:
            print("\nFim do jogo! A maquina VENCEU!\n")
            return 2 #Ponto para o computador
        else:
            print("\nFim do jogo! Você VENCEU!\n")
            return 1 #Ponto para o usuario

def campeonato():
    quantidade_partida = 1
    placar_computador = placar_usuario = 0
    
    while quantidade_partida < 4:
        print("**** Rodada", quantidade_partida ,"****\n")
        if partida() == 1:
            placar_usuario = placar_usuario + 1
        else:
            placar_computador = placar_computador + 1
        quantidade_partida = quantidade_partida + 1
        
    print("\n**** Final do campeonato! ****\n")
    print("\nPlacar: Você", placar_usuario, "vs", placar_computador, "Maquina")

def main():
    print(" ____________________________")
    print("|   BEM-VINDO AO JOGO NIM!   |")
    print("|   1 - Partida isolada      |")
    print("|   2 - Campeonato           |")
    print("|____________________________|")
    
    escolha = int(input("\nSua escolha: "))    
    while escolha != 1 and escolha != 2:
        print("\nEscolha uma opção válida!")
        escolha = int(input("\nSua escolha: "))
        
    if escolha == 1:
        print("\nVocê optou por uma partida isolada!")
        partida()
    else:
        if escolha == 2:
            print("\nVocê optou por um campeonato!")
            campeonato()

main()
