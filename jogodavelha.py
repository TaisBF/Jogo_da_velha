import os
import random
from colorama import Fore, Back, Style

# Variáveis
jogarNovamente = "s"
jogadas = 0
quemJoga = 2  # 1=CPU 2=Jogador
maxJogadas = 9
vit = "n"

# Matriz principal
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Função de desenho da tela
def tela():
    global velha
    global jogadas
    os.system('clear')
    print("    0   1   2 ")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("   -----------")
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)


# Função de jogadas do jogador
def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input("Linha..:"))
            c = int(input("Coluna..:"))

            while velha[l][c] != " ":
                l = int(input("Linha..:"))
                c = int(input("Coluna..:"))
            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Jogada inválida")
            os.system("pause")


# Função de jogadas da CPU
def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = "O"
        jogadas += 1
        quemJoga = 2

# Função de vitoria
def verificarVitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"

        # Verificar Linhas 
        il=0
        ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(velha[il][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):  
                vitoria=s
                break
            il+=1

        if(vitoria!="n"):
            break

        # Verificar Colunas 
        il=0
        ic=0
        while ic<3:
            soma=0
            il=0
            while il<3:
                if(velha[il][ic]==s):
                    soma+=1
                il+=1
            if(soma==3):  
                vitoria=s
                break
            ic+=1
        if(vitoria!="n"):
            break

        # Verificar Diagonais 

            # Diagonal 1
        soma=0
        idiag=0
        while idiag<3:
            if(velha[idiag][idiag]==s):
              soma+=1
            idiag+=1
        if(soma==3):  
            vitoria=s
            break

            # Diagonal 2
        soma=0
        idiagl=0
        idiagc=2

        while idiagc>=3:
            if(velha[idiagl][idiagc]==s):
              soma+=1
            idiagl+=1
            idiagc-=1
        if(soma==3):  
            vitoria=s
            break
    return vitoria

# Função de redefinir 
def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0
    quemJoga = 2 
    maxJogadas = 9
    vit = "n"

    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


# loop principal - definição das condições do jogo
while(jogarNovamente=="s" or jogarNovamente=="S"):
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit=verificarVitoria()
        if(vit!="n") or (jogadas>=maxJogadas):
            break
    print(Fore.RED + "FIM DE JOGO" + Fore.YELLOW )
    if(vit=="X" or vit=="O"):
        print("Resultado: Jogador" + vit + " venceu")
    else: 
        print("Resultado: Empate")
    jogarNovamente=input(Fore.BLUE + "Jogar Novamente? [s/n]" + Fore.RESET)
    redefinir()