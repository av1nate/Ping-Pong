import time
from time import time as timer
from pygame import *
from random import randint

bx = 400
by = 400

clock = time.Clock()
FPS = 120

mw = display.set_mode((bx,by))

bc = transform.scale(image.load('i(1).png'),(bx,by))

font.init()
font1 = font.SysFont('Arial',25)
font2 = font.SysFont("Arial",40)

class GmSp(sprite.Sprite):
    def __init__(self, pimage, px, py, pw, ph, pxspeed, pyspeed):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (pw,ph))
        self.pxspeed = pxspeed
        self.pyspeed = pyspeed
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Play(GmSp):
    def update1(self ):
        nk = key.get_pressed()
        if nk[K_w] and self.rect.y > 0:
            self.rect.y -= self.pxspeed
        if nk[K_s] and self.rect.y < 300:
            self.rect.y += self.pxspeed
    def update2(self ):
        nk = key.get_pressed()
        if nk[K_UP] and self.rect.y > 0:
            self.rect.y -= self.pxspeed
        if nk[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.pxspeed

class Ball(GmSp):
    def update(self):
        self.rect.x += self.pxspeed
        self.rect.y += self.pyspeed
        if self.rect.y <= 0:
            self.pyspeed *= -1
        if self.rect.y >= 350:
            self.pyspeed *= -1

    

p1 = Play('1625.png',10,30,20,100,3,0)
p2 = Play('1625.png',370,270,20,100,3,0)

b1 = Ball('ball1.png',175,175,50,50,1,1)

gm = True
f = False

total = 0

while gm == True:

    mw.blit(bc,(0,0))
    p1.reset()
    p2.reset()
    b1.reset()

    tot = font2.render(str(total), True, (145,70,0))
    mw.blit(tot,(190,10))


    if f != True:
        p1.update1()
        p2.update2()
        b1.update() 

        p2t = font1.render('Player 2', True, (145,255,0))
        mw.blit(p2t,(300,10))
        p1t = font1.render('Player 1', True, (145,255,0))
        mw.blit(p1t,(10,365))

        if sprite.collide_rect(b1,p1):
            b1.pxspeed *= -1
            total += 1
        if sprite.collide_rect(b1,p2):
            b1.pxspeed *= -1
            total += 1

    if b1.rect.x >= 350:
        f = True
        p1w = font1.render('Player 1 win', True, (255,145,0))
        mw.blit(p1w,(150,175))
    if b1.rect.x <= 0:
        f = True
        p2w = font1.render('Player 2 win', True, (255,145,0))
        mw.blit(p2w,(150,175))        

    for i in event.get():
        if i.type == QUIT:
            gm =  False  

        

    display.update()
    clock.tick(FPS)
