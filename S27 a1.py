tabuleiro = [["~"] * 10 for i in range (10)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

def colocar_navio(tabuleiro, linha_inicial, coluna_inicial, tamanho, orientacao):
    if orientacao == "horizontal":
        for i in range(tamanho):
            tabuleiro[linha_inicial][coluna_inicial + i] = "#"
    elif orientacao == "vertical":
        for i in range(tamanho):
            tabuleiro[linha_inicial + i][coluna_inicial] = "#"
            
def dar_tiro(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == "#":
        tabuleiro[linha][coluna] = "X"
        print("Que tiro foi esse, ótimo acerto.")
        return True
    elif tabuleiro[linha][coluna] == "~":
        tabuleiro[linha][coluna] = "o"
        print("Passou longe, você é péssimo.")
        return False
    else:
        print("Quer atirar no mesmo lugar?")
        return False

def jogo():
    tamanho = 10
    tabuleiro_jogador1 = [["~"] * tamanho for _ in range(tamanho)]
    tabuleiro_jogador2 = [["~"] * tamanho for _ in range(tamanho)]
    
    colocar_navio(tabuleiro_jogador1, 1,2,3, "vertival")
    colocar_navio(tabuleiro_jogador2, 3,4,2, "horizontal")
    
    while True:
        print("Vez do Jogador 1:")
        imprimir_tabuleiro(tabuleiro_jogador2)
        x = int(input("Jogador 1 escolhe a linha do tiro: (0-9)"))
        y = int(input("Jogador 1 escolhe a coluna do tiro: (0-9)"))
        dar_tiro(tabuleiro_jogador2,x,y)
        
        if all(cell != "#" for row in tabuleiro_jogador2 for cell in row):
            print("Jogador 1 ganhou!")
            break
        
        print("Vez do Jogador 2:")
        imprimir_tabuleiro(tabuleiro_jogador2)
        x = int(input("Jogador 2 escolhe a linha do tiro: (0-9)"))
        y = int(input("Jogador 2 escolhe a coluna do tiro: (0-9)"))
        dar_tiro(tabuleiro_jogador1,x,y)
        
        if all(cell != "#" for row in tabuleiro_jogador2 for cell in row):
            print("Jogador 2 ganhou!")
            break
        
jogo()
    
    
