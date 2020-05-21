import pygame
import math
import random
import mysql.connector
from sys import exit
s=pygame.display.set_mode([1450,800])
px,py=35,200
p2x,p2y=1050,45
p3x,p3y=1050,360
p4x,p4y=1250,120
p5x,p5y=1250,290
ox,oy=960,200
o2x,o2y=1100,90
o3x,o3y=1100,320
o4x,o4y=1300,160
o5x,o5y=1300,255    
b=pygame.image.load("Courtn2.png").convert()
p1=pygame.image.load("ply.png").convert()
p2=pygame.image.load("ply2.png").convert()
p3=pygame.image.load("ply3.png").convert()
p4=pygame.image.load("ply4.png").convert()
p5=pygame.image.load("ply5.png").convert()
o1=pygame.image.load("opp.png").convert()
o2=pygame.image.load("opp2.png").convert()
o3=pygame.image.load("opp3.png").convert()
o4=pygame.image.load("opp4.png").convert()
o5=pygame.image.load("opp5.png").convert()
def activeplayer(p,x,y):
                s.blit(p,(x,y))
def distance(x1,x2,y1,y2):
        d = ((((x1-y1)**2)+(x2-y2)**2))**0.5
        return d
player="pg"
pchangex=0
pchangey=0    
while running:
        s.fill([30,0,0])
        s.blit(b,(0,0))
        s.blit(p1,(px,py))
        s.blit(p2,(p2x,p2y))
        s.blit(p3,(p3x,p3y))
        s.blit(p4,(p4x,p4y))
        s.blit(p5,(p5x,p5y))
        s.blit(o1,(ox,oy))
        s.blit(o2,(o2x,o2y))
        s.blit(o3,(o3x,o3y))
        s.blit(o4,(o4x,o4y))
        s.blit(o5,(o5x,o5y))

