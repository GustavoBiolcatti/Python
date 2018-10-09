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

j1_nome = input("\nNome 1º jogador: ").strip().title()
j2_nome = input("Nome 2º jogador: ").strip().title()

tab = [[["-"], ["-"], ["-"]], [["-"], ["-"], ["-"]], [["-"], ["-"], ["-"]]]


def ExibirJogo():
    for i in range(1,4):
        print(" {} | {} | {} ".format(tab[i-1][0][0], tab[i-1][1][0], tab[i-1][2][0]))
        if i < 3:
            print("-"*11)

            
def InserirPosicao(t):
    valid_pos = True
    while valid_pos:
        
        verif_input = True
        while verif_input:
            l = int(input("Posição na linha: "))
            c = int(input("Posição na cluna: "))
            
            if 0 <= l <= 3 and 0 <= c <= 3:
                if tab[l][c] != "X" and tab[l][c] != "O":
                    tab[l][c] = t
                    
                    valid_pos = False
                    verif_input = False
                    continue
                else:
                    print("\nPosição já preenchida! Digite outra posição.\n")
            else:
                print("\nPosição fora de index! Digite novamente.\n")
                
    
    print("\n\n{}".format(ExibirJogo()))
    
def VerifGanhou(nome):
    if (tab[0][0][0] == "X" and tab[0][1][0] == "X" and tab[0][2][0] == "X") or (tab[0][0][0] == "O" and tab[0][1][0] == "O" and tab[0][2][0] == "O"):
        print("Parabéns {}!".format(nome))
        
    elif (tab[1][0][0] == "X" and tab[1][1][0] == "X" and tab[1][2][0] == "X") or (tab[1][0][0] == "O" and tab[1][1][0] == "O" and tab[1][2][0] == "O"):
        print("Parabéns {}!".format(nome))
        
    elif (tab[0][0][0] == "X" and tab[2][1][0] == "X" and tab[2][2][0] == "X") or (tab[2][0][0] == "O" and tab[2][1][0] == "O" and tab[2][2][0] == "O"):
        print("Parabéns {}!".format(nome))
    
    elif (tab[0][0][0] == "X" and tab[1][0][0] == "X" and tab[2][0][0] == "X") or (tab[0][0][0] == "O" and tab[1][0][0] == "O" and tab[2][0][0] == "O"):
        print("Parabéns {}!".format(nome))
        
    elif (tab[0][1][0] == "X" and tab[1][1][0] == "X" and tab[2][1][0] == "X") or (tab[0][1][0] == "O" and tab[1][1][0] == "O" and tab[2][1][0] == "O"):
        print("Parabéns {}!".format(nome))
        
    elif (tab[0][2][0] == "X" and tab[1][2][0] == "X" and tab[2][2][0] == "X") or (tab[0][2][0] == "O" and tab[1][2][0] == "O" and tab[2][2][0] == "O"):
        print("Parabéns {}!".format(nome))
    
    if (tab[0][0][0] == "X" and tab[1][1][0] == "X" and tab[2][2][0] == "X") or (tab[0][0][0] == "O" and tab[1][1][0] == "O" and tab[2][2][0] == "O"):
        print("Parabéns {}!".format(nome))
        
    elif (tab[0][2][0] == "X" and tab[1][1][0] == "X" and tab[2][0][0] == "X") or (tab[0][2][0] == "O" and tab[1][1][0] == "O" and tab[2][0][0] == "O"):
        print("Parabéns {}!".format(nome))
        
        
jogo =  True
jogadas = 1
while jogo or jogadas <= 9:
    rodada = True
    while rodada:
        
        verif_1 = True
        while verif_1:
            print("\nSua vez {}".format(j1_nome))
            tipo = "X"
            
            InserirPosicao(tipo)
            VerifGanhou(j1_nome)
            verif_1 = False
            
        verif_2 = True
        jogadas += 1

        if jogadas >= 9:
            break
        
        ''

        while verif_2:
            print("\nSua vez {}".format(j2_nome))
            tipo = "O"

            InserirPosicao(tipo)
            VerifGanhou(j1_nome)
            
            verif_2 = False
        jogadas += 1
        
      

        rodada = False
