import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Capture os Itens")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

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

# Pontuação
score = 0
font = pygame.font.SysFont("Arial", 24)

# Estado do jogo
game_active = False
paused = False

# Carregar imagem de fundo para a tela inicial
background_image = pygame.image.load("assets/1.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Redimensiona a imagem para caber na tela

# Função para desenhar texto na tela
def draw_text(text, font, color, x, y):
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

# Função para mostrar a tela de início
def show_menu():
    screen.blit(background_image, (0, 0))  # Desenha a imagem de fundo
    draw_text("Capture os Itens", pygame.font.SysFont("Arial", 48), WHITE, WIDTH // 4, HEIGHT // 4)
    draw_text("Pressione P para Jogar", font, WHITE, WIDTH // 4, HEIGHT // 2)
    pygame.display.flip()

# Função para mostrar a tela de pausa
def show_pause_menu():
    screen.fill(BLACK)
    draw_text("Pausado", pygame.font.SysFont("Arial", 48), WHITE, WIDTH // 3, HEIGHT // 4)
    draw_text("Pressione C para Continuar", font, WHITE, WIDTH // 4, HEIGHT // 2)
    draw_text("Pressione R para Reiniciar", font, WHITE, WIDTH // 4, HEIGHT // 2 + 30)
    draw_text("Pressione ESC para Sair", font, WHITE, WIDTH // 4, HEIGHT // 2 + 60)
    pygame.display.flip()

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
                # Reiniciar o jogo
                score = 0
                player_x = WIDTH // 2 - player_size // 2
                player_y = HEIGHT - 2 * player_size
                item_x = random.randint(0, WIDTH - item_size)
                item_y = 0
                game_active = True
                paused = False
        elif game_active and paused:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                # Continuar o jogo
                paused = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                # Reiniciar o jogo enquanto pausado
                score = 0
                player_x = WIDTH // 2 - player_size // 2
                player_y = HEIGHT - 2 * player_size
                item_x = random.randint(0, WIDTH - item_size)
                item_y = 0
                paused = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Sair do jogo a partir da tela de pausa
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

    # Detectar colisão
    if (player_x < item_x < player_x + player_size or
        player_x < item_x + item_size < player_x + player_size) and \
            player_y < item_y + item_size < player_y + player_size:
        score += 1
        item_y = 0
        item_x = random.randint(0, WIDTH - item_size)
        
    # Limpar a tela
    screen.fill(BLACK)

    # Desenhar o jogador e o item
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (item_x, item_y, item_size, item_size))

    # Exibir pontuação e instrução para pausar
    score_text = font.render(f"Pontos: {score}  |  Pressione ESC para Pausar", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Atualizar a tela
    pygame.display.flip()

# Encerrar pygame
pygame.quit()
sys.exit()
