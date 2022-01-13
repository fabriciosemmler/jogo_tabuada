from os import wait
import sys
import random
import pygame
import pygame_textinput

pygame.init()

# Cores
yellow = (255, 255, 0)

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption('Jogo da Tabuada')
# Escolhe uma fonte e atribui um tamanho
myfont = pygame.font.SysFont("Comic Sans MS", 50)
myfont_big = pygame.font.SysFont("Comic Sans MS", 100)
# Aplica a fonte a um texto em um label
label = myfont.render(
    "Esse é o jogo da tabuada! Em quanto tempo você faz 9 acertos?", 1, yellow)

# Inicializa variáveis
score = 0
fator1 = random.randint(0, 10)
fator2 = random.randint(0, 10)
resultado_textinput = pygame_textinput.TextInputVisualizer()
resultado_textinput.font_object = myfont_big
resultado_textinput.font_color = yellow
venceu = False
loop = True

# Carrega imagens
fundo = pygame.image.load('assets/fundo.png')
clock_img = pygame.image.load('assets/yellow_clock.png')
score_trophy = pygame.image.load('assets/trophy.png')
score_img = pygame.image.load('assets/score/' + str(score) + '.png')
win = pygame.image.load('assets/win.png')

# Desenha fundo, tempo, fatores e resultado


def draw():
    global venceu
    global loop

    window.blit(fundo, (0, 0))
    window.blit(clock_img, (100, 200))
    window.blit(score_trophy, (100, 400))
    window.blit(score_img, (200, 410))

    if score < 9:
        # Põe a label de boas vindas no ponto x=100, y=100
        window.blit(label, (100, 100))
        ticks = int(pygame.time.get_ticks() / 1000)
        label_ticks = myfont.render(str(ticks), 1, yellow)
        window.blit(label_ticks, (225, 237))
    else:
        venceu = True

    if not venceu:
        label_tabuada = myfont_big.render(
            str(fator1) + ' x ' + str(fator2) + ' = ', 1, yellow)
        window.blit(label_tabuada, (500, 330))
        if fator1 == 10 or fator2 == 10:
            window.blit(resultado_textinput.surface, (800, 330))
        else:
            window.blit(resultado_textinput.surface, (750, 330))


# Monitora teclas e chama função de desenho
while loop:

    events = pygame.event.get()
    resultado_textinput.update(events)

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if resultado_textinput.value.isnumeric():
                    resultado = int(resultado_textinput.value)
                else:
                    resultado = 99
                if fator1 * fator2 == resultado:
                    score += 1
                    score_img = pygame.image.load(
                        'assets/score/' + str(score) + '.png')
                fator1 = random.randint(0, 10)
                fator2 = random.randint(0, 10)
                resultado_textinput.value = ''

    draw()
    pygame.display.update()

    if venceu:
        window.blit(fundo, (0, 0))
        window.blit(clock_img, (100, 200))
        ticks = int(pygame.time.get_ticks() / 1000)
        label_ticks = myfont.render(str(ticks), 1, yellow)
        window.blit(label_ticks, (225, 237))
        window.blit(score_trophy, (100, 400))
        window.blit(score_img, (200, 410))
        window.blit(win, (400, 330))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.quit()
                    sys.exit(0)
        loop = False
