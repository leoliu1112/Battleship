import sys
import pygame
from pygame.locals import *
from game import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1000,600))

game=Game(DISPLAYSURF)
clock = pygame.time.Clock()
FPS=60

while True:
    mouse_x=0
    mouse_y=0
    click=False
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                click=True
    game.update(click,(mouse_x,mouse_y))
    DISPLAYSURF.fill((255,255,255))
    game.draw()
    pygame.display.update()
    clock.tick(FPS)
