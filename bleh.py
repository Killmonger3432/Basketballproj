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
f1=pygame.image.load("opp.png").convert()
f2=pygame.image.load("opp2.png").convert()
f3=pygame.image.load("opp3.png").convert()
f4=pygame.image.load("opp4.png").convert()
f5=pygame.image.load("opp5.png").convert()
gply=pygame.sprite.Group()
oply=pygame.sprite.Group()
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
    oply.add(o1,o2,o3,o5,o4)
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
    def movement(self,x,y):
        self.movex += x
        self.movey +=y
            
    def defsel(self):
        max=math.dist([self.rect.x,self.rect.y],[ox,oy])
        if math.dist([self.rect.x,self.rect.y],[o2x,o2y])>max:
            return o2
        elif math.dist([self.rect.x,self.rect.y],[o3x,o3y])>max:
            return o3
        elif math.dist([self.rect.x,self.rect.y],[o4x,o4y])>max:
            return o4
        elif math.dist([self.rect.x,self.rect.y],[o5x,o5y])>max:
            return o5
        else:
            return o1
        oply.add(o1,o2,o3,o4,o5)
    def update(self):
        global px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y
        self.rect.x += self.movex
        self.rect.y += self.movey
        player.boundary(self)
        global L
        L = [self.rect.x,self.rect.y]
        
        if activeplayer=="pg":
            px=self.rect.x
            py=self.rect.y
            s.blit(l1,(px,py))
            s.blit(l2,(p2x,p2y))
            s.blit(l3,(p3x,p3y))
            s.blit(l4,(p4x,p4y))
            s.blit(l5,(p5x,p5y))
        elif activeplayer=="sg":
            p2x=self.rect.x
            p2y=self.rect.y
            s.blit(l2,(p2x,p2y))
            s.blit(l1,(px,py))
            s.blit(l3,(p3x,p3y))
            s.blit(l4,(p4x,p4y))
            s.blit(l5,(p5x,p5y))
        elif activeplayer=="sf":
            p3x=self.rect.x
            p3y=self.rect.y
            s.blit(l3,(p3x,p3y))
            s.blit(l2,(p2x,p2y))
            s.blit(l1,(px,py))
            s.blit(l4,(p4x,p4y))
            s.blit(l5,(p5x,p5y))
        elif activeplayer=="pf":
            p4x=self.rect.x
            p4y=self.rect.y
            s.blit(l4,(p4x,p4y))
            s.blit(l2,(p2x,p2y))
            s.blit(l3,(p3x,p3y))
            s.blit(l1,(px,py))
            s.blit(l5,(p5x,p5y))
        elif activeplayer=="c":
            p5x=self.rect.x
            p5y=self.rect.y
            s.blit(l5,(p5x,p5y))
            s.blit(l2,(p2x,p2y))
            s.blit(l3,(p3x,p3y))
            s.blit(l4,(p4x,p4y))
            s.blit(l1,(px,py))            
class opponent(pygame.sprite.Sprite):
        def __init__(self,imagefile,x,y):
            super().__init__()
            pygame.sprite.Sprite.__init__(self)
            self.load=pygame.image.load(imagefile).convert()
            self.rect=self.load.get_rect()
            self.movex=0
            self.movey=0
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
        def defmov(self):
            k=math.dist(L,[self.rect.x,self.rect.y])
            if k<=100:
                self.movex+=15
                self.movey+=15
            else:
                self.movex=0
                self.movey=0
        def update(self):
            self.rect.x+=self.movex
            self.rect.y+=self.movey
            global ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y
            k=player.defsel(useplayer())
            if k==o1:
                oy=self.rect.y
                ox=self.rect.x
                s.blit(f1,(ox,oy))
                s.blit(f2,(o2x,o2y))
                s.blit(f3,(o3x,o3y))
                s.blit(f4,(o4x,o4y))
                s.blit(f5,(o5x,o5y))
            elif k==o2:
                o2y=self.rect.y
                o2x=self.rect.x
                s.blit(f2,(o2x,o2y))
                s.blit(f1,(ox,oy))
                s.blit(f3,(o3x,o3y))
                s.blit(f4,(o4x,o4y))
                s.blit(f5,(o5x,o5y))
            elif k==o3:
                o3y=self.rect.y
                o3x=self.rect.x
                s.blit(f3,(o3x,o3y))
                s.blit(f2,(o2x,o2y))
                s.blit(f1,(ox,oy))
                s.blit(f4,(o4x,o4y))
                s.blit(f5,(o5x,o5y))
            elif k==o4:
                o4y=self.rect.y
                o4x=self.rect.x
                s.blit(f4,(o4x,o4y))
                s.blit(f2,(o2x,o2y))
                s.blit(f3,(o3x,o3y))
                s.blit(f1,(ox,oy))
                s.blit(f5,(o5x,o5y))
            elif k==o5:
                o5y=self.rect.y
                o5x=self.rect.x
                s.blit(f5,(o5x,o5y))
                s.blit(f2,(o2x,o2y))
                s.blit(f3,(o3x,o3y))
                s.blit(f4,(o4x,o4y))
                s.blit(f1,(ox,oy))
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
    o2=opponent("opp2.png",o2x,o2y)
    o3=opponent("opp3.png",o3x,o3y)
    o4=opponent("opp4.png",o4x,o4y)
    o5=opponent("opp5.png",o5x,o5y)
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
    opponent.defmov(player.defsel(useplayer()))
    opponent.update(player.defsel(useplayer()))
    pygame.display.update()
 
