📘 Quiz sobre Arduino

Um quiz interativo em Python desenvolvido para testar seus conhecimentos sobre Arduino, desde história e modelos de placas até sensores, funções da IDE e boas práticas.

O jogo inclui menu, regras, créditos, sorteio aleatório de questões, embaralhamento de alternativas, correção automática e pontuação final.

---

🚀 Funcionalidades

Menu inicial com:

Iniciar quiz
Exibir regras
Créditos
Encerrar programa

20 perguntas por rodada
Questões totalmente embaralhadas
Alternativas embaralhadas a cada execução
Correção automática com feedback (acerto/erro)
Pontuação final de 0 a 10
Interface simples direto no terminal

---

📂 Estrutura Geral do Código

- O projeto contém funções para cada parte do jogo:
- mostrar_menu() → exibe o menu principal
- mostrar_regras() → exibe as regras do jogo
- sortear_questoes() → cria e embaralha a lista de questões
- exibir_questoes() → apresenta as perguntas ao jogador
- verificar_respostas() → valida as alternativas e soma pontos
- exibir_resultado() → mostra a pontuação final

---

🧠 Como funciona o Quiz

Cada questão vale 0,5 ponto
São 20 perguntas por rodada
Alternativas são de A a E
Apenas uma correta
Pontuação máxima: 10 pontos

---

▶️ Como executar

Certifique-se de ter o Python instalado.

1. Baixe o arquivo .py
2. Abra o terminal na pasta do arquivo
3. Execute:
quiz.py

---

👨‍💻 Tecnologias utilizadas

Python 3

Módulos padrão:
os
time
random

---

👥 Créditos

👤 Brayan Frezzarin Do Nascimento - "sortear_questoes" e "exibir_questoes"

👤 Daniel Kolde Boucas - "exibir_resultado"

👤 Gustavo de Lima Costa - "mostrar_menu()"

👤 William Lucas da Silva - "mostrar_regras" e "verificar_respostas"

---

📄 Licença

Este projeto é apenas para fins educacionais.
