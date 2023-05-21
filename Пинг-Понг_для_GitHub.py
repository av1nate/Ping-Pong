import time
from time import time as timer
from pygame import *
from random import randint

bx = 400
by = 400

clock = time.Clock()
FPS = 120

mw = display.set_mode((bx,by))

bc = transform.scale(image.load('i (1).png'),(bx,by))

class GmSp(sprite.Sprite):
    def __init__(self, pimage, px, py, pw, ph, pspeed):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (pw,ph))
        self.pspeed = pspeed
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Play(GmSp):
    def update1(self ):
        global gx
        global gy
        nk = key.get_pressed()
        if nk[K_w] and self.rect.y > 0:
            self.rect.y -= self.pspeed
        if nk[K_s] and self.rect.y < 300:
            self.rect.y += self.pspeed
    def update2(self ):
        global gx
        global gy
        nk = key.get_pressed()
        if nk[K_UP] and self.rect.y > 0:
            self.rect.y -= self.pspeed
        if nk[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.pspeed

# class Ball(GmSp):
#     def update(self):

        

p1 = Play('1625.png',-20,150,100,100,3)
p2 = Play('1625.png',320,150,100,100,3)



gm = True

while gm == True:

    mw.blit(bc,(0,0))
    p1.reset()
    p2.reset()

    p1.update1()
    p2.update2()

    for i in event.get():
        if i.type == QUIT:
            gm =  False  

    display.update()
    clock.tick(FPS)
