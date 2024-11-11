import pygame
import random
import sys
import os

# Inicializar pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Capture os Itens")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Variáveis do jogador
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 10

# Variáveis dos itens
item_size = 20
item_x = random.randint(0, WIDTH - item_size)
item_y = 0
item_speed = 5

# Pontuação e vidas
score = 0
max_score = 20  # Pontuação máxima antes de voltar ao menu
lives = 3       # Pontos de vida
font = pygame.font.SysFont("Arial", 24)

# Estado do jogo
game_active = False
paused = False

def resource_path(relative_path):
    """Obtém o caminho correto para o arquivo de recurso, mesmo após a compilação com PyInstaller."""
    try:
        # PyInstaller cria um diretório temporário onde os recursos são extraídos
        base_path = sys._MEIPASS
    except Exception:
        # Caso o código esteja em execução como script Python normal
        base_path = os.path.abspath(".")
    
    # Retorna o caminho completo do arquivo de recurso
    return os.path.join(base_path, relative_path)

# Usar a função resource_path para carregar os arquivos
menu_background = pygame.image.load(resource_path("assets/1.png"))
menu_background = pygame.transform.scale(menu_background, (WIDTH, HEIGHT))

game_background = pygame.image.load(resource_path("assets/2.png"))
game_background = pygame.transform.scale(game_background, (WIDTH, HEIGHT))

player_image = pygame.image.load(resource_path("assets/Pink_Monster.png"))
player_image = pygame.transform.scale(player_image, (player_size, player_size))

item_image = pygame.image.load(resource_path("assets/Rock2.png"))
item_image = pygame.transform.scale(item_image, (item_size, item_size))

heart_image = pygame.image.load(resource_path("assets/Rock2.png"))
heart_image = pygame.transform.scale(heart_image, (30, 30))

# Função para desenhar texto na tela
def draw_text(text, font, color, x, y):
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

# Função para mostrar a tela de início
def show_menu():
    screen.blit(menu_background, (0, 0))
    draw_text("Capture os Itens", pygame.font.SysFont("Arial", 48), WHITE, WIDTH // 4, HEIGHT // 4)
    draw_text("Pressione P para Jogar", font, WHITE, WIDTH // 4, HEIGHT // 2)
    pygame.display.flip()

# Função para mostrar a tela de pausa
def show_pause_menu():
    screen.blit(menu_background, (0, 0))
    draw_text("Pausado", pygame.font.SysFont("Arial", 48), WHITE, WIDTH // 3, HEIGHT // 4)
    draw_text("Pressione C para Continuar", font, WHITE, WIDTH // 4, HEIGHT // 2)
    draw_text("Pressione R para Reiniciar", font, WHITE, WIDTH // 4, HEIGHT // 2 + 30)
    draw_text("Pressione ESC para Sair", font, WHITE, WIDTH // 4, HEIGHT // 2 + 60)
    pygame.display.flip()

# Função para mostrar mensagem de parabéns
def show_congratulations():
    screen.blit(game_background, (0, 0))
    draw_text("Parabéns! Você atingiu 20 pontos!", pygame.font.SysFont("Arial", 32), WHITE, WIDTH // 6, HEIGHT // 3)
    draw_text("Pressione qualquer tecla para voltar ao menu", font, WHITE, WIDTH // 6, HEIGHT // 2)
    pygame.display.flip()
    
    # Espera até que uma tecla seja pressionada
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False  # Sai do loop quando uma tecla é pressionada

# Função para mostrar mensagem de fim de jogo
def show_game_over():
    screen.blit(game_background, (0, 0))
    draw_text("Game Over", pygame.font.SysFont("Arial", 48), WHITE, WIDTH // 3, HEIGHT // 3)
    draw_text("Pressione R para Reiniciar ou ESC para Sair", font, WHITE, WIDTH // 6, HEIGHT // 2)
    pygame.display.flip()
    
    # Espera até que o jogador reinicie ou saia do jogo
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reiniciar o jogo
                    global score, lives, game_active
                    score = 0
                    lives = 3
                    game_active = True
                    waiting = False
                elif event.key == pygame.K_ESCAPE:  # Sair do jogo
                    pygame.quit()
                    sys.exit()

# Função para desenhar as vidas na tela
def draw_lives(lives):
    for i in range(lives):
        screen.blit(heart_image, (10 + i * 35, 50))  # Ajuste a posição e o espaçamento entre as imagens

# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
    # Manter a velocidade do jogo constante
    clock.tick(30)
    
    # Eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Teclas para controlar o menu
        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                game_active = True
                paused = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                score = 0
                lives = 3
                player_x = WIDTH // 2 - player_size // 2
                player_y = HEIGHT - 2 * player_size
                item_x = random.randint(0, WIDTH - item_size)
                item_y = 0
                game_active = True
                paused = False
        elif game_active and paused:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                paused = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                score = 0
                lives = 3
                player_x = WIDTH // 2 - player_size // 2
                player_y = HEIGHT - 2 * player_size
                item_x = random.randint(0, WIDTH - item_size)
                item_y = 0
                paused = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Pausar o jogo
        if game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            paused = True

    # Tela de início
    if not game_active:
        show_menu()
        continue

    # Tela de pausa
    if paused:
        show_pause_menu()
        continue

    # Verificar se atingiu a pontuação máxima
    if score >= max_score:
        show_congratulations()
        game_active = False  # Voltar ao menu principal
        score = 0           # Reiniciar a pontuação
        continue

    # Verificar se as vidas acabaram
    if lives <= 0:
        show_game_over()
        game_active = False
        continue

    # Desenha a imagem de fundo do jogo
    screen.blit(game_background, (0, 0))

    # Controles do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Movimento do item
    item_y += item_speed
    if item_y > HEIGHT:
        item_y = 0
        item_x = random.randint(0, WIDTH - item_size)
        lives -= 1  # Perde uma vida se o jogador não capturar o item

    # Detectar colisão
    if (player_x < item_x < player_x + player_size or
        player_x < item_x + item_size < player_x + player_size) and \
            player_y < item_y + item_size < player_y + player_size:
        score += 1
        item_y = 0
        item_x = random.randint(0, WIDTH - item_size)
        
    # Desenhar o jogador e o item
    screen.blit(player_image, (player_x, player_y))
    screen.blit(item_image, (item_x, item_y))

    # Exibir pontuação, vidas e instrução para pausar
    score_text = font.render(f"Pontos: {score}  |  Pressione ESC para Pausar", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # Desenhar as vidas como imagens de coração
    draw_lives(lives)

    # Atualizar a tela
    pygame.display.flip()

# Sair do pygame
pygame.quit()
