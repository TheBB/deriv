#!/usr/bin/python

import pygame, sys, game
from pygame.locals import *

WIDTH = 640
HEIGHT = 480
DRAWSTEP = 3
TICK = 30
VOLATILITY = 0.8
TIMESTEP = float(TICK)/1000
if len(sys.argv) < 2:
    ORDER = 2
else:
    ORDER = int(sys.argv[1])

BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)

pygame.init()
fpsClock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Deriv')

drawX = range(0, WIDTH/2, DRAWSTEP)
drawY = [HEIGHT/2] * len(drawX)
numDraw = len(drawX)

cDerivatives = [0] * (ORDER+1)
pDerivatives = cDerivatives

paused = True

game = game.Game(ORDER, len(drawX))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos
        elif event.type == MOUSEBUTTONUP:
            paused = not paused
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    if not paused:
        mouseX, mouseY = pygame.mouse.get_pos()
        game.tick(VOLATILITY * (1-2*float(mouseY)/HEIGHT), TIMESTEP)
        #cDerivatives[ORDER] = VOLATILITY * (1 - 2*float(mouseY)/HEIGHT)
        #for i in range(ORDER,0,-1):
            #cDerivatives[i-1] = pDerivatives[i-1] + 0.5*TIMESTEP*(pDerivatives[i] + cDerivatives[i])
        #pDerivatives = cDerivatives
        #drawY.append(int(0.5*HEIGHT*(1-cDerivatives[0])))
        drawY.append(int(0.5*HEIGHT*(1-game.history[-1])))
        drawY.pop(0)

    window.fill(BLACK)

    if paused:
        text = font.render("Paused", True, WHITE)
        textpos = text.get_rect(centerx = WIDTH/2)
        textpos.top = 50
        window.blit(text, textpos)

    for i in range(0, min(len(drawY),numDraw)-1):
        pygame.draw.line(window, WHITE, (drawX[i],drawY[i]), (drawX[i+1],drawY[i+1]))

    pygame.display.update()
    fpsClock.tick(TICK)
