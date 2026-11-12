# ==========================================
# JOGO DA VELHA 3X3
# TRABALHO DE CODING
# ==========================================

# PLACAR GERAL
vitorias_x = 0
vitorias_o = 0
empates = 0
total_partidas = 0

opcao = ""

# MENU PRINCIPAL
while opcao != "4":

    print("\n========== JOGO DA VELHA ==========")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Ver placar")
    print("4 - Sair")

    opcao = input("Escolha uma opcao: ")

    # INICIAR JOGO
    if opcao == "1":

        print("\nEscolha o modo:")
        print("1 - Partida normal")
        print("2 - Campeonato melhor de 3")

        modo = ""

        while modo != "1" and modo != "2":

            modo = input("Escolha: ")

            if modo != "1" and modo != "2":
                print("Opcao invalida!")

        pontos_x = 0
        pontos_o = 0
        partidas_campeonato = 0

        if modo == "1":
            vitorias_necessarias = 1
        else:
            vitorias_necessarias = 2

        campeonato_ativo = True

        # REPETICAO DAS PARTIDAS
        while campeonato_ativo == True:

            # CRIACAO DA MATRIZ
            tabuleiro = [
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ]

            # LIMPEZA DA MATRIZ
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = " "

            jogador = "X"
            partida_encerrada = False

            # SEQUENCIA DE JOGADAS
            while partida_encerrada == False:

                # EXIBICAO DO TABULEIRO
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

                print("\nVez do jogador:", jogador)

                jogada_valida = False

                # VALIDACAO DA JOGADA
                while jogada_valida == False:

                    # VALIDACAO DA LINHA
                    linha_valida = False

                    while linha_valida == False:

                        entrada_linha = input(
                            "Digite a linha (1 a 3): "
                        )

                        for n in range(1, 4):

                            if entrada_linha == str(n):
                                linha = n - 1
                                linha_valida = True

                        if linha_valida == False:
                            print("Linha invalida!")

                    # VALIDACAO DA COLUNA
                    coluna_valida = False

                    while coluna_valida == False:

                        entrada_coluna = input(
                            "Digite a coluna (1 a 3): "
                        )

                        for n in range(1, 4):

                            if entrada_coluna == str(n):
                                coluna = n - 1
                                coluna_valida = True

                        if coluna_valida == False:
                            print("Coluna invalida!")

                    # VERIFICAR CASA OCUPADA
                    if tabuleiro[linha][coluna] != " ":

                        print("Essa casa ja esta ocupada!")
                        print("Escolha outra posicao.")

                    else:

                        tabuleiro[linha][coluna] = jogador
                        jogada_valida = True

                # VERIFICAR VITORIA
                venceu = False

                diagonal_principal = True
                diagonal_secundaria = True

                # VERIFICAR LINHAS E DIAGONAIS
                for i in range(3):

                    if (tabuleiro[i][0] == jogador and
                        tabuleiro[i][1] == jogador and
                        tabuleiro[i][2] == jogador):

                        venceu = True

                    if tabuleiro[i][i] != jogador:
                        diagonal_principal = False

                    if tabuleiro[i][2 - i] != jogador:
                        diagonal_secundaria = False

                # VERIFICAR COLUNAS
                for j in range(3):

                    if (tabuleiro[0][j] == jogador and
                        tabuleiro[1][j] == jogador and
                        tabuleiro[2][j] == jogador):

                        venceu = True

                # CONFERIR DIAGONAIS
                if diagonal_principal == True:
                    venceu = True

                if diagonal_secundaria == True:
                    venceu = True

                # VERIFICAR VITORIA
                if venceu == True:

                    print("\nO jogador", jogador, "venceu!")

                    total_partidas = total_partidas + 1
                    partida_encerrada = True

                    if jogador == "X":

                        vitorias_x = vitorias_x + 1
                        pontos_x = pontos_x + 1

                    else:

                        vitorias_o = vitorias_o + 1
                        pontos_o = pontos_o + 1

                else:

                    # CONTAR CASAS VAZIAS
                    vazias = 0

                    for i in range(3):
                        for j in range(3):

                            if tabuleiro[i][j] == " ":
                                vazias = vazias + 1

                    # VERIFICAR EMPATE
                    if vazias == 0:

                        print("\nDeu empate!")

                        empates = empates + 1
                        total_partidas = total_partidas + 1

                        partida_encerrada = True

                # ALTERNAR JOGADORES
                if partida_encerrada == False:

                    if jogador == "X":
                        jogador = "O"
                    else:
                        jogador = "X"

            # CONTAR PARTIDA DO CAMPEONATO
            partidas_campeonato = partidas_campeonato + 1

            # MOSTRAR TABULEIRO FINAL
            print("\n========== TABULEIRO FINAL ==========")
            print("    1   2   3")

            for i in range(3):

                print(i + 1, end="   ")

                for j in range(3):

                    print(tabuleiro[i][j], end="")

                    if j < 2:
                        print(" | ", end="")

                print()

                if i < 2:
                    print("   -----------")

            # MOSTRAR PLACAR GERAL
            print("\n========== PLACAR GERAL ==========")
            print("Vitorias do X:", vitorias_x)
            print("Vitorias do O:", vitorias_o)
            print("Empates:", empates)
            print("Partidas realizadas:", total_partidas)

            # VERIFICAR CAMPEAO
            if pontos_x >= vitorias_necessarias:

                print("\nJOGADOR X VENCEU O CAMPEONATO!")
                campeonato_ativo = False

            elif pontos_o >= vitorias_necessarias:

                print("\nJOGADOR O VENCEU O CAMPEONATO!")
                campeonato_ativo = False

            elif modo == "1":

                campeonato_ativo = False

            elif partidas_campeonato >= 3:

                print("\nCAMPEONATO TERMINOU EMPATADO!")
                campeonato_ativo = False

            else:

                print("\nPlacar do campeonato:")
                print("Jogador X:", pontos_x)
                print("Jogador O:", pontos_o)
                print("Nova partida do campeonato!")

    # MOSTRAR REGRAS
    elif opcao == "2":

        print("\n========== REGRAS ==========")
        print("O jogo possui dois jogadores: X e O.")
        print("O jogador X comeca.")
        print("Cada jogador escolhe uma linha e uma coluna.")
        print("Vence quem completar tres simbolos iguais.")
        print("A sequencia pode ser horizontal, vertical ou diagonal.")
        print("Se todas as casas forem preenchidas sem vencedor, ocorre empate.")

    # MOSTRAR PLACAR
    elif opcao == "3":

        print("\n========== PLACAR ==========")
        print("Vitorias do X:", vitorias_x)
        print("Vitorias do O:", vitorias_o)
        print("Empates:", empates)
        print("Total de partidas:", total_partidas)

    # SAIR DO PROGRAMA
    elif opcao == "4":

        print("\n========== RESULTADO FINAL ==========")
        print("Vitorias do X:", vitorias_x)
        print("Vitorias do O:", vitorias_o)
        print("Empates:", empates)
        print("Total de partidas:", total_partidas)

        if total_partidas > 0:

            percentual_x = (vitorias_x / total_partidas) * 100
            percentual_o = (vitorias_o / total_partidas) * 100

            print("Porcentagem de vitorias do X:", percentual_x, "%")
            print("Porcentagem de vitorias do O:", percentual_o, "%")

        print("\nObrigado por jogar!")

    else:

        print("Opcao invalida! Escolha de 1 a 4.")