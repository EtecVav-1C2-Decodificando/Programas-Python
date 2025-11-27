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
#Modulo que mostra as regras 
def mostrar_regras():
    print("------------------------------")
    print("            REGRAS            ")
    print("------------------------------")
    print("Cada questão vale 0,5 pontos")
    print("Cada rodada é composta por 20 questões")
    print("Questões de múltipla escolha (A-E)")
    print("Há apenas uma alternativa correta")
    print("A pontuação máxima é 10 pontos")
    print("------------------------------")

    input("Pressione ENTER para voltar ao menu...")
    os.system('cls')
    mostrar_menu()

# Módulo responsavel por definir e embaralhar as questoes e alternativas
def sortear_questoes():
    questoes = [
      # === Historia e origem do projeto ===
        ("Em que ano o projeto Arduino foi criado?", ["2001", "2003", "2005", "2007", "2010"], "2005"),
        ("Onde o Arduino foi desenvolvido originalmente?", ["Italia", "EUA", "Japao", "Alemanha", "Canada"], "Italia"),
        ("Quem e considerado o principal criador do Arduino?", ["Massimo Banzi", "Elon Musk", "Steve Wozniak", "Bill Gates", "David Cuartielles"], "Massimo Banzi"),
        ("O Arduino foi criado como uma ferramenta de apoio a:", ["Engenheiros", "Professores", "Designers e estudantes", "Cientistas", "Programadores profissionais"], "Designers e estudantes"),
        ("O projeto Arduino nasceu no Instituto de:", ["Ivrea", "Milao", "Torino", "Roma", "Pisa"], "Ivrea"),

        # === Modelos e familias de placas ===
        ("Qual e o modelo de placa Arduino mais popular?", ["Arduino Mega", "Arduino Uno", "Arduino Nano", "Arduino Due", "Arduino Leonardo"], "Arduino Uno"),
        ("O Arduino Mega se destaca por possuir:", ["Mais memoria e pinos digitais", "Menos consumo", "Wi-Fi integrado", "Bluetooth", "Menor tamanho"], "Mais memoria e pinos digitais"),
        ("O Arduino Nano e conhecido por:", ["Ser compacto", "Ter display embutido", "Usar bateria interna", "Ter Wi-Fi", "Nao ter porta USB"], "Ser compacto"),
        ("O Arduino Due utiliza qual tipo de microcontrolador?", ["ATmega328", "ATmega2560", "ARM Cortex-M3", "ESP32", "ATtiny85"], "ARM Cortex-M3"),
        ("Qual placa Arduino ja vem com Wi-Fi integrado?", ["Arduino Uno", "Arduino Mega", "Arduino Nano", "Arduino Uno WiFi Rev2", "Arduino Leonardo"], "Arduino Uno WiFi Rev2"),

        # === Conexoes, portas e sinais ===
        ("As portas digitais do Arduino podem ser usadas para:", ["Sinais analogicos apenas", "Sinais digitais", "Sinais de radio", "Energia AC", "Som"], "Sinais digitais"),
        ("As portas analogicas do Arduino sao identificadas por:", ["D0 a D13", "A0 a A5", "P0 a P7", "ADC0 a ADC5", "PIN0 a PIN13"], "A0 a A5"),
        ("A tensao padrao de operacao do Arduino Uno e de:", ["3.3V", "5V", "9V", "12V", "1.8V"], "5V"),
        ("O pino GND do Arduino serve para:", ["Enviar dados", "Conectar a terra eletrica", "Fornecer energia", "Resetar o sistema", "Ativar o Wi-Fi"], "Conectar a terra eletrica"),
        ("O pino VIN e usado para:", ["Entrada de tensao externa", "Saida de som", "Ligacao USB", "Conexao serial", "Sensor de luz"], "Entrada de tensao externa"),

        # === Estrutura de codigos ===
        ("Um programa no Arduino e chamado de:", ["Script", "Sketch", "App", "Modulo", "Arquivo binario"], "Sketch"),
        ("As funcoes principais em todo codigo Arduino sao:", ["main() e loop()", "start() e end()", "setup() e loop()", "run() e stop()", "inicial() e repetir()"], "setup() e loop()"),
        ("A funcao setup() e executada:", ["A cada ciclo", "Somente uma vez no inicio", "Somente quando resetar", "Nunca", "A cada 10 segundos"], "Somente uma vez no inicio"),
        ("A funcao loop() e usada para:", ["Executar o codigo repetidamente", "Configurar portas", "Carregar bibliotecas", "Ler sensores uma vez", "Conectar Wi-Fi"], "Executar o codigo repetidamente"),
        ("A linguagem usada no Arduino e baseada em:", ["Python", "C/C++", "Java", "Assembly", "Rust"], "C/C++"),

        # === Principais comandos e funcoes da IDE Arduino ===
        ("A funcao pinMode() serve para:", ["Ler sensores", "Definir pinos como entrada ou saida", "Iniciar comunicacao serial", "Enviar dados", "Salvar dados na EEPROM"], "Definir pinos como entrada ou saida"),
        ("A funcao digitalWrite() faz:", ["Define nivel logico em um pino digital", "Ler valor analogico", "Ativa Wi-Fi", "Conecta Bluetooth", "Mostra mensagem no display"], "Define nivel logico em um pino digital"),
        ("A funcao digitalRead() retorna:", ["Um valor de tensao", "Um valor HIGH ou LOW", "Um numero aleatorio", "Um caractere", "Um byte de memoria"], "Um valor HIGH ou LOW"),
        ("A funcao analogRead() retorna valores de:", ["0 a 1023", "0 a 255", "0 a 1", "1 a 100", "0 a 5000"], "0 a 1023"),
        ("A funcao delay(1000) pausa o codigo por:", ["1 segundo", "100 segundos", "1 milissegundo", "1 minuto", "10 segundos"], "1 segundo"),

        # === Sensores, atuadores e shields ===
        ("Um sensor LDR mede:", ["Temperatura", "Luz", "Som", "Distancia", "Umidade"], "Luz"),
        ("Um servo motor e um tipo de:", ["Sensor", "Atuador", "Resistor", "Conversor", "Buzzer"], "Atuador"),
        ("Os shields no Arduino sao:", ["Placas de expansao", "Sensores de luz", "Programas externos", "Drivers USB", "Resistores"], "Placas de expansao"),
        ("Um buzzer serve para:", ["Gerar som", "Ler luz", "Medir temperatura", "Ativar LED", "Medir tensao"], "Gerar som"),
        ("Um sensor ultrassonico mede:", ["Distancia", "Temperatura", "Som", "Umidade", "Pressao"], "Distancia"),

        # === Comunicacoes ===
        ("A comunicacao Serial e feita pelos pinos:", ["0 e 1", "A0 e A1", "2 e 3", "13 e GND", "VIN e GND"], "0 e 1"),
        ("A taxa de transmissao padrao (baud rate) do Serial Monitor e:", ["115200", "4800", "9600", "19200", "57600"], "9600"),
        ("A comunicacao I2C usa quantos fios principais?", ["1", "2", "3", "4", "5"], "2"),
        ("A comunicacao SPI e conhecida por:", ["Alta velocidade", "Baixo consumo", "Longa distancia", "Facilidade de uso", "Compatibilidade Wi-Fi"], "Alta velocidade"),
        ("O modulo HC-05 e usado para conexao:", ["Bluetooth", "Wi-Fi", "Serial", "Ethernet", "I2C"], "Bluetooth"),

        # === Boas praticas e seguranca eletrica ===
        ("Qual e a tensao maxima recomendada nas portas do Arduino Uno?", ["3.3V", "5V", "9V", "12V", "24V"], "5V"),
        ("Antes de ligar novos componentes, deve-se sempre:", ["Verificar as especificacoes eletricas", "Soldar diretamente", "Usar qualquer fonte", "Desligar o computador", "Resetar o Arduino"], "Verificar as especificacoes eletricas"),
        ("O uso de resistores em serie com LEDs serve para:", ["Limitar corrente", "Aumentar brilho", "Reduzir tensao", "Mudar cor", "Ativar PWM"], "Limitar corrente"),
        ("Para evitar curto-circuitos, e recomendado:", ["Usar protoboard organizada", "Usar fios desencapados", "Ligar positivo no GND", "Soldar rapido", "Desligar o GND"], "Usar protoboard organizada"),
        ("E seguro alimentar o Arduino Uno com mais de 12V?", ["Sim", "Nao", "Depende do sensor", "Somente via USB", "Apenas com shield"], "Nao"),

        # === Casos de uso e aplicacoes praticas ===
        ("Um exemplo de aplicacao comum do Arduino e:", ["Controle de luzes", "Compilador C++", "Servidor web profissional", "Jogo 3D", "Banco de dados"], "Controle de luzes"),
        ("O Arduino pode ser usado em projetos de:", ["Automacao residencial", "Edicao de video", "Design grafico", "Redes sociais", "Navegacao GPS apenas"], "Automacao residencial"),
        ("Em um projeto de estufa automatica, o Arduino pode controlar:", ["Temperatura e umidade", "Rede Wi-Fi", "Fonte de energia", "Impressora", "Roteador"], "Temperatura e umidade"),
        ("Robos simples podem ser controlados por:", ["Arduino", "Planilha Excel", "Pendrive", "Calculadora", "HD externo"], "Arduino"),
		("Um sistema de irrigacao automatica com Arduino geralmente usa:", ["Sensor de umidade do solo", "Sensor de gas", "Sensor de movimento", "Sensor ultrassonico", "Sensor de cor"], "Sensor de umidade do solo"),
      
    ]
    random.shuffle(questoes) # Embaralha a lista de questoes
    for pergunta, alternativas, correta in questoes:
        random.shuffle(alternativas) # Embaralhas as alternativas
    return questoes

def exibir_questoes(perguntas_embaralhadas):
    qtd = 1
    pontuacao = 0
    letras = ["A", "B", "C", "D", "E"]
    for pergunta, alternativas, correta in perguntas_embaralhadas:
        if qtd > 20:
            break
        print(f"Pergunta numero{qtd}")
        print(pergunta)
        i = 0
        while i < len(letras) and i < len(alternativas):
            print(f"{letras[i]}) {alternativas[i]}")
            i += 1
        resposta_usuario = input("Digite a letra de sua resposta: ").upper()
        pontuacao += verificar_respostas(resposta_usuario, alternativas, correta) # Soma a pontuação retornada pela funçao verificar_resposta
        qtd += 1
    
    exibir_resultado(pontuacao) # Exibe pontuação final depois das 20 perguntas
# Módulo que soma as respostas e pontuação
def verificar_respostas(resposta_usuario, alternativas, correta):
    while resposta_usuario not in ["A", "B", "C", "D", "E"]:
        print("Letra inválida")
        resposta_usuario = input("Digite a letra de sua resposta: ").upper()

    pontos = 0

    if resposta_usuario == "A" and alternativas[0] == correta:
        print("✅️ Você Acertou!")
        pontos = 0.5
    elif resposta_usuario == "A":
        print(f"❌️ Errado! a resposta correta era: {correta}")

    elif resposta_usuario == "B" and alternativas[1] == correta:
        print("✅️ Você Acertou!")
        pontos = 0.5
    elif resposta_usuario == "B":
        print(f"❌️ Errado! a resposta correta era: {correta}")

    elif resposta_usuario == "C" and alternativas[2] == correta:
        print("✅️ Você Acertou!")
        pontos = 0.5
    elif resposta_usuario == "C":
        print(f"❌️ Errado! a resposta correta era: {correta}")

    elif resposta_usuario == "D" and alternativas[3] == correta:
        print("✅️ Você Acertou!")
        pontos = 0.5
    elif resposta_usuario == "D":
        print(f"❌️ Errado! a resposta correta era: {correta}")

    elif resposta_usuario == "E" and alternativas[4] == correta:
        print("✅️ Você Acertou!")
        pontos = 0.5
    elif resposta_usuario == "E":
        print(f"❌️ Errado! a resposta correta era: {correta}")
    
    print("Carregando próxima pergunta")
    time.sleep(2)
    os.system('cls')
    return pontos

def exibir_resultado(pontuacao_total):
    if pontuacao_total >= 7:
        print(f"🟢 Parabéns! Você acertou {pontuacao_total}/10")
    elif pontuacao_total >= 5:
        print(f"🟠 Muito bem! Você acertou {pontuacao_total}/10, mas ainda dá para melhorar!")
    else:
        print(f"🔴 Infelizmente você só acertou {pontuacao_total}/10, estude mais e tente novamente")

    input("Pressione ENTER para voltar ao menu: ")
    time.sleep(1)
    os.system('cls')
    mostrar_menu()
    
#  Chama a função responsavel por exibir o menu e iniciar o código
mostrar_menu()
