import pygame

pygame.init()

# Cores
yellow = (255, 255, 0)

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption('Jogo da Tabuada')
# Escolhe uma fonte e atribui um tamanho
myfont = pygame.font.SysFont("Comic Sans MS", 50)
# Aplica a fonte a um texto em um label
label = myfont.render(
    "Esse é o jogo da tabuada! Em quanto tempo você faz 9 acertos?", 1, yellow)

# Inicializa variáveis
score = 0
fator1 = 0
fator2 = 0
resultado = 0

# Carrega imagens
fundo = pygame.image.load('assets/fundo.png')
clock_img = pygame.image.load('assets/yellow_clock.png')
score_trophy = pygame.image.load('assets/trophy.png')
score_img = pygame.image.load('assets/score/0.png')
win = pygame.image.load('assets/win.png')

# Desenha fundo, tempo, fatores e resultado


def draw():
    window.blit(fundo, (0, 0))
    window.blit(clock_img, (100, 200))
    window.blit(score_trophy, (100, 400))
    score_img = pygame.image.load('assets/score/' + str(score) + '.png')
    window.blit(score_img, (200, 410))

    if score < 9:
        # Põe a label de boas vindas no ponto x=100, y=100
        window.blit(label, (100, 100))
        ticks = int(pygame.time.get_ticks() / 1000)

    else:
        window.blit(win, (300, 330))

    label_ticks = myfont.render(str(ticks), 1, yellow)
    window.blit(label_ticks, (225, 237))


# Monitora teclas e chama função de desenho
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    draw()
    pygame.display.update()
