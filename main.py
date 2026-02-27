import pygame
import random

# Inicialização
pygame.init()
LARGURA, ALTURA = 600, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake Game - CS Student Edition")

# Cores e Configurações
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
TAMANHO_CELULA = 20
relogio = pygame.time.Clock()

def jogar():
    rodando = True
    
    # Cabeça da cobra
    x, y = LARGURA // 2, ALTURA // 2
    velocidade_x, velocidade_y = 0, 0
    
    # Corpo da cobra (Lista de segmentos)
    corpo_cobra = []
    comprimento_cobra = 1
    
    # Comida
    comida_x = round(random.randrange(0, LARGURA - TAMANHO_CELULA) / 20.0) * 20.0
    comida_y = round(random.randrange(0, ALTURA - TAMANHO_CELULA) / 20.0) * 20.0

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and velocidade_x == 0:
                    velocidade_x, velocidade_y = -TAMANHO_CELULA, 0
                elif evento.key == pygame.K_RIGHT and velocidade_x == 0:
                    velocidade_x, velocidade_y = TAMANHO_CELULA, 0
                elif evento.key == pygame.K_UP and velocidade_y == 0:
                    velocidade_y, velocidade_x = -TAMANHO_CELULA, 0
                elif evento.key == pygame.K_DOWN and velocidade_y == 0:
                    velocidade_y, velocidade_x = TAMANHO_CELULA, 0

        # Atualiza posição
        x += velocidade_x
        y += velocidade_y

        # Lógica de Crescimento (O "pulo do gato" da computação)
        cabeca = [x, y]
        corpo_cobra.append(cabeca)
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0] # Remove a "cauda" para dar o efeito de movimento

        # Colisão com a comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, LARGURA - TAMANHO_CELULA) / 20.0) * 20.0
            comida_y = round(random.randrange(0, ALTURA - TAMANHO_CELULA) / 20.0) * 20.0
            comprimento_cobra += 1

        # Colisão com as paredes (Game Over)
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
            rodando = False

        # Desenho
        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_CELULA, TAMANHO_CELULA])
        
        for segmento in corpo_cobra:
            pygame.draw.rect(tela, VERDE, [segmento[0], segmento[1], TAMANHO_CELULA, TAMANHO_CELULA])
            
        pygame.display.update()
        relogio.tick(10) # Velocidade inicial mais tranquila

    pygame.quit()

if __name__ == "__main__":
    jogar()