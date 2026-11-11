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
