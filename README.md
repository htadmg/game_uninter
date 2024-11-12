# Game de Trabalho de Linguagem de Programação Aplicada

## Descrição do Projeto

Um jogo DEMO de captura de itens desenvolvido com Python e Pygame. O objetivo do jogo é capturar itens que caem da parte superior da tela para ganhar pontos, evitando que eles cheguem ao fim da tela, o que faz o jogador perder vidas. O jogo oferece uma interface com uma tela de menu, opção de pausa e controle de pontuação.

## Funcionalidades do Jogo
- Menu Inicial: Tela inicial onde o jogador pode iniciar o jogo.
- Jogo em Andamento: Jogador controla um personagem para capturar itens e acumular pontos.
- Pausa: O jogador pode pausar o jogo a qualquer momento.
- Fim de Jogo: O jogo exibe uma mensagem de “Game Over” ao perder todas as vidas.
- Tela de Parabéns: Ao alcançar uma pontuação específica (20 pontos), o jogador recebe uma mensagem de parabéns e retorna ao menu principal.
- Vidas Representadas por Corações: Cada vida perdida é representada visualmente com uma imagem de coração.
  
## Tecnologias Usadas

- **Python**: Linguagem de programação usada para construir o backend.
- **Pygame**:  Biblioteca usada para desenvolvimento de jogos em Python, gerenciando a lógica do jogo, renderização de gráficos e detecção de eventos.

## Como Configurar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

1. **Clone o Repositório**
- Usando HTTPS:
```bash
git clone https://github.com/htadmg/game_uninter.git
```
- Usando SSH:
```bash
git clone git@github.com:htadmg/game_uninter.git
```
- Navegue até o diretório do projeto:
```bash
cd .\game_uninter
```
2. **Crie e Ative um Ambiente Virtual (opcional, mas recomendado)**
- **Para Linux/MacOS:**
```bash
python -m .venv venv
source .venv/bin/activate
```

- **Para Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
3. **Instale as dependências**
```bash
pip install -r requirements.txt
```
## Como Jogar
**Objetivo:** Capture o maior número de itens possível para aumentar sua pontuação. Atingir 20 pontos é o máximo necessário para vencer.
**Controles:**
- Seta Esquerda: Move o personagem para a esquerda.
- Seta Direita: Move o personagem para a direita.
- P: Inicia o jogo no menu principal.
- ESC: Pausa o jogo durante a partida.
- C: Continua o jogo a partir da pausa.
- R: Reinicia o jogo após a derrota.
  
**Perda de Vida:** Toda vez que um item não é capturado e passa pelo jogador, uma vida é perdida.
**Game Over:** O jogo termina quando todas as vidas são perdidas.
