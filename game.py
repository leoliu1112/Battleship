import sys
import pygame
from pygame.locals import *
from layout import *
from constant import *

CONS=constant()
WIDTH=CONS.WID
LENGTH=CONS.LEN

LAYOUT1=layout((50,50))
LAYOUT2=layout((550,50))

class Game(pygame.sprite.Sprite):
    def __init__(self, surface):
        self.surface=surface
        self.firstPlayer=True
        self.winner=1
        self.font=pygame.font.Font(None, 60)
        self.StartText=self.font.render("Start", True,(0,0,0))
        self.EndText=self.font.render("Player%d Wins"%self.winner, True,(0,0,0))

    def update(self, click, clickpos):
        if(click):
            if(self.firstPlayer):
                for n in range(WIDTH):
                    for m in range(LENGTH):
                        if(LAYOUT1.arrange[n][m].getRect().collidepoint(clickpos) and LAYOUT1.arrange[n][m].status==0):
                            LAYOUT1.arrange[n][m].update()
                            LAYOUT1.checkShipAlive()
                            self.firstPlayer=False
            
            else:
                for n in range(WIDTH):
                    for m in range(LENGTH):
                        if(LAYOUT2.arrange[n][m].getRect().collidepoint(clickpos) and LAYOUT2.arrange[n][m].status==0):
                            LAYOUT2.arrange[n][m].update()
                            LAYOUT2.checkShipAlive()
                            self.firstPlayer=True
        

    def draw(self):
        LAYOUT1.draw(self.surface)
        LAYOUT2.draw(self.surface)
