import pygame
import math
import random
import warnings
warnings.filterwarnings("ignore")
from sys import exit
pygame.init()
score=0
pause=False
fontdef=pygame.font.get_fonts()[23]
fontdef2=pygame.font.get_fonts()[3]
fontdef3=pygame.font.get_fonts()[0]
font=pygame.font.SysFont(fontdef,30) 
textcenter = (660,450)
winfont=pygame.font.SysFont(fontdef2,90)
winfont2=pygame.font.SysFont(fontdef3,30)
tfont=pygame.font.SysFont(fontdef3,30)
s=pygame.display.set_mode([1450,800])
wincenter=(570,500)
wincenter2=(568,590)
tcenter=(1180,450)
activeplayer="pg"
pygame.init()
valp=[97,88]
coord=[]
valo=[77,65]
px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y=725,200,1050,40,1050,360,1250,120,1250,290
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
i=True
a=945
b,b2=280,130
count=0
while i:
    if a>1105:
        break
    coord.append([a,b])
    coord.append([a,b2])
    if a==1095:
        a+=5
    elif count>=5:
        a+=20
    else:
        a+=10
    b+=10
    b2-=10
    count+=1
ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y=925,202.5,1100,90,1100,320,1300,160,1300,255
def TP(x,y):
    TP= False
    if y==390:
        TP= True
    elif y==15:
        TP= True
    elif x<=940:
        TP= True
    for i in coord:
        if y<=130:
            if y==i[1] or y == i[1]-5 or y==i[1]+5:
                if x<=i[0]:
                    TP=True
        elif y>=280:
            if y==i[1] or y == i[1]+5:
                if x<=i[0]:
                    TP=True
    if TP==True:
        return True    
    
def activedefender():
    z=player.activecoord(useplayer())
    min=math.dist(z,[ox,oy])
    b=o1
    if math.dist(z,[o2x,o2y])<min:
        min=math.dist(z,[o2x,o2y])
        b=o2
    if math.dist(z,[o3x,o3y])<min:
        min=math.dist(z,[o3x,o3y])
        b=o3
    if math.dist(z,[o4x,o4y])<min:
        min=math.dist(z,[o4x,o4y])
        b=o4
    if math.dist(z,[o5x,o5y])<min:
        min=math.dist(z,[o5x,o5y])
        b=o5
    return b 
def useplayer():
    if activeplayer=="pg":
        gply.empty()
        gply.add(p2,p3,p4,p5)
        return p1
    elif activeplayer=="sg":
        gply.empty()
        gply.add(p1,p3,p4,p5)
        return p2
    elif activeplayer=="sf":
        gply.empty()
        gply.add(p2,p1,p4,p5)
        return p3
    elif activeplayer=="pf":
        gply.empty()
        gply.add(p2,p3,p1,p5)
        return p4
    elif activeplayer=="c":
        gply.empty()
        gply.add(p2,p3,p4,p1)
        return p5
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
            oply.add(self)
        def boundary(self):

            if self.rect.x>=1365:
                self.rect.x=1365
            if self.rect.x<=30:
                self.rect.x=30
            if self.rect.y<=15:
                self.rect.y=15
            if self.rect.y>=390:
                self.rect.y=390
        def move_towards_player(self, player):
            dx=0
            dy=0
            if math.dist([player.rect.x,player.rect.y],[self.rect.x,self.rect.y]) <400:
                dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
                d = math.hypot(dx,dy)
                if d==0:
                    d=1
                dx,dy=dx/d,dy/d
            if math.dist([player.rect.x,player.rect.y],[self.rect.x,self.rect.y])<=25:
                dx=0
                dy=0
            self.rect.x += dx
            self.rect.y += dy
        def update(self):
            self=activedefender()
            opponent.move_towards_player(self,useplayer())
            opponent.boundary(self)
            global ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y
            if self==o1:
                oy=self.rect.y
                ox=self.rect.x
                s.blit(f1,(ox,oy))
                s.blit(f2,(o2x,o2y))
                s.blit(f3,(o3x,o3y))
                s.blit(f4,(o4x,o4y))
                s.blit(f5,(o5x,o5y))
            elif self==o2:
                o2y=self.rect.y
                o2x=self.rect.x
                s.blit(f2,(o2x,o2y))
                s.blit(f1,(ox,oy))
                s.blit(f3,(o3x,o3y))
                s.blit(f4,(o4x,o4y))
                s.blit(f5,(o5x,o5y))
            elif self==o3:
                o3y=self.rect.y
                o3x=self.rect.x
                s.blit(f3,(o3x,o3y))
                s.blit(f2,(o2x,o2y))
                s.blit(f1,(ox,oy))
                s.blit(f4,(o4x,o4y))
                s.blit(f5,(o5x,o5y))
            elif self==o4:
                o4y=self.rect.y
                o4x=self.rect.x
                s.blit(f4,(o4x,o4y))
                s.blit(f2,(o2x,o2y))
                s.blit(f3,(o3x,o3y))
                s.blit(f1,(ox,oy))
                s.blit(f5,(o5x,o5y))
            elif self==o5:
                o5y=self.rect.y
                o5x=self.rect.x
                s.blit(f5,(o5x,o5y))
                s.blit(f2,(o2x,o2y))
                s.blit(f3,(o3x,o3y))
                s.blit(f4,(o4x,o4y))
                s.blit(f1,(ox,oy))
                
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
        self.score=0
    def boundary(self):
        if self.rect.x>=1365:
            self.rect.x=1365
        if self.rect.x<=725:
            self.rect.x=725
        if self.rect.y<=15:
            self.rect.y=15
        if self.rect.y>=390:
            self.rect.y=390
    def activecoord(self):
        if self==p1:
            z=[px,py]
        elif self==p3:
            z=[p3x,p3y]
        elif self==p2:
            z=[p2x,p2y]
        elif self==p4:
            z=[p4x,p4y]
        elif self==p5:
            z=[p5x,p5y]
        return z    
    
    def collide(self,y,x2,y2):
        if pygame.sprite.collide_rect(self,y):
            if self.rect.x <x2:
                self.movex=-20
            elif self.rect.x>x2:
                self.movex=20
            if self.rect.y<y2:
                self.movey=-20
            elif self.rect.y>y2:
                self.movey=20
    
    def movement(self,x,y):
        self.movex += x
        self.movey +=y
        player.collide(self,o1,ox,oy)
        player.collide(self,o2,o2x,o2y)
        player.collide(self,o3,o3x,o3y)
        player.collide(self,o4,o4x,o4y)
        player.collide(self,o5,o5x,o5y)
        if activeplayer=="pg":
            player.collide(self,p2,p2x,p2y)
            player.collide(self,p3,p3x,p3y)
            player.collide(self,p4,p4x,p4y)
            player.collide(self,p5,p5x,p5y)
        elif activeplayer=="sg":
            player.collide(self,p1,px,py)
            player.collide(self,p3,p3x,p3y)
            player.collide(self,p4,p4x,p4y)
            player.collide(self,p5,p5x,p5y)
        elif activeplayer=="sf":
            player.collide(self,p1,px,py)
            player.collide(self,p2,p2x,p2y)
            player.collide(self,p4,p4x,p4y)
            player.collide(self,p5,p5x,p5y)
        elif activeplayer=="pf":
            player.collide(self,p1,px,py)
            player.collide(self,p2,p2x,p2y)
            player.collide(self,p3,p3x,p3y)
            player.collide(self,p5,p5x,p5y)
        else:
            player.collide(self,p1,px,py)
            player.collide(self,p2,p2x,p2y)
            player.collide(self,p3,p3x,p3y)
            player.collide(self,p4,p4x,p4y)
    def shot(self,x,y,opponent):
        shotprob=0
        if TP(player.activecoord(useplayer())[0],player.activecoord(useplayer())[1]):
            self.K=True
        else:
            self.K=False
        if math.dist(player.activecoord(useplayer()),[1331,202.5])<=100:
            dis=10
        elif math.dist(player.activecoord(useplayer()),[1331,202.5])<=200 and math.dist(player.activecoord(useplayer()),[1331,202.5])>100:
            dis=8
        elif math.dist(player.activecoord(useplayer()),[1331,202.5])<=300 and math.dist(player.activecoord(useplayer()),[1331,202.5])>200:
            dis=6
        elif math.dist(player.activecoord(useplayer()),[1331,202.5])<=400 and math.dist(player.activecoord(useplayer()),[1331,202.5])>300:
            dis=4
        elif math.dist(player.activecoord(useplayer()),[1331,202.5])<=550 and math.dist(player.activecoord(useplayer()),[1331,202.5])>400:
            dis=2
        else:
            dis=0
        if self.K:
            if x[1]-y[1]>=20:
                shotprob=8 + random.randint(0,2)
            elif x[1]-y[1]>=15 and x[1]-y[1]<20:
                shotprob=7 + random.randint(0,3)
            elif x[1]-y[1]>=10 and x[1]-y[1]<15:
                shotprob=6 + random.randint(0,4)
            elif x[1]-y[1]>=7 and x[1]-y[1]<10:
                shotprob=5 + random.randint(0,5)
            else:
                shotprob=4+ random.randint(0,6)
        else:
            if x[0]-y[0]>=20:
                shotprob=8 + random.randint(0,2)
            elif x[0]-y[0]>=15 and x[0]-y[0]<20:
                shotprob=7 + random.randint(0,3)
            elif x[0]-y[0]>=10 and x[0]-y[0]<15:
                shotprob=6 + random.randint(0,4)
            elif x[0]-y[0]>=7 and x[0]-y[0]<10:
                shotprob=5 + random.randint(0,5)
            else:
                shotprob=4+ random.randint(0,6)
        if  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])<80:
            blockprob=random.randint(0,1)
            if blockprob==1:
                self.block= True
            else:
                self.block=False
            
            defprob=2
        elif math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])<100 and  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])>=80:
            defprob=4
            blockprob=random.randint(0,3)
            if blockprob==1:
                self.block= True
            else:
                self.block=False
        elif  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])>=100 and  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])<120:
            defprob=6
            blockprob=random.randint(0,9)
            if blockprob==1:
                self.block= True
            else:
                self.block=False
        elif  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])>=120 and  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])<=140:
            self.block = False
            defprob=8
        else:
            self.block = False
            defprob=10
        self.shotchance= shotprob+defprob+dis
    def score(self):
        if self.block==True:
            self.score =0
            self.state="b"
        elif self.shotchance>=20:
            if self.K:
                self.state="3p"
                self.score=3
            else:
                self.score =2
                self.state="2p"
        elif self.shotchance<20:
            self.state="M"
            self.score=0
        global shoot
        shoot= True
        return self.score
    def win(self):
        if score >=21:
            wintext= "YOU WIN"
            winblit = winfont.render(wintext,True, [0,0,0], [155,0,0])
            s.blit(winblit,wincenter)
            wintext2="Exit window to close game"
            winblit2=winfont2.render(wintext2,True,[0,0,0],[155,0,0])
            s.blit(winblit2,wincenter2)
            self.movey=0
            self.movex=0
            return True
    def update(self):
        global px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y
        player.win(self)
        self.rect.x+=self.movex
        self.rect.y+=self.movey
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
RUN=True
pygame.display.set_caption("Swisheroo")    
b=pygame.image.load("Courtn2.png").convert()
icon=pygame.image.load("icon2.jpeg").convert()
pygame.display.set_icon(icon)
shoot= False
start_ticks=pygame.time.get_ticks()
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
    scoretxt="Score is " + str(score)
    text = font.render(scoretxt,True, [0,0,0], [155,0,0])
    s.blit(text,textcenter)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()                                
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:                  
                            player.movement(useplayer(),-20,0)
                    elif event.key == pygame.K_RIGHT or event.key==pygame.K_d:        
                            player.movement(useplayer(),20,0)
                    elif event.key == pygame.K_UP or event.key==pygame.K_w:
                            player.movement(useplayer(),0,-20)
                    elif event.key== pygame.K_DOWN or event.key==pygame.K_s:
                            player.movement(useplayer(),0,20)
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
                    elif event.key == pygame.K_SPACE:
                            if score<21:
                                player.shot(useplayer(),valp,valo,activedefender())
                                score+=player.score(useplayer())
                            else:
                                print()
    if shoot:
        start_ticks=0
    seconds=(pygame.time.get_ticks()-start_ticks)//1000
    if score>=21:
        seconds=24
    tleft="Time Left is : " + str(24-seconds)
    tblit = tfont.render(tleft,True, [0,0,0], [155,0,0])
    s.blit(tblit,tcenter)
    if seconds>24:
        RUN= False                           
    player.update(useplayer())
    opponent.update(o1)
    pygame.display.update()
    if RUN== False:
        pygame.quit()
    



