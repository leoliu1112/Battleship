import pygame, sys
from pygame.locals import *
from constant import *

CONS=constant()

class Block(pygame.sprite.Sprite):
    def __init__(self, rowId, colId, width, height, rePos, status, isShip):
        super().__init__()
        self.rowId=rowId
        self.colId=colId
        self.width=width
        self.height=height
        self.rePos=rePos
        #0是未被炮击，2是炮击中了，1是炮击未中，3是船死了    
        self.status=status
        self.ship=isShip

        self.loadImage()
        self.updateImagePos()

    def updateImagePos(self):
        self.rect=self.image.get_rect()
        self.rect.left=self.rePos[0]+self.width*self.colId
        self.rect.top=self.rePos[1]+self.height*self.rowId

    def update(self):
        if(self.ship):
            self.status=2
        else:
            self.status=1

    def draw(self, surface):
        self.updateImagePos()
        self.loadImage()
        surface.blit(self.image, self.rect)

    def loadImage(self):
        self.image =pygame.image.load(CONS.blockType[self.status])

    def getRect(self):
        return self.rect
    
    def placeShip(self, isShip):
        self.ship=isShip




