#Создай собственный Шутер!

import time
from time import time as timer
from pygame import *
from random import randint

#параметры бг

bx = 400
by = 800

clock = time.Clock()
FPS = 120

mw = display.set_mode((bx,by))

bc = transform.scale(image.load('back4.png'),(bx,by))

#тест величина
tst = 9999

# очки
lost = 0

# Счётчик пропусков (1)
font.init()
font1 = font.SysFont('Arial',25)
font2 = font.SysFont('Arial', 40)

#счёт
global t 

#перезарядка (переменные)

rt = 3
ry = False
sc = 5

# координаты игрока глоб.
global gx
global gy

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
    def update(self ):
        global gx
        global gy
        nk = key.get_pressed()
        if nk[K_a] and self.rect.x > 30:
            self.rect.x -= self.pspeed
        if nk[K_d] and self.rect.x < 350:
            self.rect.x += self.pspeed

    def f(self):
        spb = Bullet('sp32.png',self.rect.x + 5,self.rect.y,10,10,10)
        b.add(spb)


class Enemy(GmSp):
    def update(self):
        global lost
        if self.rect.y < 790:
            self.rect.y += self.pspeed
        elif self.rect.y > 700:
            self.rect.y = 0
            self.rect.x = randint(25,340)
            self.pspeed = randint(1,3)
            lost += 1

class Astra(GmSp):
    def update(self):
        if self.rect.y < 790:
            self.rect.y += self.pspeed
        elif self.rect.y > 700:
            self.rect.y = 0
            self.rect.x = randint(25,340)
            self.pspeed = randint(3,6)

class Bullet(GmSp):
    def update(self):
        self.rect.y -= self.pspeed
        if self.rect.y < 0:
            self.kill()
        

# mixer.init()
# mixer.music.load('space.ogg')
# music.Play()

sp1 = Play('sp21.png', 200,700,20,30,4)

spb = Bullet('sp32.png',0,0,10,10,10)

sp2 = Enemy('sp22.png', randint(25,340), 0, 50, 50, randint(1,3) )
sp3 = Enemy('sp22.png', randint(25,340), 0, 50, 50, randint(1,3) )
sp4 = Enemy('sp22.png', randint(25,340), 0, 50, 50, randint(1,3) )
sp5 = Enemy('sp22.png', randint(25,340), 0, 50, 50, randint(1,3) )
sp6 = Enemy('sp22.png', randint(25,340), 0, 50, 50, randint(1,3) )
sp7 = Enemy('sp22.png', randint(25,340), 0, 50, 50, randint(1,3) )
sp8 = Enemy('sp22.png', randint(25,340), 0, 50, 50, randint(1,3) )

sp9 = Astra('astr1.png', randint(25,340), 0, 120, 25, randint(3,6) )
sp10 = Astra('astr1.png', randint(25,340), 0, 120, 25, randint(3,6) )

ast = sprite.Group()
ms = sprite.Group()
b = sprite.Group()
player = sprite.Group()

ms.add(sp2,sp3,sp4,sp5,sp6,sp7,sp8)
ast.add(sp9,sp10)
player.add(sp1)

gm = True
finish = False

#счёт
t = 0

#HP
HP = 5


while gm == True:
    nk = key.get_pressed()

    mw.blit(bc,(0,0))
    sp1.reset()
    ms.draw(mw)
    b.draw(mw)
    ast.draw(mw)



    if finish != True:
        sp1.update()
        ms.update()
        b.update()
        ast.update()

        spd = sprite.groupcollide(
            player, ast, False, True
        )

        spl = sprite.groupcollide(
            ms, b , True, True
        )

        if spd:
            sp9 = Astra('astr1.png', randint(25,340), 0, 120, 25, randint(3,6) )
            ast.add(sp9)
            HP -= 1

        if spl:
            sp2 = Enemy('sp22.png', randint(25,340), 0, 50, 50, randint(1,3) )
            ms.add(sp2)
            t += 1
        
    if t >= 10:
        win = font2.render('WIN', True, (180, 255, 0))
        mw.blit(win, (150,380))
        finish = True
    if lost >= 15:
        lose = font2.render('LOSE', True, (255,145,0))
        mw.blit(lose, (150,380))
        finish = True
    if HP <= 0:
        lose = font2.render('LOSE', True, (255,145,0))
        died = font1.render('DIE', True, (200,50,0))
        mw.blit(lose, (150,380))
        mw.blit(died,(185,420))
        finish = True


    health = font1.render('HP:' + str(HP), True, (255, 200, 0))
    los = font1.render('LOS:'+ str(lost) + ' (15)', True, (255, 200, 0))
    kll = font1.render('KLL:'+ str(t) + ' (10)', True, (255, 200, 0))
    ammo = font1.render('AMM:'+ str(sc), True, (255, 200 , 0))
    mw.blit(los, (15,740))
    mw.blit(kll, (15, 715))  
    mw.blit(health, (335, 715))
    mw.blit(ammo, (308, 740))

        
    for i in event.get():
        if i.type == QUIT:
            gm =  False  
        
        elif i.type == KEYDOWN:
            if i.key == K_w or i.key == K_SPACE:
                if ry == False:
                    sp1.f()
                    sc -= 1
                if sc <= 0:
                    lt = timer()
                    ry = True     

    if ry == True:
        tt = timer()
        if tt - lt < rt:
            rld = font1.render('(' + str(3 - (tt - lt))  + ')', True, (255, 0, 0))
            mw.blit(rld, (210, 690))
        else:
            sc = 5
            ry = False


            
    display.update()
    clock.tick(FPS)  

