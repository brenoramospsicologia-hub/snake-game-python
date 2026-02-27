# 🐍 Snake Game Pro - CS Portfolio Edition

Este projeto é uma implementação técnica e robusta do clássico jogo da cobrinha, desenvolvida em **Python** com a biblioteca **Pygame**. O objetivo principal foi aplicar conceitos fundamentais de engenharia de software, lógica de programação e persistência de dados.

## 🚀 Funcionalidades e Conceitos de Computação

O projeto vai além de um jogo simples, integrando pilares essenciais:

* **Persistência de Dados (File I/O):** Implementação de um sistema de recorde que interage com o sistema de arquivos (`recorde.txt`). O jogo lê a pontuação máxima ao iniciar e a sobrescreve apenas se o novo recorde for atingido, garantindo que o progresso não seja perdido ao fechar o programa.
* **Lógica de Probabilidade:** Inclusão de um sistema de *Power-ups* com a "Maçã Dourada". Utilizei sorteio pseudoaleatório (`random.random()`) para definir uma chance de 20% de spawn, oferecendo um bônus de +5 pontos ao jogador.
* **Design de Níveis e Matrizes de Colisão:** O mapa de jogo é dinâmico. Dependendo da dificuldade escolhida (Fácil, Médio ou Difícil), o algoritmo gera diferentes coordenadas de obstáculos (paredes de pedra) que exigem detecção de colisão em tempo real.
* **Máquina de Estados Simples:** O fluxo do software é gerenciado por estados (Menu Inicial -> Seleção de Dificuldade -> Gameplay -> Game Over), garantindo uma experiência de usuário (UX) fluida.
* **Tratamento de Exceções:** Uso de blocos `try/except` para garantir que erros na leitura do arquivo de recorde não interrompam a execução do sistema.



## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12+
* **Biblioteca:** Pygame
* **Ambiente:** Virtualenv (venv)
* **Versionamento:** Git & GitHub

## 🕹️ Como Rodar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/snake-game-python.git](https://github.com/SEU-USUARIO/snake-game-python.git)
    ```
2.  **Crie e ative o ambiente virtual:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```
3.  **Instale o Pygame:**
    ```powershell
    pip install pygame
    ```
4.  **Inicie o jogo:**
    ```powershell
    python main.py
    ```

## 📈 Roadmap de Evolução
- [ ] Implementar sistema de **Vidas** (3 chances por rodada).
- [ ] Adicionar trilha sonora e efeitos de áudio.
- [ ] Criar animação de impacto ao colidir.
- [ ] Gerar executável (.exe) para distribuição.

---
Desenvolvido por um estudante de Ciência da Computação.
