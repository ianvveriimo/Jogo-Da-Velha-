# JOGO DA VELHA 3X3
# Trabalho de Coding

vitorias_x = 0
vitorias_o = 0
empates = 0
total_partidas = 0

opcao = ""

while opcao != "4":

    print("\n===== JOGO DA VELHA =====")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Placar")
    print("4 - Sair")

    opcao = input("Escolha uma opcao: ")
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

jogador = "X"
venceu = False
vazias = 9
print("\n    1   2   3")

for i in range(3):

    print(i + 1, end="   ")

    for j in range(3):

        print(tabuleiro[i][j], end="")

        if j < 2:
            print(" | ", end="")

    print()

    if i < 2:
        print("   -----------")
elif opcao == "2":

    print("\n===== REGRAS =====")
    print("Dois jogadores participam.")
    print("O jogador X comeca.")
    print("Cada jogador escolhe uma linha e coluna.")
    print("Vence quem completar tres simbolos iguais.")
    print("O jogo pode terminar empatado.")
elif opcao == "3":

    print("\n===== PLACAR =====")
    print("Vitorias X:", vitorias_x)
    print("Vitorias O:", vitorias_o)
    print("Empates:", empates)
    print("Total de partidas:", total_partidas)
partida_encerrada = False

while partida_encerrada == False:

    print("\nVez do jogador:", jogador)
linha_valida = False

while linha_valida == False:

    entrada_linha = input("Digite a linha (1 a 3): ")

    for n in range(1, 4):

        if entrada_linha == str(n):

            linha = n - 1
            linha_valida = True

    if linha_valida == False:

        print("Linha invalida!")
coluna_valida = False

while coluna_valida == False:

    entrada_coluna = input("Digite a coluna (1 a 3): ")

    for n in range(1, 4):

        if entrada_coluna == str(n):

            coluna = n - 1
            coluna_valida = True

    if coluna_valida == False:

        print("Coluna invalida!")
if tabuleiro[linha][coluna] != " ":

    print("Casa ocupada!")
    print("Escolha outra posicao.")

else:

    tabuleiro[linha][coluna] = jogador
    vazias = vazias - 1
if partida_encerrada == False:

    if jogador == "X":
        jogador = "O"

    else:
        jogador = "X"
venceu = False

for i in range(3):

    if (tabuleiro[i][0] == jogador and
        tabuleiro[i][1] == jogador and
        tabuleiro[i][2] == jogador):

        venceu = True
diagonal_principal = True
diagonal_secundaria = True

for i in range(3):

    if tabuleiro[i][i] != jogador:

        diagonal_principal = False

    if tabuleiro[i][2 - i] != jogador:

        diagonal_secundaria = False

for j in range(3):

    if (tabuleiro[0][j] == jogador and
        tabuleiro[1][j] == jogador and
        tabuleiro[2][j] == jogador):

        venceu = True

if diagonal_principal == True:
    venceu = True

if diagonal_secundaria == True:
    venceu = True
vazias = 0

for i in range(3):

    for j in range(3):

        if tabuleiro[i][j] == " ":

            vazias = vazias + 1

if vazias == 0 and venceu == False:

    print("A partida terminou empatada!")

    empates = empates + 1
    total_partidas = total_partidas + 1

    partida_encerrada = True
    if venceu == True:

    print("Jogador", jogador, "venceu!")

    total_partidas = total_partidas + 1

    if jogador == "X":

        vitorias_x = vitorias_x + 1

    else:

        vitorias_o = vitorias_o + 1

    partida_encerrada = True
    pontos_x = 0
pontos_o = 0

vitorias_necessarias = 2

if jogador == "X" and venceu == True:

    pontos_x = pontos_x + 1

elif jogador == "O" and venceu == True:

    pontos_o = pontos_o + 1

if pontos_x >= vitorias_necessarias:

    print("JOGADOR X VENCEU O CAMPEONATO!")

elif pontos_o >= vitorias_necessarias:

    print("JOGADOR O VENCEU O CAMPEONATO!")