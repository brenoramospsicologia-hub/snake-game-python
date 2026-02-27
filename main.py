import pygame
import random

# --- CONFIGURAÇÕES ---
LARGURA, ALTURA = 600, 400
TAMANHO_CELULA = 20
FUNDO = (15, 15, 30)
BRANCO = (255, 255, 255)
VERDE = (46, 204, 113)
AMARELO = (241, 196, 15)
VERMELHO = (231, 76, 60)

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake Game Pro - Níveis de Dificuldade")
relogio = pygame.time.Clock()

# Fontes
fonte_titulo = pygame.font.SysFont("Consolas", 50, bold=True)
fonte_texto = pygame.font.SysFont("Consolas", 20)

def desenhar_texto(texto, fonte, cor, x, y):
    obj_texto = fonte.render(texto, True, cor)
    ret_texto = obj_texto.get_rect(center=(x, y))
    tela.blit(obj_texto, ret_texto)

def menu_inicial():
    while True:
        tela.fill(FUNDO)
        desenhar_texto("SNAKE GAME", fonte_titulo, VERDE, LARGURA // 2, ALTURA // 4)
        
        desenhar_texto("Escolha a Dificuldade:", fonte_texto, BRANCO, LARGURA // 2, ALTURA // 2 - 20)
        desenhar_texto("1 - FÁCIL (Lento)", fonte_texto, AMARELO, LARGURA // 2, ALTURA // 2 + 20)
        desenhar_texto("2 - INTERMEDIÁRIO (Normal)", fonte_texto, AMARELO, LARGURA // 2, ALTURA // 2 + 50)
        desenhar_texto("3 - DIFÍCIL (Rápido)", fonte_texto, AMARELO, LARGURA // 2, ALTURA // 2 + 80)
        
        desenhar_texto("Pressione Q para Sair", fonte_texto, VERMELHO, LARGURA // 2, ALTURA - 40)
        
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return 10  # Velocidade Fácil
                if evento.key == pygame.K_2:
                    return 18  # Velocidade Média
                if evento.key == pygame.K_3:
                    return 30  # Velocidade Difícil
                if evento.key == pygame.K_q:
                    pygame.quit(); quit()

def jogar(velocidade_escolhida):
    x, y = LARGURA // 2, ALTURA // 2
    vel_x, vel_y = 0, 0
    corpo = [[x, y]]
    comprimento = 1
    
    comida_x = round(random.randrange(0, LARGURA - TAMANHO_CELULA) / 20.0) * 20.0
    comida_y = round(random.randrange(0, ALTURA - TAMANHO_CELULA) / 20.0) * 20.0
    
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and vel_x == 0: vel_x, vel_y = -TAMANHO_CELULA, 0
                if evento.key == pygame.K_RIGHT and vel_x == 0: vel_x, vel_y = TAMANHO_CELULA, 0
                if evento.key == pygame.K_UP and vel_y == 0: vel_y, vel_x = -TAMANHO_CELULA, 0
                if evento.key == pygame.K_DOWN and vel_y == 0: vel_y, vel_x = TAMANHO_CELULA, 0

        x += vel_x
        y += vel_y
        
        # Colisões (Parede e Próprio Corpo)
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA or [x, y] in corpo[:-1]:
            rodando = False 

        corpo.append([x, y])
        if len(corpo) > comprimento: del corpo[0]

        # Comer comida
        if x == comida_x and y == comida_y:
            comprimento += 1
            comida_x = round(random.randrange(0, LARGURA - TAMANHO_CELULA) / 20.0) * 20.0
            comida_y = round(random.randrange(0, ALTURA - TAMANHO_CELULA) / 20.0) * 20.0

        tela.fill(FUNDO)
        
        # Desenhar Comida
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_CELULA, TAMANHO_CELULA], border_radius=8)
        
        # Desenhar Cobra
        for i, c in enumerate(corpo):
            cor = (50, 255, 120) if i == len(corpo) - 1 else VERDE
            pygame.draw.rect(tela, cor, [c[0], c[1], TAMANHO_CELULA-1, TAMANHO_CELULA-1], border_radius=4)
        
        # Placar
        desenhar_texto(f"Pontos: {comprimento - 1}", fonte_texto, BRANCO, 70, 20)
        
        pygame.display.update()
        relogio.tick(velocidade_escolhida) # Usa a velocidade que veio do menu

# --- LOOP PRINCIPAL ---
while True:
    vel = menu_inicial() # O menu retorna o número (10, 18 ou 30)
    jogar(vel)           # Passamos esse número para a função jogar