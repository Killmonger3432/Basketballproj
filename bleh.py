import pygame
import math
from sys import exit
s=pygame.display.set_mode([1450,800])
activeplayer="pg"
pygame.init()
px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y=35,200,1050,45,1050,360,1250,120,1250,290
l1=pygame.image.load("ply.png").convert()
l2=pygame.image.load("ply2.png").convert()
l3=pygame.image.load("ply3.png").convert()
l4=pygame.image.load("ply4.png").convert()
l5=pygame.image.load("ply5.png").convert()
gply=pygame.sprite.Group()
ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y=960,200,1100,90,1100,320,1300,160,1300,255
def useplayer():
    if activeplayer=="pg":
        gply.add(p2,p3,p4,p5)
        return p1
    elif activeplayer=="sg":
        gply.add(p1,p3,p4,p5)
        return p2
    elif activeplayer=="sf":
        gply.add(p2,p1,p4,p5)
        return p3
    elif activeplayer=="pf":
        gply.add(p2,p3,p1,p5)
        return p4
    elif activeplayer=="c":
        gply.add(p2,p3,p4,p1)
        return p5
    
class player(pygame.sprite.Sprite):
    def __init__(self,imagefile,x,y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.load=pygame.image.load(imagefile).convert()
        self.movex=0
        self.movey=0
        self.rect=self.load.get_rect()
        self.rect.x=x
        self.rect.y=y
    def boundary(self):
        if self.rect.x>=1365:
            self.rect.x=1365
        if self.rect.x<=30:
            self.rect.x=30
        if self.rect.y<=15:
            self.rect.y=15
        if self.rect.y>=390:
            self.rect.y=390
    def collision(self,x):
        if pygame.sprite.spritecollideany(self,x,True):
            self.movex-=300
            self.movey-=300
            print("ya")
    def movement(self,x,y):
        self.movex += x
        self.movey +=y
        player.collision(self,gply)

    def update(self):
        global px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y
        self.rect.x += self.movex
        self.rect.y += self.movey
        player.boundary(self)
        global L
        if activeplayer=="pg":
            px=self.rect.x
            py=self.rect.y
            L=[px,py]
            s.blit(self.load,(px,py))
            s.blit(l2,(p2x,p2y))
            s.blit(l3,(p3x,p3y))
            s.blit(l4,(p4x,p4y))
            s.blit(l5,(p5x,p5y))
        elif activeplayer=="sg":
            p2x=self.rect.x
            p2y=self.rect.y
            L=[p2x,p2y]
            s.blit(self.load,(p2x,p2y))
            s.blit(l1,(px,py))
            s.blit(l3,(p3x,p3y))
            s.blit(l4,(p4x,p4y))
            s.blit(l5,(p5x,p5y))
        elif activeplayer=="sf":
            p3x=self.rect.x
            p3y=self.rect.y
            L=[p3x,p3y]
            s.blit(self.load,(p3x,p3y))
            s.blit(l2,(p2x,p2y))
            s.blit(l1,(px,py))
            s.blit(l4,(p4x,p4y))
            s.blit(l5,(p5x,p5y))
        elif activeplayer=="pf":
            p4x=self.rect.x
            p4y=self.rect.y
            L=[p4x,p4y]
            s.blit(self.load,(p4x,p4y))
            s.blit(l2,(p2x,p2y))
            s.blit(l3,(p3x,p3y))
            s.blit(l1,(px,py))
            s.blit(l5,(p5x,p5y))
        elif activeplayer=="c":
            p5x=self.rect.x
            p5y=self.rect.y
            L=[p5x,p5y]
            s.blit(self.load,(p5x,p5y))
            s.blit(l2,(p2x,p2y))
            s.blit(l3,(p3x,p3y))
            s.blit(l4,(p4x,p4y))
            s.blit(l1,(px,py))
    def collision(self,x):
        if pygame.sprite.spritecollide(self,x,True):
            self.movex=0
            self.movey=0
class opponent(pygame.sprite.Sprite):
        def __init__(self,imagefile,x,y):
            super().__init__()
            pygame.sprite.Sprite.__init__(self)
            self.load=pygame.image.load(imagefile).convert()
            self.movex=0
            self.movey=0
            self.x=x
            self.y=y
        def boundary(self):
            if self.x>=1365:
                self.x=1365
            if self.x<=30:
                self.x=30
            if self.y<=15:
                self.y=15
            if self.y>=390:
                self.y=390
        def defmov(self):
            k=math.dist(L,[self.x,self.y])
            if k<=100:
                self.movex+=15
                self.movey+=15
            else:
                self.movex=0
                self.movey=0
                
        def update(self):
            global o1x,o1y
            self.x+=self.movex
            self.y+=self.movey
            ox=self.x
            oy=self.y
            s.blit(self.load,(ox,oy)) 
RUN=True
pygame.display.set_caption("Basketball Game")    
b=pygame.image.load("Courtn2.png").convert()
icon=pygame.image.load("bb.png").convert()
pygame.display.set_icon(icon)
while RUN:
    s.fill([155,0,0])
    s.blit(b,(0,0))
    p1=player("ply.png",px ,py)
    p2=player("ply2.png",p2x,p2y)    
    p3=player("ply3.png",p3x,p3y)
    p4=player("ply4.png",p4x,p4y)
    p5=player("ply5.png",p5x,p5y)
    o1=opponent("opp.png",ox,oy)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()                                
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:                  
                            player.movement(useplayer(),-40,0)
                    elif event.key == pygame.K_RIGHT or event.key==pygame.K_d:        
                            player.movement(useplayer(),40,0)
                    elif event.key == pygame.K_UP or event.key==pygame.K_w:
                            player.movement(useplayer(),0,-40)
                    elif event.key== pygame.K_DOWN or event.key==pygame.K_s:
                            player.movement(useplayer(),0,40)
                    elif event.key == pygame.K_1:
                            activeplayer="pg"
                    elif event.key == pygame.K_2:
                            activeplayer="sg"
                    elif event.key == pygame.K_3:
                            activeplayer="sf"
                    elif event.key == pygame.K_4:
                            activeplayer="pf"
                    elif event.key == pygame.K_5:
                            activeplayer="c"
                                      
    player.update(useplayer())
    opponent.defmov(o1)
    opponent.update(o1)
    pygame.display.update()
 



