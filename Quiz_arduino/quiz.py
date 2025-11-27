# Módulo que exibe o menu inicial
def mostrar_menu():
    print("Seja bem vindo ao Quiz! sobre Arduíno")
    print("------------------------------")
    print("             MENU             ")
    print("------------------------------")
    print("Escolha uma das opcoes pelo número")
    print("1 - Iniciar quiz")
    print("2 - Exibir regras")
    print("3 - Encerrar programa")
    print("4 - Créditos")
    print("------------------------------")

    opcao = int(input("Digite a opcao desejada: "))  # Lê a opção do menu que o jogador escolher
    os.system('cls')

    if opcao == 1:
        perguntas = sortear_questoes()
        exibir_questoes(perguntas)

    elif opcao == 2:
        mostrar_regras()  # chama o módulo responsável pelas regras
        input("Pressione ENTER para voltar ao menu...")
        os.system('cls')
        mostrar_menu()

    elif opcao == 3:
        i = 3
        while i >= 1:
            print(f"Encerrando em {i}s")
            time.sleep(1)
            i -= 1
        print("Encerrando...")
        time.sleep(1)
        exit()

    elif opcao == 4:
        print("------------------------------")
        print("        CRÉDITOS DO QUIZ      ")
        print("------------------------------")
        print("👤 Brayan Frezzarin Do Nascimento")
        print("👤 Daniel Kolde Boucas")
        print("👤 Gustavo de Lima Costa")
        print("👤 William Lucas da Silva\n")
        print("------------------------------")

        input("Pressione ENTER para voltar ao menu...")
        os.system('cls')
        mostrar_menu()

    else:
        print("Opcao invalida!")
        time.sleep(1)
        mostrar_menu()
