import pygame
from random import *
from time import *

back = pygame.display.set_mode((1000,500))
game = True
clock = pygame.time.Clock()

fon1 = pygame.transform.scale(pygame.image.load('desert.jpg'),(1000,500))
fon2 = pygame.transform.scale(pygame.image.load('desert.jpg'),(1000,500))
fon3 = pygame.transform.scale(pygame.image.load('desert.jpg'),(1000,500))
x1 =0
start = time()

class Object(pygame.sprite.Sprite):
    def __init__(self,pict,x,y,shir,vys):
        self.image = pygame.transform.scale(pygame.image.load(pict),(shir,vys))
        self.rect = self.image.get_rect()
        self.rect.x =x
        self.rect.y =y
    def ris(self):
        back.blit(self.image,(self.rect.x,self.rect.y))
    def nabeg(self):
        self.ris()
        self.rect.x-=10

hero = Object('druzhinnik.png',200,200,100,80)
hppict = Object('woodenhouse.png', 5,5,75,75)

hpcont = pygame.Rect((85,37,296,33))
hpinfill = pygame.Rect((88,40,290,27))
hpoutfill = pygame.Rect((88,40,290,27))

pygame.font.init()
pointfont = pygame.font.Font(None, 45)
points = 0
stats = 0
hp = 100

gravity = 0
n = 100
mongols = []

while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
    back.blit(fon1, (0+x1,0))
    back.blit(fon2, (-1000+x1,0))
    back.blit(fon3, (1000+x1,0))
    hero.ris()
    hppict.ris()
    pygame.draw.rect(back,(0,0,0),hpcont,5)
    pygame.draw.rect(back,(255,255,255),hpinfill)
    pygame.draw.rect(back,(25,255,0),hpoutfill)
    text_points = pointfont.render(str(stats), True, (255,0,0))
    back.blit(text_points, (hero.rect.x+17, hero.rect.y-30))

    n-=1
    if n == 0:
        y2 = randint(140,450)
        mongol = Object('nomad.png',900,y2,70,70)
        mongols.append(mongol)
        n = 100

    stats = 'Kills:' + str(points)

    time_passed = time()
    speed_new = 0
    if speed_new < 10:
        speed_new = (time_passed - start) // 5

    for m in mongols:
        m.nabeg()
        if pygame.sprite.collide_rect(hero,m):
            mongols.remove(m)
            points+=1
        elif m.rect.x < 150:
            mongols.remove(m)
            hp-=10
            hpoutfill.width -= 29
        m.rect.x -= speed_new

    kn = pygame.key.get_pressed()
    x1-=8

    if kn[pygame.K_s]:
        hero.rect.y+=6
        if hero.rect.y > 380:
            hero.rect.y = 380
    if kn[pygame.K_w]:
        hero.rect.y-=6
        if hero.rect.y < 140:
            hero.rect.y = 140

    if x1 <-1000:
        x1=1000

    if hp <1:
        game = False

    pygame.display.update()
    clock.tick(60)
