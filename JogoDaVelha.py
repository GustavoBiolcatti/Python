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

tab = [[[], [], []], [[], [], []], [[], [], []]]

def ExibirJogo():
    print(" {} | {} | {} ".format(tab[0][0][0], tab[0][1][0], tab[0][2][0]))
    print("-"*11)
    print(" {} | {} | {} ".format(tab[1][0][0], tab[1][1][0], tab[1][2][0]))
    print("-"*11)
    print(" {} | {} | {} ".format(tab[2][0][0], tab[2][1][0], tab[2][2][0]))


def InserirPosicao(l, c, t):
    valid_pos = True
    while valid_pos:
        if 0 <= l <= 3 and 0 <= c <= 3:
            valid_pos = False
            tab[l][c] += t
        else:
            print("Posição fora de index! Digite novamente.")


jogadas = 1
while jogadas <= 9:
    rodada = True
    while rodada:
        verif_1 = True
        while verif_1:
            print("\nSua vez {}".format(j1_nome))
            tipo = "X"
            l1 = int(input("Posição na linha: "))
            c1 = int(input("Posição na cluna: "))

            InserirPosicao(l1, c1, tipo)
            verif_1 = False
        verif_2 = True
        jogadas += 1

        if jogadas >= 9:
            break

        while verif_2:
            print("\nSua vez {}".format(j2_nome))
            tipo = "O"
            l2 = int(input("Posição na linha: "))
            c2 = int(input("Posição na cluna: "))

            InserirPosicao(l2, c2, tipo)
            verif_2 = False
        jogadas += 1

        rodada = False

print("\n{}".format(ExibirJogo()))

