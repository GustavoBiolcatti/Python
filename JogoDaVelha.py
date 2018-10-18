#TUTORIAL
print("=" * 15)
print("{:^15}".format("POSIÇÕES"))
print("=" * 15)

print("""\n    0   1   2
0     |   |   
   -----------
1     |   |   
   -----------
2     |   |   \n""")

print("=" * 15)
#FIM TUTORIAL


j1_nome = input("\nNome 1º jogador: ").strip().title()
j2_nome = input("Nome 2º jogador: ").strip().title()

tab = [[["-"], ["-"], ["-"]], [["-"], ["-"], ["-"]], [["-"], ["-"], ["-"]]]


def ExibirJogo():
    '''Exibe como está o andamento do jogo'''
    for i in range(1, 4):
        print(" {} | {} | {} ".format(tab[i - 1][0][0], tab[i - 1][1][0], tab[i - 1][2][0]))
        if i < 3:
            print("-" * 11)


def InserirPosicao(t):
    '''Verifica se a jogada pode ser validada'''
    valid_pos = True
    while valid_pos:

        verif_input = True
        while verif_input:
            l = int(input("Posição na linha: "))
            c = int(input("Posição na coluna: "))

            #VERIFICA SE A POSIÇÃO ESTÁ DENTRO DO INDICE DA MATRIZ (3X3)
            if 0 <= l <= 3 and 0 <= c <= 3:

                #VERIFICA SE A POSIÇÃO JÁ ESTÁ PREENCHIDA
                if tab[l][c] != "X" and tab[l][c] != "O":
                    tab[l][c] = t

                    valid_pos = False
                    verif_input = False
                    continue
                else:
                    print("\nPosição já preenchida! Digite outra posição.\n")
            else:
                print("\nPosição fora de index! Digite novamente.\n")
    
    print("\n")
    print("\n\n{}".format(ExibirJogo()))


def VerifGanhou(nome):
    '''Verifica se o jogador venceu após sua jogada'''
    if(tab[0][0][0] == "X" and tab[0][1][0] == "X" and tab[0][2][0] == "X" or 
       tab[1][0][0] == "X" and tab[1][1][0] == "X" and tab[1][2][0] == "X" or
       tab[2][0][0] == "X" and tab[2][1][0] == "X" and tab[2][2][0] == "X" or
       tab[0][0][0] == "X" and tab[1][0][0] == "X" and tab[2][0][0] == "X" or
       tab[0][1][0] == "X" and tab[1][1][0] == "X" and tab[2][1][0] == "X" or
       tab[0][2][0] == "X" and tab[1][2][0] == "X" and tab[2][2][0] == "X" or
       tab[0][0][0] == "X" and tab[1][1][0] == "X" and tab[2][2][0] == "X" or
       tab[2][0][0] == "X" and tab[1][1][0] == "X" and tab[0][2][0] == "X"):
        
        print("Parabéns {}!".format(nome))
        quit()
        
    if(tab[0][0][0] == "O" and tab[0][1][0] == "O" and tab[0][2][0] == "O" or 
       tab[1][0][0] == "O" and tab[1][1][0] == "O" and tab[1][2][0] == "O" or
       tab[2][0][0] == "O" and tab[2][1][0] == "O" and tab[2][2][0] == "O" or
       tab[0][0][0] == "O" and tab[1][0][0] == "O" and tab[2][0][0] == "O" or
       tab[0][1][0] == "O" and tab[1][1][0] == "O" and tab[2][1][0] == "O" or
       tab[0][2][0] == "O" and tab[1][2][0] == "O" and tab[2][2][0] == "O" or
       tab[0][0][0] == "O" and tab[1][1][0] == "O" and tab[2][2][0] == "O" or
       tab[2][0][0] == "O" and tab[1][1][0] == "O" and tab[0][2][0] == "O"):
        
        print("Parabéns {}!".format(nome))
        quit()
        

#JOGADAS

jogo = True
jogadas = 1
while jogo and jogadas <= 9:
    rodada = True
    while rodada:

        #VEZ DO JOGADOR 1
        verif_1 = True
        while verif_1:
            print("\nSua vez {}".format(j1_nome))
            tipo = "X"

            InserirPosicao(tipo)
            VerifGanhou(j1_nome)
            verif_1 = False

        verif_2 = True
        jogadas += 1

        #VERIFICAÇÃO DE FIM DE JOGO
        if jogadas >= 9:
            print("VELHA! NINGUÉM GANHOU.")
            break

        #VEZ DO JOGADOR 2
        while verif_2:
            print("\nSua vez {}".format(j2_nome))
            tipo = "O"

            InserirPosicao(tipo)
            VerifGanhou(j1_nome)

            verif_2 = False
        jogadas += 1

        rodada = False
