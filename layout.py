import pygame, sys
from pygame.locals import *
from block import *
from constant import *
import random

CONS=constant()
WIDTH=CONS.WID
LENGTH=CONS.LEN
ORIENT=CONS.orient
SHIPS=CONS.ships

class layout(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.arrange=[]
        self.shipAlive=[]
        for n in range(WIDTH):
            temp=[]
            for m in range(LENGTH):
                temp.append(Block(n,m,40,40,pos,0,False))
            self.arrange.append(temp)
        self.placeShip()


    def update(self,clickpos):
        pass

    def update(self):
        pass
    
    def checkShipAlive(self):
        for i in self.shipAlive:
            die=True
            for j in i:
                if(self.arrange[j[0]][j[1]].status!=2):
                    die=False
                    break
            if(die):
                for n in i:
                    self.arrange[n[0]][n[1]].status=3
                    self.arrange[n[0]][n[1]].loadImage()


    def draw(self, surface):
        for n in range(WIDTH):
            for m in range(LENGTH):
                self.arrange[n][m].draw(surface)

    def placeShip(self):
        i=0
        while(i<5):
            direction=random.choice(ORIENT)
            relpos=(random.randint(0,WIDTH-1),random.randint(0,LENGTH-1))
            placed=False
            if(direction=="horizontal"):
                for u in range(SHIPS[i]):
                    if(relpos[0]+u<0 or relpos[0]+u>=WIDTH):
                        placed=True
                        break
                    nextBlock=self.arrange[relpos[0]+u][relpos[1]]
                    if(nextBlock.ship==True):
                        placed=True
                        break
                if(placed==False):
                    temp=[]
                    for j in range(SHIPS[i]):
                        self.arrange[relpos[0]+j][relpos[1]].placeShip(True)
                        temp.append((relpos[0]+j,relpos[1]))
                    self.shipAlive.append(temp)
                    i+=1
            
            else:
                for u in range(SHIPS[i]):
                    if(relpos[1]+u<0 or relpos[1]+u>=LENGTH):
                        placed=True
                        break
                    nextBlock=self.arrange[relpos[0]][relpos[1]+u]
                    if(nextBlock.ship==True):
                        placed=True
                        break
                if(placed==False):
                    temp=[]
                    for j in range(SHIPS[i]):
                        self.arrange[relpos[0]][relpos[1]+j].placeShip(True)
                        temp.append((relpos[0]+j,relpos[1]))
                    self.shipAlive.append(temp)
                    i+=1
                
                    


                
            





