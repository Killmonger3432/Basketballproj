import pygame
import random
import math
import mysql.connector
from sys import exit
from over import *
import warnings
warnings.filterwarnings("ignore")
pygame.init()
def activeopp(): #current opponent with ball
    if offopp=="pg":
        return o1
    elif offopp=="sg":
        return o2
    elif offopp=="sf":
        return o3
    elif offopp=="pf":
        return o4
    elif offopp=="c":
        return o5
def activedefender(): #calculates nearest defender when we have ball
    z=player.activecoord(useplayer())
    b=min(math.dist(z,[oxo,oyo]),math.dist(z,[o2xo,o2yo]),math.dist(z,[o3xo,o3yo]),math.dist(z,[o4xo,o4yo]),math.dist(z,[o5xo,o5yo]))
    if b==math.dist(z,[oxo,oyo]):
        return o1
    elif b==math.dist(z,[o2xo,o2yo]):
        return o2
    elif b==math.dist(z,[o3xo,o3yo]):
        return o3
    elif b==math.dist(z,[o4xo,o4yo]):
        return o4
    else:
        return o5
def activepp(): #calculates nearest player to ball when opponent have ball, meant to help with player shot
    z=opponent.activecoord(activeopp())
    b=min(math.dist(z,[px,py]),math.dist(z,[p2x,p2y]),math.dist(z,[p3x,p3y]),math.dist(z,[p4x,p4y]),math.dist(z,[p5x,p5y]))
    if b==math.dist(z,[px,py]):
        return p1
    elif b==math.dist(z,[p2x,p2y]):
        return p2
    elif b==math.dist(z,[p3x,p3y]):
        return p3
    elif b==math.dist(z,[p4x,p4y]):
        return p4
    else:
        return p5
def curopp(): #returns nearest player
    if activepp()==p1:
        return "pg"
    elif activepp()==p2:
        return "sg"
    elif activepp()==p3:
        return "sf"
    elif activepp()==p4:
        return "pf"
    elif activepp()==p5:
        return "c"
def plah(): #returns nearest defender when we have ball
    if activedefender()==o1:
        return "pg"
    elif activedefender()==o2:
        return "sg"
    elif activedefender()==o3:
        return "sf"
    elif activedefender()==o4:
        return "pf"
    elif activedefender()==o5:
        return "c"
def curplayer(): #returns current player when they have ball
    if defplayer=="pg":
        return p1
    elif defplayer=="sg":
        return p2
    elif defplayer=="sf":
        return p3
    elif defplayer=="pf":
        return p4
    elif defplayer=="c":
        return p5
def useplayer(): #returns current player when we have ball
    if activeplayer=="pg":
        return p1
    elif activeplayer=="sg":
        return p2
    elif activeplayer=="sf":
        return p3
    elif activeplayer=="pf":
        return p4
    elif activeplayer=="c":
        return p5
def collside(x1,x2,y1,y2): #what happens when 2 opp collide
    global h1,L1,h2
    if x1>y1:
        if x2>y2:
            h1=1
            L1=1
            h2=-1
        else:
            h1=-1
            L1=1
            h2=1
    elif x1<y1:
        if x2>y2:
            h1=1
            L1=-1
            h2=1
        elif x2<y2:
            h1=-1
            L1=-1
            h2=1
        else:
            h2=-1
    else:
        if x2>y2:
            h1=1
            L1=1
        else:
            h1=-1
            L1=-1
    return [h1,L1]    
def nonpcollide(): #detecting collision bw two opp
    global ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y
    global px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y        
    
    if pygame.sprite.collide_rect(o1,o2):
        oy+=collside(ox,oy,o2x,o2y)[0]
        ox+=collside(ox,oy,o2x,o2y)[1]
    if pygame.sprite.collide_rect(o1,o3):
        oy+=collside(ox,oy,o3x,o3y)[0]
        ox+=collside(ox,oy,o3x,o3y)[1]
    if pygame.sprite.collide_rect(o1,o4):
        oy+=collside(ox,oy,o4x,o4y)[0]
        ox+=collside(ox,oy,o4x,o4y)[1]
    if pygame.sprite.collide_rect(o1,o5):
        oy+=collside(ox,oy,o5x,o5y)[0]
        ox+=collside(ox,oy,o5x,o5y)[1]
    if pygame.sprite.collide_rect(o3,o2):
        o3y+=collside(o3x,o3y,o2x,o2y)[0]
        o3x+=collside(o3x,o3y,o2x,o2y)[1] 
    if pygame.sprite.collide_rect(o4,o2):
        o4y+=collside(o4x,o4y,o2x,o2y)[0]
        o4x+=collside(o4x,o4y,o2x,o2y)[1]
    if pygame.sprite.collide_rect(o5,o2):
        o5y+=collside(o5x,o5y,o2x,o2y)[0]
        o5x+=collside(o5x,o5y,o2x,o2y)[1] 
    if pygame.sprite.collide_rect(o3,o4):
        o3y+=collside(o3x,o3y,o4x,o4y)[0]
        o3x+=collside(o3x,o3y,o4x,o4y)[1] 
    if pygame.sprite.collide_rect(o4,o5):
        o4y+=collside(o4x,o4y,o5x,o5y)[0]
        o4x+=collside(o4x,o4y,o5x,o5y)[1]
    if pygame.sprite.collide_rect(o3,o5):
        o3y+=collside(o3x,o3y,o5x,o5y)[0]
        o3x+=collside(o3x,o3y,o5x,o5y)[1]
    if pygame.sprite.collide_rect(o1,p1):
        oy+=collside(ox,oy,px,py)[0]
        ox+=collside(ox,oy,px,py)[1]
    if pygame.sprite.collide_rect(o1,p2):
        oy+=collside(ox,oy,p2x,p2y)[0]
        ox+=collside(ox,oy,p2x,p2y)[1]
    if pygame.sprite.collide_rect(o1,p3):
        oy+=collside(ox,oy,p3x,p3y)[0]
        ox+=collside(ox,oy,p3x,p3y)[1]
    if pygame.sprite.collide_rect(o1,p4):
        oy+=collside(ox,oy,p4x,p4y)[0]
        ox+=collside(ox,oy,p4x,p4y)[1]
    if pygame.sprite.collide_rect(o1,p5):
        oy+=collside(ox,oy,p2x,p2y)[0]
        ox+=collside(ox,oy,p2x,p2y)[1]
    if pygame.sprite.collide_rect(o2,p1):
        o2y+=collside(o2x,o2y,px,py)[0]
        o2x+=collside(o2x,o2y,px,py)[1]
    if pygame.sprite.collide_rect(o2,p2):
        o2y+=collside(o2x,o2y,p2x,p2y)[0]
        o2x+=collside(o2x,o2y,p2x,p2y)[1]
    if pygame.sprite.collide_rect(o2,p3):
        o2y+=collside(o2x,o2y,p3x,p3y)[0]
        o2x+=collside(o2x,o2y,p3x,p3y)[1]
    if pygame.sprite.collide_rect(o2,p4):
        o2y+=collside(o2x,o2y,p4x,p4y)[0]
        o2x+=collside(o2x,o2y,p4x,p4y)[1]
    if pygame.sprite.collide_rect(o2,p5):
        o2y+=collside(o2x,o2y,p5x,p5y)[0]
        o2x+=collside(o2x,o2y,p5x,p5y)[1]
    if pygame.sprite.collide_rect(o3,p1):
        o3y+=collside(o3x,o3y,px,py)[0]
        o3x+=collside(o3x,o3y,px,py)[1]
    if pygame.sprite.collide_rect(o3,p2):
        o3y+=collside(o3x,o3y,p2x,p2y)[0]
        o3x+=collside(o3x,o3y,p2x,p2y)[1]
    if pygame.sprite.collide_rect(o3,p3):
        o3y+=collside(o3x,o3y,p3x,p3y)[0]
        o3x+=collside(o3x,o3y,p3x,p3y)[1]
    if pygame.sprite.collide_rect(o3,p4):
        o3y+=collside(o3x,o3y,p4x,p4y)[0]
        o3x+=collside(o3x,o3y,p4x,p4y)[1]
    if pygame.sprite.collide_rect(o3,p5):
        o3y+=collside(o5x,o5y,p5x,p5y)[0]
        o3x+=collside(o5x,o5y,p5x,p5y)[1]
    if pygame.sprite.collide_rect(o4,p1):
        o4y+=collside(o4x,o4y,px,py)[0]
        o4x+=collside(o4x,o4y,px,py)[1]
    if pygame.sprite.collide_rect(o4,p2):
        o4y+=collside(o4x,o4y,p2x,p2y)[0]
        o4x+=collside(o4x,o4y,p2x,p2y)[1]
    if pygame.sprite.collide_rect(o4,p3):
        o4y+=collside(o4x,o4y,p3x,p3y)[0]
        o4x+=collside(o4x,o4y,p3x,p3y)[1]
    if pygame.sprite.collide_rect(o4,p4):
        o4y+=collside(o4x,o4y,p4x,p4y)[0]
        o4x+=collside(o4x,o4y,p4x,p4y)[1]
    if pygame.sprite.collide_rect(o4,p5):
        o4y+=collside(o4x,o4y,p5x,p5y)[0]
        o4x+=collside(o4x,o4y,p5x,p5y)[1]
    if pygame.sprite.collide_rect(o5,p1):
        o5y+=collside(o5x,o5y,px,py)[0]
        o5x+=collside(o5x,o5y,px,py)[1]
    if pygame.sprite.collide_rect(o5,p2):
        o5y+=collside(o5x,o5y,p2x,p2y)[0]
        o5x+=collside(o5x,o5y,p2x,p2y)[1]
    if pygame.sprite.collide_rect(o5,p3):
        o5y+=collside(o5x,o5y,p3x,p3y)[0]
        o5x+=collside(o5x,o5y,p3x,p3y)[1]
    if pygame.sprite.collide_rect(o5,p4):
        o5y+=collside(o5x,o5y,p4x,p4y)[0]
        o5x+=collside(o5x,o5y,p4x,p4y)[1]
    if pygame.sprite.collide_rect(o5,p5):
        o5y+=collside(o5x,o5y,p5x,p5y)[0]
        o5x+=collside(o5x,o5y,p5x,p5y)[1]

class opponent(pygame.sprite.Sprite):
        def __init__(self,imagefile,x,y,xo,yo):
            super().__init__()
            pygame.sprite.Sprite.__init__(self)
            self.load=pygame.image.load(imagefile).convert()
            self.rect=self.load.get_rect()
            self.movex=0
            self.movey=0
            if status=="OFFENSE":
                self.rect.x=xo
                self.rect.y=yo
            elif status=="DEFENSE":
                self.rect.x=x
                self.rect.y=y
                
            self.Z= 0
            self.shotprob,self.dis,self.defprob=0,0,0
        def boundaryD(self): #boundary on defense
                if self.rect.x>=675:
                    self.rect.x=675
                if self.rect.x<=30:
                    self.rect.x=30
                if self.rect.y<=15:
                    self.rect.y=15
                if self.rect.y>=390:
                    self.rect.y=390
        def boundaryO(self): #boundary on offense
            if self.rect.x>=1365:
                self.rect.x=1365
            if self.rect.x<=725:
                self.rect.x=725
            if self.rect.y<=15:
                self.rect.y=15
            if self.rect.y>=390:
                self.rect.y=390
        def oppmove(self): #moves opponent on offense
            global ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y
            global fin
            hoopdis=math.dist([self.rect.x,self.rect.y],[65,202.5])
            if a1==1:
                ax,ay=405,80
                bx,by=85,15
                cx,cy=405,330
                dx,dy=330,200
                ex,ey=115,300
                a2x,a2y=310,250
                b2x,b2y=405,320
                c2x,c2y=85,390
                d2x,d2y=85,280
                e2x,e2y=185,155
            elif a1==2:
                ax,ay=400,330
                bx,by=400,80
                cx,cy=85,390
                dx,dy=105,120
                ex,ey=330,200
                a2x,a2y=305,160
                b2x,b2y=90,15
                c2x,c2y=400,80
                d2x,d2y=150,250
                e2x,e2y=90,120
            elif a1==3:
                ax,ay=85,390
                bx,by=85,20
                cx,cy=450,120
                dx,dy=270,280
                ex,ey=270,130
                a2x,a2y=85,330
                b2x,b2y=85,80
                c2x,c2y=330,200
                d2x,d2y=270,300
                e2x,e2y=270,110
            elif a1==4:
                ax,ay=85,20
                bx,by=465,200
                cx,cy=85,390
                dx,dy=240,280
                ex,ey=240,130
                a2x,a2y=85,80
                b2x,b2y=330,200
                c2x,c2y=85,330
                d2x,d2y=270,300
                e2x,e2y=270,110
                
            elif a1==5:
                ax,ay=185,300
                bx,by=130,100
                cx,cy=70,390
                dx,dy=390,80
                ex,ey=310,150
                a2x,a2y=325,220
                b2x,b2y=450,120
                c2x,c2y=270,30
                d2x,d2y=230,120
                e2x,e2y=130,250
            elif a1==6:
                ax,ay=205,120
                bx,by=90,15
                cx,cy=150,310
                dx,dy=310,240
                ex,ey=390,330
                a2x,a2y=325,180
                b2x,b2y=290,20
                c2x,c2y=390,340
                d2x,d2y=130,160
                e2x,e2y=230,290
            elif a1==7:
                ax,ay=160,390
                bx,by=250,120
                cx,cy=250,290
                dx,dy=110,15
                ex,ey=110,390
                a2x,a2y=265,390
                b2x,b2y=110,290
                c2x,c2y=110,110
                d2x,d2y=310,110
                e2x,e2y=310,290
            elif a1==8:
                ax,ay=160,20
                bx,by=250,120
                cx,cy=250,290
                dx,dy=110,15
                ex,ey=110,390
                a2x,a2y=265,15
                b2x,b2y=110,110
                c2x,c2y=110,290
                d2x,d2y=290,290
                e2x,e2y=290,110
            elif a1==9:
                ax,ay=305,280
                bx,by=85,390
                cx,cy=310,15
                dx,dy=390,200
                ex,ey=130,150
                a2x,a2y=125,320
                b2x,b2y=270,390
                c2x,c2y=465,195
                d2x,d2y=290,110
                e2x,e2y=90,90
            elif a1==10:
                ax,ay=305,120
                bx,by=350,390
                cx,cy=90,15
                dx,dy=150,250
                ex,ey=390,210
                a2x,a2y=145,80
                b2x,b2y=470,210
                c2x,c2y=305,15
                d2x,d2y=90,310
                e2x,e2y=310,290
            step=max(abs(ax-ox),abs(ay-oy))
            step2=max(abs(bx-o2x),abs(by-o2y))
            step3=max(abs(cx-o3x),abs(cy-o3y))
            step4=max(abs(dx-o4x),abs(dy-o4y))
            step5=max(abs(ex-o5x),abs(ey-o5y))
            step6=max(abs(a2x-ox),abs(a2y-oy))
            step7=max(abs(b2x-o2x),abs(b2y-o2y))
            step8=max(abs(c2x-o3x),abs(c2y-o3y))
            step9=max(abs(d2x-o4x),abs(d2y-o4y))
            step10=max(abs(e2x-o5x),abs(e2y-o5y))
            if fin==True:
                if math.dist([a2x,a2y],[ox,oy])<=3:
                    ox=a2x
                    oy=a2y
                    if math.dist([b2x,b2y],[o2x,o2y])<=3:
                        o2x=b2x
                        o2y=b2y
                        if math.dist([c2x,c2y],[o3x,o3y])<=3:
                            o3x=c2x
                            o3y=c2y
                            if math.dist([d2x,d2y],[o4x,o4y])<=3:
                                o4x=d2x
                                o4y=d2y
                                if math.dist([e2x,e2y],[o5x,o5y])<=3:
                                    o5x=e2x
                                    o5y=e2y
                                else:
                                    o5x+=((e2x-o5x)/step10)*1.2
                                    o5y+=((e2y-o5y)/step10)*1.2
                            else:
                                o4x+=((d2x-o4x)/step9)*1.2
                                o4y+=((d2y-o4y)/step9)*1.2
                        else:
                            o3x+=((c2x-o3x)/step8)*1.2
                            o3y+=((c2y-o3y)/step8)*1.2
                    else:
                        o2x+=((b2x-o2x)/step7)*1.2
                        o2y+=((b2y-o2y)/step7)*1.2
                else:
                    ox+=((a2x-ox)/step6)*1.2
                    oy+=((a2y-oy)/step6)*1.2
            else:
                if math.dist([ax,ay],[ox,oy])<=3:
                    ox=ax
                    oy=ay
                    if math.dist([bx,by],[o2x,o2y])<=3:
                        o2x=bx
                        o2y=by
                        if math.dist([cx,cy],[o3x,o3y])<=3:
                            o3x=cx
                            o3y=cy
                            if math.dist([dx,dy],[o4x,o4y])<=3:
                                o4x=dx
                                o4y=dy
                                if math.dist([ex,ey],[o5x,o5y])<=3:
                                    o5x=ex
                                    o5y=ey
                                    fin=True
                                else:
                                    o5x+=((ex-o5x)/step5)*1.2
                                    o5y+=((ey-o5y)/step5)*1.2
                            else:
                                o4x+=((dx-o4x)/step4)*1.2
                                o4y+=((dy-o4y)/step4)*1.2
                        else:
                            o3x+=((cx-o3x)/step3)*1.2
                            o3y+=((cy-o3y)/step3)*1.2
                    else:
                        o2x+=((bx-o2x)/step2)*1.2
                        o2y+=((by-o2y)/step2)*1.2
                else:
                    ox+=((ax-ox)/step)*1.2
                    oy+=((ay-oy)/step)*1.2
        def move_towards_player(self): #moves opponent on defense
            global oxo,oyo,o2xo,o2yo,o3xo,o3yo,o4xo,o4yo,o5xo,o5yo
            dx=0
            dy=0
            if math.dist(player.activecoord(useplayer()),opponent.activecoord(activedefender())) <400:
                step=max(abs(player.activecoord(useplayer())[0]-opponent.activecoord(activedefender())[0]),abs(player.activecoord(useplayer())[1]-opponent.activecoord(activedefender())[1]))
                dx+=float(player.activecoord(useplayer())[0]-opponent.activecoord(activedefender())[0])/step
                dy+=float(player.activecoord(useplayer())[1]-opponent.activecoord(activedefender())[1])/step
            if math.dist(player.activecoord(useplayer()),opponent.activecoord(activedefender()))<=25:
                dx=0
                dy=0
            if plah()=="pg":
                oxo += (dx/2) 
                oyo += (dy/2)
            if plah()=="sg":
                o2xo += (dx/3) 
                o2yo += (dy/3)
            if plah()=="sf":
                o3xo += (dx/3) 
                o3yo += (dy/3)
            if plah()=="pf":
                o4xo += (dx/3) 
                o4yo += (dy/3)
            if plah()=="c":
                o5xo += (dx/3) 
                o5yo += (dy/3)
        def activecoord(x): #returns coordinate of current opponent
            if status=="DEFENSE":
                if x==o1:
                    z=[ox,oy]
                elif x==o3:
                    z=[o3x,o3y]
                elif x==o2:
                    z=[o2x,o2y]
                elif x==o4:
                    z=[o4x,o4y]
                elif x==o5:
                    z=[o5x,o5y]
                return z
            elif status=="OFFENSE":
                if x==o1:
                    z=[oxo,oyo]
                elif x==o3:
                    z=[o3xo,o3yo]
                elif x==o2:
                    z=[o2xo,o2yo]
                elif x==o4:
                    z=[o4xo,o4yo]
                elif x==o5:
                    z=[o5xo,o5yo]
                return z
        def opppass(self): #opponent passing on offense
                global offopp,movement
                pos1=zpr[0]
                pos2=zpr[1]
                pos3=zpr[2]
                pos4=zpr[3]
                pos5=zpr[4]
                dis1=math.dist(opponent.activecoord(self),pos1)
                dis2=math.dist(opponent.activecoord(self),pos2)
                dis3=math.dist(opponent.activecoord(self),pos3)
                dis4=math.dist(opponent.activecoord(self),pos4)
                dis5=math.dist(opponent.activecoord(self),pos5)
                dislist=[dis1,dis2,dis3,dis4,dis5]
                dislist.sort()
                if dislist[1]==dis1:
                    prob1="pg"
                    moveloc=[ox,oy]
                if dislist[2]==dis1:
                    prob2="pg"
                    moveloc2=[ox,oy]
                if dislist[1]==dis2:
                    prob1="sg"
                    moveloc=[o2x,o2y]
                if dislist[2]==dis2:
                    prob2="sg"
                    moveloc2=[o2x,o2y]
                if dislist[1]==dis3:
                    prob1="sf"
                    moveloc=[o3x,o3y]
                if dislist[2]==dis3:
                    prob2="sf"
                    moveloc2=[o3x,o3y]
                if dislist[1]==dis4:
                    prob1="pf"
                    moveloc=[o4x,o4y]
                if dislist[2]==dis4:
                    prob2="pf"
                    moveloc2=[o4x,o4y]
                if dislist[1]==dis5:
                    prob1="c"
                    moveloc=[o5x,o5y]
                if dislist[2]==dis5:
                    prob2="c"
                    moveloc2=[o5x,o5y]
                pprob=random.randint(1,10)
                if shoot==False:
                    if coll==False:
                        if pprob in range(1,7):
                            offopp=prob1
                            moveball=moveloc
                        else:
                            offopp=prob2
                            moveball=moveloc2
                            
                        if offopp=="pg":
                            ball.movement(b1,ox,oy)
                        elif offopp=="sg":
                            ball.movement(b1,o2x,o2y)
                        elif offopp=="sf":
                            ball.movement(b1,o3x,o3y)
                        elif offopp=="pf":
                            ball.movement(b1,o4x,o4y)
                        elif offopp=="c":
                            ball.movement(b1,o5x,o5y)
                        movement=False
        def shot2(self,x,y): #calculates when to shoot
            if TPD(opponent.activecoord(self)[0],opponent.activecoord(self)[1]):
                self.K=True
            else:
                self.K=False
            
            if math.dist(opponent.activecoord(self),[65,202.5])<=100:
                self.dis=10
            elif math.dist(opponent.activecoord(self),[65,202.5])<=200 and math.dist(opponent.activecoord(self),[65,202.5])>100:
                self.dis=8
            elif math.dist(opponent.activecoord(self),[65,202.5])<=300 and math.dist(opponent.activecoord(self),[65,202.5])>200:
                self.dis=6
            elif math.dist(opponent.activecoord(self),[65,202.5])<=400 and math.dist(opponent.activecoord(self),[65,202.5])>300:
                self.dis=4
            elif math.dist(opponent.activecoord(self),[65,202.5])<=550 and math.dist(opponent.activecoord(self),[65,202.5])>400:
                self.dis=2
            else:
                self.dis=0
            if self.K:
                if x[1]-y[1]>=20:
                    self.shotprob=8 + random.randint(0,2)
                elif x[1]-y[1]>=15 and x[1]-y[1]<20:
                    self.shotprob=7 + random.randint(0,3)
                elif x[1]-y[1]>=10 and x[1]-y[1]<15:
                    self.shotprob=6 + random.randint(0,4)
                elif x[1]-y[1]>=7 and x[1]-y[1]<10:
                    self.shotprob=5 + random.randint(0,5)
                else:
                    self.shotprob=2+ random.randint(0,8)
            else:
                if x[0]-y[0]>=20:
                    self.shotprob=8 + random.randint(0,2)
                elif x[0]-y[0]>=15 and x[0]-y[0]<20:
                    self.shotprob=7 + random.randint(0,3)
                elif x[0]-y[0]>=10 and x[0]-y[0]<15:
                    self.shotprob=6 + random.randint(0,4)
                elif x[0]-y[0]>=7 and x[0]-y[0]<10:
                    self.shotprob=5 + random.randint(0,5)
                else:
                    self.shotprob=2+ random.randint(0,8)
            if  math.dist(opponent.activecoord(activeopp()),player.activecoord(curplayer()))<80:
                self.defprob=random.randint(1,10)
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            blockprob=random.randint(1,2)
                            if blockprob==1:
                                block = True
                            else:
                                block = False 
            elif math.dist(opponent.activecoord(activeopp()),player.activecoord(curplayer()))<100 and  math.dist(opponent.activecoord(self),player.activecoord(curplayer()))>=80:
                    self.defprob=2+random.randint(0,8)
                    for event in pygame.event.get():
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_SPACE:
                                blockprob=random.randint(0,3)
                                if blockprob==1:
                                    block = True
                                else:
                                    block = False
            elif math.dist(opponent.activecoord(self),player.activecoord(curplayer()))>=100 and  math.dist(opponent.activecoord(self),player.activecoord(curplayer()))<120:
                self.defprob=4+random.randint(0,6)
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            blockprob=random.randint(0,9)
                            if blockprob==1:
                                block = True
                            else:
                                block = False
            elif math.dist(opponent.activecoord(self),player.activecoord(curplayer()))>=120 and  math.dist(opponent.activecoord(self),player.activecoord(curplayer()))<140:
                self.defprob=6+random.randint(0,4)
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            block = False
            else:
                self.defprob=8+random.randint(0,2)
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            block = False
            self.Z=self.shotprob+self.defprob+self.dis
                
        def shot(self,x,y): #calculates shot chance
            global RUN
            if TPD(opponent.activecoord(self)[0],opponent.activecoord(self)[1]):
                self.K=True
            else:
                self.K=False
        
            if math.dist(opponent.activecoord(activeopp()),player.activecoord(activepp()))>=150:
                 if self.K:
                     if math.dist(opponent.activecoord(self),[65,202.5])<=450:
                              if x[1]-y[1]>=20:
                                  chance=random.randint(1,100)
                                  if chance == 1:
                                      opponent.shot2(activeopp(),curvalO(),plycurval())
                              elif x[1]-y[1]>=15 and x[1]-y[1]<20:
                                    chance = random.randint(1,200)
                                    if chance == 1:
                                      opponent.shot2(activeopp(),curvalO(),plycurval())
                              elif x[1]-y[1]>=10 and x[1]-y[1]<15:
                                    chance = random.randint(1,300)
                                    if chance == 1:
                                      opponent.shot2(activeopp(),curvalO(),plycurval())
                              elif x[1]-y[1]>=5 and x[1]-y[1]<10:
                                    chance = random.randint(1,400)
                                    if chance == 1:
                                      opponent.shot2(activeopp(),curvalO(),plycurval())
                              else:
                                    chance = random.randint(1,500)
                                    if chance == 1:
                                      opponent.shot2(activeopp(),curvalO(),plycurval())
                    
                 elif self.K==False:
                    if math.dist(opponent.activecoord(self),[65,202.5])<=100:
                        if x[0]-y[0]>=20:
                            chance=random.randint(1,50)
                            if chance ==6:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        elif x[0]-y[0]>=15 and x[0]-y[0]<20:
                            chance=random.randint(1,100)
                            if chance ==5:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        elif x[0]-y[0]>=10 and x[0]-y[0]<15:
                            chance=random.randint(1,150)
                            if chance ==4:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        elif x[0]-y[0]>=5 and x[0]-y[0]<10:
                            chance=random.randint(1,200)
                            if chance ==3:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        else:
                            chance=random.randint(1,250)
                            if chance ==2:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                    elif math.dist(opponent.activecoord(self),[65,202.5])<=200 and math.dist(opponent.activecoord(self),[65,202.5])>100:
                        if x[0]-y[0]>=20:
                            chance=random.randint(1,100)
                            if chance ==5:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        elif x[0]-y[0]>=15 and x[0]-y[0]<20:
                            chance=random.randint(1,200)
                            if chance ==4:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        elif x[0]-y[0]>=10 and x[0]-y[0]<15:
                            chance=random.randint(1,300)
                            if chance ==3:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        elif x[0]-y[0]>=5 and x[0]-y[0]<10:
                            chance=random.randint(1,400)
                            if chance ==2:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        else:
                            chance=random.randint(1,500)
                            if chance ==1:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                    elif math.dist(opponent.activecoord(self),[65,202.5])<=300 and math.dist(opponent.activecoord(self),[65,202.5])>200:
                        if x[0]-y[0]>=20:
                            chance=random.randint(1,150)
                            if chance ==3:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        elif x[0]-y[0]>=15 and x[0]-y[0]<20:
                            chance=random.randint(1,250)
                            if chance ==2:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        elif x[0]-y[0]>=10 and x[0]-y[0]<15:
                            chance=random.randint(1,350)
                            if chance ==2:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        elif x[0]-y[0]>=5 and x[0]-y[0]<10:
                            chance=random.randint(1,450)
                            if chance ==2:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        else:
                            chance=random.randint(1,550)
                            if chance ==1:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                    elif math.dist(opponent.activecoord(self),[65,202.5])<=400 and math.dist(opponent.activecoord(self),[65,202.5])>300:
                        if x[0]-y[0]>=20:
                            chance=random.randint(1,200)
                            if chance ==5:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        elif x[0]-y[0]>=15 and x[0]-y[0]<20:
                            chance=random.randint(1,300)
                            if chance ==2:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        elif x[0]-y[0]>=10 and x[0]-y[0]<15:
                            chance=random.randint(1,400)
                            if chance ==2:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        elif x[0]-y[0]>=7 and x[0]-y[0]<10:
                            chance=random.randint(1,500)
                            if chance ==2:
                                opponent.shot2(activeopp(),curvalO(),plycurval())
                        else:
                            chance=random.randint(1,600)
                            if chance ==1:
                                opponent.shot2(activeopp(),curvalO(),plycurval())

        def score(self): #score increment
            global stat1,RUN,shoot,status,movement,blittime,k1,k2,k3,k4,k5
            if status == 'DEFENSE':
                if shoot==False:
                    if movement==True:
                       opponent.shot(self,curvalO(),plycurval())
                if sec==3:
                    self.Z=random.randint(13,23)
            score=0
            if TPD(opponent.activecoord(self)[0],opponent.activecoord(self)[1]):
                self.K=True
            else:
                self.K=False
            if block==True:
                score =0
                stat1="B"
            
            elif self.Z>0:
                if movement:
                    if coll==False:
                        shoot=True
                        if self.Z>=23:
                            if self.K:
                                score=30
                                stat1='3P'
                            else:
                                score = 2
                                stat1 = '2P'
                        else:
                            stat1="M"
                            score=0
                        if offopp=="pg":
                            k1+=score
                        elif offopp=="sg":
                            k2+=score
                        elif offopp=="sf":
                            k3+=score
                        elif offopp=="pf":
                            k4+=score
                        elif offopp=="c":
                            k5+=score
                        ball.movement(b1,cx,cy)
                        movement=False
                        blittime=pygame.time.get_ticks()+1500
                        

            return score

        def update(self): #opponent updated in loop
            global ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y
            global oxo,oyo,o2xo,o2yo,o3xo,o3yo,o4xo,o4yo,o5xo,o5yo
            if status == 'DEFENSE':
                if notransit:
                    if shoot==False:
                        if coll==False:
                            opponent.oppmove(self)
                    opponent.boundaryD(self)
            elif status == 'OFFENSE':
                self=activedefender()
                if notransit:
                    if shoot==False:
                        if coll==False:
                            opponent.move_towards_player(self)
                    opponent.boundaryO(self)

            if status=="DEFENSE":
                    s.blit(f4,(o4x,o4y))
                    s.blit(f2,(o2x,o2y))
                    s.blit(f3,(o3x,o3y))
                    s.blit(f1,(ox,oy))
                    s.blit(f5,(o5x,o5y))
            elif status=="OFFENSE":
                    s.blit(f1,(oxo,oyo))
                    s.blit(f2,(o2xo,o2yo))
                    s.blit(f3,(o3xo,o3yo))
                    s.blit(f4,(o4xo,o4yo))
                    s.blit(f5,(o5xo,o5yo))
            
                    
                
class player(pygame.sprite.Sprite):
    def __init__(self,imagefile,x,y,xo,yo):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.load=pygame.image.load(imagefile).convert()
        self.movex=0
        self.movey=0
        self.rect=self.load.get_rect()
        if status=="DEFENSE":
            self.rect.x=x
            self.rect.y=y
        if status=="OFFENSE":
            self.rect.x=xo
            self.rect.y=yo
        self.score=0
    def boundaryD(self): #boundary on defense
            global px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y
            if px>=675:
                px=675
            if px<=30:
                px=30
            if py<=15:
                py=15
            if py>=390:
                py=390
            if p2x>=675:
                p2x=675
            if p2x<=30:
                p2x=30
            if p2y<=15:
                p2y=15
            if p2y>=390:
                p2y=390
            if p3x>=675:
                p3x=675
            if p3x<=30:
                p3x=30
            if p3y<=15:
                p3y=15
            if p3y>=390:
                p3y=390
            if p4x>=675:
                p4x=675
            if p4x<=30:
                p4x=30
            if p4y<=15:
                p4y=15
            if p4y>=390:
                p4y=390
            if p5x>=675:
                p5x=675
            if p5x<=30:
                p5x=30
            if p5y<=15:
                p5y=15
            if p5y>=390:
                p5y=390
    def boundaryO(self): #boundary on offense
            global pxo,pyo,p2xo,p2yo,p3xo,p3yo,p4xo,p4yo,p5xo,p5yo
            if pxo>=1365:
                pxo=1365
            if pxo<=725:
                pxo=725
            if pyo<=15:
                pyo=15
            if pyo>=390:
                pyo=390
            if p2xo>=1365:
                p2xo=1365
            if p2xo<=725:
                p2xo=725
            if p2yo<=15:
                p2yo=15
            if p2yo>=390:
                p2yo=390
            if p3xo>=1365:
                p3xo=1365
            if p3xo<=725:
                p3xo=725
            if p3yo<=15:
                p3yo=15
            if p3yo>=390:
                p3yo=390
            if p4xo>=1365:
                p4xo=1365
            if p4xo<=725:
                p4xo=725
            if p4yo<=15:
                p4yo=15
            if p4yo>=390:
                p4yo=390
            if p5xo>=1365:
                p5xo=1365
            if p5xo<=725:
                p5xo=725
            if p5yo<=15:
                p5yo=15
            if p5yo>=390:
                p5yo=390
            
    def collide(self,y,x2,y2): #detects collision
        if pygame.sprite.collide_rect(self,y):
            if self.rect.x <x2:
                self.movex=-20
            elif self.rect.x>x2:
                self.movex=20
            if self.rect.y<y2:
                self.movey=-20
            elif self.rect.y>y2:
                self.movey=20
    def activecoord(self): #returns player coord
        if status=="DEFENSE":
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
        elif status=="OFFENSE":
            if self==p1:
                z=[pxo,pyo]
            elif self==p3:
                z=[p3xo,p3yo]
            elif self==p2:
                z=[p2xo,p2yo]
            elif self==p4:
                z=[p4xo,p4yo]
            elif self==p5:
                z=[p5xo,p5yo]
            return z
    def movement(self,x,y): #player movement+collison handler
        self.movex += x
        self.movey +=y
        if status=="DEFENSE":
            player.collide(self,o1,ox,oy)
            player.collide(self,o2,o2x,o2y)
            player.collide(self,o3,o3x,o3y)
            player.collide(self,o4,o4x,o4y)
            player.collide(self,o5,o5x,o5y)
        elif status=="OFFENSE":
            player.collide(self,o1,oxo,oyo)
            player.collide(self,o2,o2xo,o2yo)
            player.collide(self,o3,o3xo,o3yo)
            player.collide(self,o4,o4xo,o4yo)
            player.collide(self,o5,o5xo,o5yo)
        if status=="DEFENSE":
            if defplayer=="pg":
                player.collide(self,p2,p2x,p2y)
                player.collide(self,p3,p3x,p3y)
                player.collide(self,p4,p4x,p4y)
                player.collide(self,p5,p5x,p5y)
            elif defplayer=="sg":
                player.collide(self,p1,px,py)
                player.collide(self,p3,p3x,p3y)
                player.collide(self,p4,p4x,p4y)
                player.collide(self,p5,p5x,p5y)
            elif defplayer=="sf":
                player.collide(self,p1,px,py)
                player.collide(self,p2,p2x,p2y)
                player.collide(self,p4,p4x,p4y)
                player.collide(self,p5,p5x,p5y)
            elif defplayer=="pf":
                player.collide(self,p1,px,py)
                player.collide(self,p3,p3x,p3y)
                player.collide(self,p2,p2x,p2y)
                player.collide(self,p5,p5x,p5y)
            else:
                player.collide(self,p1,px,py)
                player.collide(self,p3,p3x,p3y)
                player.collide(self,p4,p4x,p4y)
                player.collide(self,p2,p2x,p2y)
        elif status=="OFFENSE":
            if activeplayer=="pg":
                player.collide(self,p2,p2xo,p2yo)
                player.collide(self,p3,p3xo,p3yo)
                player.collide(self,p4,p4xo,p4yo)
                player.collide(self,p5,p5xo,p5yo)
            elif activeplayer=="sg":
                player.collide(self,p1,pxo,pyo)
                player.collide(self,p3,p3xo,p3yo)
                player.collide(self,p4,p4xo,p4yo)
                player.collide(self,p5,p5xo,p5yo)
            elif activeplayer=="sf":
                player.collide(self,p1,pxo,pyo)
                player.collide(self,p2,p2xo,p2yo)
                player.collide(self,p4,p4xo,p4yo)
                player.collide(self,p5,p5xo,p5yo)
            elif activeplayer=="pf":
                player.collide(self,p1,pxo,pyo)
                player.collide(self,p3,p3xo,p3yo)
                player.collide(self,p2,p2xo,p2yo)
                player.collide(self,p5,p5xo,p5yo)
            else:
                player.collide(self,p1,pxo,pyo)
                player.collide(self,p3,p3xo,p3yo)
                player.collide(self,p4,p4xo,p4yo)
                player.collide(self,p2,p2xo,p2yo)
    def shot(self,x,y,opponent): #player shot%
        shotprob=0
        if TPO(player.activecoord(useplayer())[0],player.activecoord(useplayer())[1]):
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
                shotprob=2+ random.randint(0,8)
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
                shotprob=2+ random.randint(0,8)
        if  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])<80:
            blockprob=random.randint(0,1)
            if blockprob==1:
                self.block= True
            else:
                self.block=False
            
            defprob=random.randint(0,10)
        elif math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])<100 and  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])>=80:
            defprob=2+random.randint(0,8)
            blockprob=random.randint(0,3)
            if blockprob==1:
                self.block= True
            else:
                self.block=False
        elif  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])>=100 and  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])<120:
            defprob=4+random.randint(0,6)
            blockprob=random.randint(0,9)
            if blockprob==1:
                self.block= True
            else:
                self.block=False
        elif  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])>=120 and  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])<=140:
            self.block = False
            defprob=6+random.randint(0,4)
        else:
            self.block = False
            defprob=8+random.randint(0,2)
        self.shotchance= shotprob+defprob+dis
    def score(self):#player score increm
        global status,stat1
        if status=="OFFENSE":
            if sec<=3:
                self.shotchance=random.randint(10,25)
            if self.block==True:
                self.score =0
                stat1="B"
            elif self.shotchance>=23:
                if self.K:
                    stat1="3P"
                    self.score=3
                else:
                    self.score =2
                    
                    stat1="2P"
            elif self.shotchance<23:
                stat1="M"
                self.score=0
            notransit= False
        
            return self.score
    def update(self): #player loop update
        global px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y
        global pxo,pyo,p2xo,p2yo,p3xo,p3yo,p4xo,p4yo,p5xo,p5yo
        if status == "DEFENSE":
            if defplayer=="pg":
                px+=self.movex
                py+=self.movey
            elif defplayer=="sg":
                p2x+=self.movex
                p2y+=self.movey
            elif defplayer=="sf":
                p3x+=self.movex
                p3y+=self.movey
            elif defplayer=="pf":
                p4x+=self.movex
                p4y+=self.movey
            elif defplayer=="c":
                p5x+=self.movex
                p5y+=self.movey
            if notransit:
                player.boundaryD(self)
        elif status=="OFFENSE":
            
            if activeplayer=="pg":
                pxo+=self.movex
                pyo+=self.movey
            elif activeplayer=="sg":
                p2xo+=self.movex
                p2yo+=self.movey
            elif activeplayer=="sf":
                p3xo+=self.movex
                p3yo+=self.movey
            elif activeplayer=="pf":
                p4xo+=self.movex
                p4yo+=self.movey
            elif activeplayer=="c":
                p5xo+=self.movex
                p5yo+=self.movey
            if notransit:
                player.boundaryO(self)
        if status=="DEFENSE":
            if notransit:
                pass
            else:
                self.rect.x=player.activecoord(useplayer())[0]
                self.rect.y=player.activecoord(useplayer())[1]
            s.blit(l1,(px,py))
            s.blit(l2,(p2x,p2y))
            s.blit(l3,(p3x,p3y))
            s.blit(l4,(p4x,p4y))
            s.blit(l5,(p5x,p5y))
        elif status=="OFFENSE":
            if notransit:
                pass
            else:
                self.rect.x=player.activecoord(curplayer())[0]
                self.rect.y=player.activecoord(curplayer())[1]
            s.blit(l1,(pxo,pyo))
            s.blit(l2,(p2xo,p2yo))
            s.blit(l3,(p3xo,p3yo))
            s.blit(l4,(p4xo,p4yo))
            s.blit(l5,(p5xo,p5yo))
class ball:
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.rad=10
        self.ballmovex,self.ballmovey=0,0
        self.screen=s
        self.state="P"
        self.number=0
    def boundaryO(self): #ball boundary
        if self.x>=1375:
            self.x=1375
        if self.x<=30:
            self.x=30
        if self.y<=15:
            self.y=15
        if self.y>=390:
            self.y=390
    def boundaryD(self):
            if self.x>=675:
                self.x=675
            if self.x<=30:
                self.x=30
            if self.y<=15:
                self.y=15
            if self.y>=390:
                self.y=390
    def state(self,x): #
        self.state=x
    def state2(self):
        return self.state
    def collision(self,x2,y2): # ball collision with player
        if math.dist((self.x,self.y),(x2,y2))<20:
                self.ballmovex=0
                self.ballmovey=0
                return True
    def collisionb(self,x2,y2): #ball collision with board
        if math.dist([self.x],[x2])<=10:
            if math.dist([self.y],[y2])<=5:
                self.ballmovex=0
                self.ballmovey=0
                return True
    def collisionO(self,x2,y2): #for interception
        if math.dist((self.x,self.y),(x2,y2))<=10:
            self.ballmovex,self.ballmovey=0,0
            return True
    def movement(self,x2,y2): #ball movement
        global disfn
        
        self.number=max(abs(x2-self.x),abs(y2-self.y))
        self.ballmovex=float(x2-self.x)/self.number
        self.ballmovey=float(y2-self.y)/self.number
        self.state="M"
        if shoot==False:
            
            if math.dist((self.x,self.y),(x2,y2))<=100:
                disfn="T1"
            elif math.dist((self.x,self.y),(x2,y2))<=300 and math.dist((self.x,self.y),(x2,y2))>100:
                disfn="T2"
            else:
                disfn="T3"
        else:
            disfn="T0"

    def cor(self): #returns ball coord
        return [self.x,self.y]
    def draw(self): #bll loop update
        global shoot,movement,status,coll,collo,setO,setD,stat1,blittime
        if status=="DEFENSE":
            if shoot == False:
                if notransit==True:
                    if self.state=="M":
                        if ball.collision(self,px,py):
                            self.state="D1"
                            coll=True
                        elif ball.collision(self,p2x,p2y):
                            self.state="D2"
                            coll=True
                        elif ball.collision(self,p3x,p3y):
                            self.state="D3"
                            coll=True
                        elif ball.collision(self,p4x,p4y):
                            self.state="D4"
                            coll=True
                        elif ball.collision(self,p5x,p5y):
                            self.state="D5"
                            coll=True
                    if ball.collision(self,ox,oy) or ball.collision(self,o2x,o2y) or ball.collision(self,o3x,o3y) or ball.collision(self,o4x,o4y)or ball.collision(self,o5x,o5y) :
                        self.state="P"
                        movement=True
                if coll:
                    blittime=pygame.time.get_ticks()+1500
                    stat1="I"
            if ball.collisionb(self,cx,cy):
                setD=True
            if setD==True:
                self.state="D1"
                transition()
                
                
            ball.boundaryD(self)            
            if self.state=="M":
                
                if disfn=="T1":
                    fx=1.5
                elif disfn=="T2":
                    fx=2
                elif disfn=="T0":
                    fx=3
                else:
                    fx=1.5
                self.x+=self.ballmovex*1.5
                self.y+=self.ballmovey*1.5
                
            elif self.state=="P":
                if offopp=="pg":
                    self.x=ox
                    self.y=oy+20
                elif offopp=="sg":
                    self.x=o2x
                    self.y=o2y+20
                elif offopp=="sf":
                    self.x=o3x
                    self.y=o3y+20
                elif offopp=="pf":
                    self.x=o4x
                    self.y=o4y+20
                elif offopp=="c":
                    self.x=o5x
                    self.y=o5y+20
            else:
                if self.state=="D1":
                    self.x=px+50
                    self.y=py+20
                    defplayer="pg"
                elif self.state=="D2":
                    self.x=p2x+50
                    self.y=p2y+20
                    defplayer="sg"
                elif self.state=="D3":
                    self.x=p3x+50
                    self.y=p3y+20
                    defplayer="sf"
                elif self.state=="D4":
                    self.x=p4x+50
                    self.y=p4y+20
                    defplayer="pf"
                elif self.state=="D5":
                    self.x=p5x+50
                    self.y=p5y+20
                    defplayer="c"
                transition()
            
        elif status=="OFFENSE":
            if shoot == False:
                if notransit==True:
                    if self.state=="M":
                        if ball.collision(self,oxo,oyo):
                            self.state="D1"
                            collo=True
                        elif ball.collision(self,o2xo,o2yo):
                            self.state="D2"
                            collo=True
                        elif ball.collision(self,o3xo,o3yo):
                            self.state="D3"
                            collo=True
                        elif ball.collision(self,o4xo,o4yo):
                            self.state="D4"
                            collo=True
                        elif ball.collision(self,o5xo,o5yo):
                            self.state="D5"
                            collo=True
                    if ball.collision(self,pxo,pyo) or ball.collision(self,p2xo,p2yo) or ball.collision(self,p3xo,p3yo) or ball.collision(self,p4xo,p4yo)or ball.collision(self,p5xo,p5yo) :
                        self.state="P"
                if collo==True:
                    blittime=pygame.time.get_ticks()+1500
                    stat1="I"
                    
            if ball.collisionO(self,c2x,c2y):
                setO=True
            if setO==True:
                transition()
                self.x=oxo
                self.y=oyo+20
            ball.boundaryO(self)
            if self.state=="M":
                if disfn=="T1":
                    fx=1.5
                elif disfn=="T2":
                    fx=2
                elif disfn=="T0":
                    fx=3
                else:
                    fx=2
                self.x+=self.ballmovex*fx
                self.y+=self.ballmovey*fx
            elif self.state=="P":
                if activeplayer=="pg":
                    self.x=pxo+50
                    self.y=pyo+20
                elif activeplayer=="sg":
                    self.x=p2xo+50
                    self.y=p2yo+20
                elif activeplayer=="sf":
                    self.x=p3xo+50
                    self.y=p3yo+20
                elif activeplayer=="pf":
                    self.x=p4xo+50
                    self.y=p4yo+20
                elif activeplayer=="c":
                    self.x=p5xo+50
                    self.y=p5yo+20
            else:
                if self.state=="D1":
                    self.x=oxo
                    self.y=oyo
                elif self.state=="D2":
                    self.x=o2xo
                    self.y=o2yo
                elif self.state=="D3":
                    self.x=o3xo
                    self.y=o3yo
                elif self.state=="D4":
                    self.x=o4xo
                    self.y=o4yo
                elif self.state=="D5":
                    self.x=o5xo
                    self.y=o5yo
                transition()
        pygame.draw.circle(s,(255,140,0),[self.x,self.y],self.rad)
def curvalD(): 
    if activedefender()==o1:
        return valo1[3:5]
    elif activedefender()==o2:
        return valo2[3:5]
    elif activedefender()==o3:
        return valo3[3:5]
    elif activedefender()==o4:
        return valo4[3:5]
    elif activedefender()==o5:
        return valo5[3:5]
def curvalO():
    if offopp=='pg':
        return valo1[1:3]
    elif offopp=='sg':
        return valo2[1:3]
    elif offopp=='sf':
        return valo3[1:3]
    elif offopp=='pf':
        return valo4[1:3]
    elif offopp=='c':
        return valo5[1:3]
def plycurval():
    if curopp()=='pg':
        return valp1[3:5]
    elif curopp()=='sg':
        return valp2[3:5]
    elif curopp()=='sf':
        return valp3[3:5]
    elif curopp()=='pf':
        return valp4[3:5]
    elif curopp()=='c':
        return valp5[3:5]
def transition(): #transition bw offesne and defense
    global px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y
    global ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y
    global oxo,oyo,o2xo,o2yo,o3xo,o3yo,o4xo,o4yo,o5xo,o5yo
    global pxo,pyo,p2xo,p2yo,p3xo,p3yo,p4xo,p4yo,p5xo,p5yo
    global status,coll,setO,setD,sec,a1,collo,stat1
    global notransit,shoot,dtime,otime,activeplayer,movement
    
    notransit=False
    if status=="DEFENSE":
        coll=False
        shoot=False
        ax,ay=725,200
        bx,by=1050,40
        cx,cy=1050,360
        dx,dy=1250,120
        ex,ey=1250,290
        fx,fy=925,200
        gx,gy=1100,90
        hx,hy=1100,320
        ix,iy=1300,160
        jx,jy=1300,255
        step1=max(abs(ax-px),abs(ay-py))
        step2=max(abs(bx-p2x),abs(by-p2y))
        step3=max(abs(cx-p3x),abs(cy-p3y))
        step4=max(abs(dx-p4x),abs(dy-p4y))
        step5=max(abs(ex-p5x),abs(ey-p5y))
        step6=max(abs(fx-ox),abs(fy-oy))
        step7=max(abs(gx-o2x),abs(gy-o2y))
        step8=max(abs(hx-o3x),abs(hy-o3y))
        step9=max(abs(ix-o4x),abs(iy-o4y))
        step10=max(abs(jx-o5x),abs(jy-o5y))
        try:
            px+=(ax-px)/step1
            py+=(ay-py)/step1
        except:
            pass
        try:
            p2x+=(bx-p2x)/step2
            p2y+=(by-p2y)/step2
        except:
            pass
        try:
            p3x+=(cx-p3x)/step3
            p3y+=(cy-p3y)/step3
        except:
            pass
        try:
            p4x+=(dx-p4x)/step4
            p4y+=(dy-p4y)/step4
        except:
            pass
        try:
            p5x+=(ex-p5x)/step5
            p5y+=(ey-p5y)/step5
        except:
            pass
        if math.dist([ox,oy],[fx,fy])<=1:
            ox,oy=fx,fy
        else:
            ox+=(fx-ox)/step6
            oy+=(fy-oy)/step6
        if math.dist([o2x,o2y],[gx,gy])<=1:
            o2x,o2y=gx,gy
        else:
            o2x+=(gx-o2x)/step7
            o2y+=(gy-o2y)/step7
        if math.dist([o3x,o3y],[hx,hy])<=1:
            o3x,o3y=hx,hy
        else:
            o3x+=(hx-o3x)/step8
            o3y+=(hy-o3y)/step8

        if math.dist([o4x,o4y],[ix,iy])<=1:
            o4x,o4y=ix,iy
        else:
            o4x+=(ix-o4x)/step9
            o4y+=(iy-o4y)/step9
        if math.dist([o5x,o5y],[jx,jy])<=1:
            o5x,o5y=jx,jy
        else:
            o5x+=(jx-o5x)/step10
            o5y+=(jy-o5y)/step10
        if step1==0 and step2==0 and step3==0 and step4==0 and step5==0 and step6==0 and step7==0 and step8==0 and step9==0 and step10==0:
            coll=False
            setD=False
            notransit=True
            ball.state(B2,"P")
            dtime=0
            movement=True
            activeplayer="pg"
            otime=pygame.time.get_ticks()+21000
            status="OFFENSE"
            px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y=500,200,285,90,285,320,85,160,85,255
            ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y=675,200,365,35,370,370,145,120,145,290
            
            
            
    if status=="OFFENSE":
        sec=5
        collo=False
        shoot=False
        ax,ay=500,200
        bx,by=285,90
        cx,cy=285,320
        dx,dy=85,160
        ex,ey=85,255
        fx,fy=675,200
        gx,gy=365,35
        hx,hy=370,370
        ix,iy=145,120
        jx,jy=145,290
        step1=max(abs(ax-pxo),abs(ay-pyo))
        step2=max(abs(bx-p2xo),abs(by-p2yo))
        step3=max(abs(cx-p3xo),abs(cy-p3yo))
        step4=max(abs(dx-p4xo),abs(dy-p4yo))
        step5=max(abs(ex-p5xo),abs(ey-p5yo))
        step6=max(abs(fx-oxo),abs(fy-oyo))
        step7=max(abs(gx-o2xo),abs(gy-o2yo))
        step8=max(abs(hx-o3xo),abs(hy-o3yo))
        step9=max(abs(ix-o4xo),abs(iy-o4yo))
        step10=max(abs(jx-o5xo),abs(jy-o5yo))
        try:
            pxo+=(ax-pxo)/step1
            pyo+=(ay-pyo)/step1
        except:
            pass
        try:
            p2xo+=(bx-p2xo)/step2
            p2yo+=(by-p2yo)/step2
        except:
            pass
        try:
            p3xo+=(cx-p3xo)/step3
            p3yo+=(cy-p3yo)/step3
        except:
            pass
        try:
            p4xo+=(dx-p4xo)/step4
            p4yo+=(dy-p4yo)/step4
        except:
            pass
        try:
            p5xo+=(ex-p5xo)/step5
            p5yo+=(ey-p5yo)/step5
        except:
            pass
        if math.dist([oxo,oyo],[fx,fy])<=1:
            oxo,oyo=fx,fy
            step6=0
        else:
            oxo+=(fx-oxo)/step6
            oyo+=(fy-oyo)/step6
        if math.dist([o2xo,o2yo],[gx,gy])<=1:
            o2xo,o2yo=gx,gy
            
        else:
            o2xo+=(gx-o2xo)/step7
            o2yo+=(gy-o2yo)/step7
        if math.dist([o3xo,o3yo],[hx,hy])<=1:
            o3xo,o3yo=hx,hy
        else:
            o3xo+=(hx-o3xo)/step8
            o3yo+=(hy-o3yo)/step8

        if math.dist([o4xo,o4yo],[ix,iy])<=1:
            o4xo,o4yo=ix,iy
        else:
            o4xo+=(ix-o4xo)/step9
            o4yo+=(iy-o4yo)/step9
        if math.dist([o5xo,o5yo],[jx,jy])<=1:
            o5xo,o5yo=jx,jy
        else:
            o5xo+=(jx-o5xo)/step10
            o5yo+=(jy-o5yo)/step10
        if step1==0 and step2==0 and step3==0 and step4==0 and step5==0 and step6==0 and step7==0 and step8==0 and step9==0 and step10==0:
            notransit=True
            a1=random.randint(1,10)
            dtime=pygame.time.get_ticks()+21000
            otime=0
            o4x,o5x=o4xo,o5xo
            o4y,o5y=o4yo,o5yo
            o3x,o3y,o2x,o2y,ox,oy=o3xo,o3yo,o2xo,o2yo,oxo,oyo
            defplayer="pg"
            ball.state(b1,"P")
            activeopp="pg"
            setO=False
            stat1="P"
            status="DEFENSE"
            pxo,pyo,p2xo,p2yo,p3xo,p3yo,p4xo,p4yo,p5xo,p5yo=725,200,1050,40,1050,360,1250,120,1250,290
            oxo,oyo,o2xo,o2yo,o3xo,o3yo,o4xo,o4yo,o5xo,o5yo=925,200,1100,90,1100,320,1300,160,1300,255
            

def over(): # after game finisheds
    if scp>=21 or sc>=21:
        abc(s1,s2,s3,s4,s5,k1,k2,k3,k4,k5)
RUN=False
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector
from pil import ImageTk,Image
def draft(): #draft
    root=Tk()
    root.title("Draft")
    root.geometry('800x800')
    width=800
    height=800
    img = Image.open("Courtn2.png")
    width,height=800,800
    img = img.resize((width,height), Image.ANTIALIAS)
    Img =  ImageTk.PhotoImage(img)
    background_label =Label(root, image=Img)
    background_label.Img = Img
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    db=mysql.connector.connect(host='localhost',database='project',user='root',password='Agasthya0112')
    mycur=db.cursor()
    im1 = ImageTk.PhotoImage(Image.open("stephcurry.png"))
    im2 = ImageTk.PhotoImage(Image.open("russelwestbrook.png"))
    im3 = ImageTk.PhotoImage(Image.open("kyrieirving.png"))
    im4 = ImageTk.PhotoImage(Image.open("chrispaul.png"))
    im5 = ImageTk.PhotoImage(Image.open("damianlillard.png"))
    im6 = ImageTk.PhotoImage(Image.open("kembawalker.png"))
    im7 = ImageTk.PhotoImage(Image.open("traeyoung.png"))
    im8 = ImageTk.PhotoImage(Image.open("bensimmons.png"))
    im9 = ImageTk.PhotoImage(Image.open("deaaronfox.png"))
    im10 = ImageTk.PhotoImage(Image.open("kylelowry.png"))
    im11 = ImageTk.PhotoImage(Image.open("jamorant.png"))
    im12=ImageTk.PhotoImage(Image.open("dangelorussel.png"))

    i1 = ImageTk.PhotoImage(Image.open("joelembid.png"))
    i2 = ImageTk.PhotoImage(Image.open("nikolajokic.png"))
    i3 = ImageTk.PhotoImage(Image.open("karlanthonytowns.png"))
    i4 = ImageTk.PhotoImage(Image.open("rudygobert.png"))
    i5 = ImageTk.PhotoImage(Image.open("hassanwhiteside.png"))
    i6 = ImageTk.PhotoImage(Image.open("kristapsporzingis.png"))
    i7 = ImageTk.PhotoImage(Image.open("bamadabeyo.png"))
    i8 = ImageTk.PhotoImage(Image.open("clintcapela.png"))
    i9=ImageTk.PhotoImage(Image.open("nikolavucevic.png"))
    i10=ImageTk.PhotoImage(Image.open("stevenadams.png"))
    i11=ImageTk.PhotoImage(Image.open("andredrummond.png"))
    i12=ImageTk.PhotoImage(Image.open("montrezlharrel.png"))

    a1 = ImageTk.PhotoImage(Image.open('jamesharden.png'))
    a2 = ImageTk.PhotoImage(Image.open("lukadoncic.png"))
    a3 = ImageTk.PhotoImage(Image.open("paulgeorge.png"))
    a4 = ImageTk.PhotoImage(Image.open("bradleybeal.png"))
    a5 = ImageTk.PhotoImage(Image.open("klaythompson.png"))
    a6 = ImageTk.PhotoImage(Image.open("devinbooker.png"))
    a7 = ImageTk.PhotoImage(Image.open("cjmcollum.png"))
    a8 = ImageTk.PhotoImage(Image.open("donovanmitchell.png"))
    a9 = ImageTk.PhotoImage(Image.open("victoroladipo.png"))
    a10 = ImageTk.PhotoImage(Image.open("zachlavine.png"))
    a11 = ImageTk.PhotoImage(Image.open("jaylenbrown.png"))
    a12 = ImageTk.PhotoImage(Image.open("shaigalexander.png"))

    pf1 = ImageTk.PhotoImage(Image.open('gantetokounmpo.png'))
    pf2 = ImageTk.PhotoImage(Image.open("anthonydavis.png"))
    pf3 = ImageTk.PhotoImage(Image.open("pascalsiakam.png"))
    pf4 = ImageTk.PhotoImage(Image.open("jaysontatum.png"))
    pf5 = ImageTk.PhotoImage(Image.open("zionwilliamson.png"))
    pf6 = ImageTk.PhotoImage(Image.open("johncollins.png"))
    pf7 = ImageTk.PhotoImage(Image.open("blakegriffin.png"))
    pf8 = ImageTk.PhotoImage(Image.open("domantassabonis.png"))
    pf9 = ImageTk.PhotoImage(Image.open("danilogallinari.png"))
    pf10 = ImageTk.PhotoImage(Image.open("jarenjacksonjr.png"))
    pf11 = ImageTk.PhotoImage(Image.open("alhorford.png"))
    pf12 = ImageTk.PhotoImage(Image.open("kevinlove.png"))

    ar1 = ImageTk.PhotoImage(Image.open('lebronjames.png'))
    ar2 = ImageTk.PhotoImage(Image.open("kevindurant.png"))
    ar3 = ImageTk.PhotoImage(Image.open("kawhileonard.png"))
    ar4 = ImageTk.PhotoImage(Image.open("jimmybutler.png"))
    ar5 = ImageTk.PhotoImage(Image.open("khrismiddleton.png"))
    ar6 = ImageTk.PhotoImage(Image.open("demarderozan.png"))
    ar7 = ImageTk.PhotoImage(Image.open("brandoningram.png"))
    ar8 = ImageTk.PhotoImage(Image.open("tobiasharris.png"))
    ar9 = ImageTk.PhotoImage(Image.open("gordonhayward.png"))
    ar10 = ImageTk.PhotoImage(Image.open("andrewwiggins.png"))
    ar11 = ImageTk.PhotoImage(Image.open("tjwarren.png"))
    ar12 = ImageTk.PhotoImage(Image.open("jonathanisaac.png"))

    sflist=[ar1,ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9,ar10,ar11,ar12]
    pflist=[pf1,pf2,pf3,pf4,pf5,pf6,pf7,pf8,pf9,pf10,pf11,pf12]
    sglist=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12]
    centerlist=[i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12]
    l3 = [im1, im2, im3, im4, im5, im6, im7, im8, im9, im10, im11,im12]
    x=im1.height()
    y=im1.width()
    sql = "select * from players where position='C' order by Overall desc"
    mycur.execute(sql)
    result = mycur.fetchall()
    l = list(result)
    l4 = []
    for i in range(len(l)):
        l4.append("\'{}\'".format(l[i][1]))
    listc = l4[:12]
    nlist=[]
    sql = "select * from players where position='SG' order by Overall desc"
    mycur.execute(sql)
    result = mycur.fetchall()
    l = list(result)
    l4 = []
    for i in range(len(l)):
        l4.append("\'{}\'".format(l[i][1]))
    listsg = l4[:12]
    nlist=[]
    pos=-1
    def myteam():
        global pos,RUN
        
        new = Toplevel(root)
        new.geometry('1000x900')
        img = Image.open("Courtn2.png")
        width,height=1000,1000
        img = img.resize((width,height), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(new, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        new.title("MY TEAM")
        frame_container = Frame(new)
        
        canvas_container = Canvas(frame_container, height=800, width=1500)
        frame2 = Frame(canvas_container)
        myscrollbar = Scrollbar(frame_container, orient="vertical",
                                command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
        canvas_container.create_window((0, 0), window=frame2, anchor='nw')
        sql="select * from myteam"
        mycur.execute(sql)
        res=mycur.fetchall()
        name=[]
        index=[]
        for i in range(len(res)):
            name.append("\'{}\'".format(res[i][1]))
            index.append("\"{}\"".format(res[i][9]))
        imgs=[]
        l2 = []
        def dele():
            sql="""DELETE FROM myteam where Name = %s"""
            
            if pos==0:
                mycur.execute(sql,(name[0],))
                
            if pos==1:
                mycur.execute(sql,(name[1],))
                
            if pos==2:
                mycur.execute(sql,(name[2],))
                
            if pos==3:
                mycur.execute(sql,(name[3],))
                
            if pos==4:
                mycur.execute(sql,(name[4],))
                
            db.commit()
            messagebox.showinfo("ALERT","This player has been removed,select a new player")
            new.destroy()
            
        def change():
            global pos
            if j.get()==0:
                b2['state']='NORMAL'
                pos=0
            elif j.get()==1:
                b2['state']='NORMAL'
                pos=1
            elif j.get()==2:
                b2['state']='NORMAL'
                pos=2
            elif j.get()==3:
                b2['state']='NORMAL'
                pos=3
            elif j.get()==4:
                b2['state']='NORMAL'
                pos=4
        for i in range(0,len(name)):
            name[i]=name[i].strip("\'")
        for i in index:
            i = i.strip('\"')
            imgs.append(ImageTk.PhotoImage(Image.open(i)))
        j=IntVar()
        for i in range(0,len(index)):
            l2.append(Radiobutton(new,variable=j,value=i,image=imgs[i],state=ACTIVE,command = change))
        
        try:
            l2[0].grid(row=2,column=1)
        except:
            pass
        try:
            l2[1].grid(row=2, column=200)
        except:
            pass
        try:
            l2[2].grid(row=10, column=5)
        except:
            pass
        try:
            l2[3].grid(row=30, column=1)
        except:
            pass
        try:
            l2[4].grid(row=30, column=200)
        except:
            pass
        
        def mainl():
            global RUN
            if len(name)<=4:
                messagebox.showerror("ERROR","You must select 5 players before proceeding")
                new.destroy()
            else:
                messagebox.showerror("READY","By pressing ok you will close the entire draft section and move to game. Music will be queued from this point and you will not be able to change it in-game. Press yes only if you are ready")
                new.destroy()
                root.destroy()
                #pygame.mixer.music.load()
                RUN=True
        
            
            
        frame2.update()
        canvas_container.configure(yscrollcommand=myscrollbar.set, scrollregion="0 0 0 %s" % frame2.winfo_height())
        canvas_container.pack(side=RIGHT)
        myscrollbar.pack(side=RIGHT, fill=Y)
        b1=Button(new,text="Proceed", command=mainl)
        b1.place(x=800,y=150,height=50,width=150)
        b2=Button(new,text="Delete",state="disabled",command=dele)
        b2.place(x=800,y=450,height=50,width=150)
        m=Button(new,text="Music Settings",command=q)
        m.place(x=800,y=750,height=50,width=150)
        frame_container.pack()



    def sg():
        new2=Toplevel(root)
        new2.title("Shooting Guard")
        frame_container = Frame(new2)
        canvas_container = Canvas(frame_container,height=850,width=1300)
        frame2 = Frame(canvas_container)
        myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
        canvas_container.create_window((0, 0), window=frame2, anchor='nw')
        def clicked(value):
            sql2="select * from myteam"
            mycur.execute(sql2)
            res=mycur.fetchall()
            count=0
            for i in res:
                if i[2]=="SG":
                    count+=1
            if count<1:
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image) select * from players where position='SG' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("error", "You already have a Shooting Guard")
            new2.destroy()
        new2.grab_set()
        #new.grab_release()
        r=StringVar()
        bn=-1
        img = Image.open("Courtn2.png")
        img = img.resize((1300,1200), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(frame2, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l2=[]
        for i in range(0,12):
            l2.append(Radiobutton(frame2,variable=r,value=listsg[i],command=lambda : clicked(r.get()),image=sglist[i]))
        l2[0].grid(row=0,column=1)
        l2[1].grid(row=0,column=3)
        l2[2].grid(row=0, column=5)
        l2[3].grid(row=1, column=2)
        l2[4].grid(row=1, column=4)
        l2[5].grid(row=1, column=6)
        l2[6].grid(row=2, column=1)
        l2[7].grid(row=2, column=3)
        l2[8].grid(row=2, column=5)
        l2[9].grid(row=3, column=2)
        l2[10].grid(row=3,column=4)
        l2[11].grid(row=3, column=6)
        
        
        frame2.update()
        canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
        canvas_container.pack(side=RIGHT)
        myscrollbar.pack(side=RIGHT, fill=Y)
        frame_container.pack()

    sql = "select * from players where position = 'PF' order by Overall desc"
    mycur.execute(sql)
    result = mycur.fetchall()
    l = list(result)
    listpf = []
    for i in range(len(l)):
        listpf.append("\'{}\'".format(l[i][1]))
    nlist=[]
    def pf():
        new2=Toplevel(root)
        new2.title("Power Forward")
        frame_container = Frame(new2)
        canvas_container = Canvas(frame_container,height=850,width=1300)
        frame2 = Frame(canvas_container)
        myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
        canvas_container.create_window((0, 0), window=frame2, anchor='nw')
        def clicked(value):
            sql2="select * from myteam"
            mycur.execute(sql2)
            res=mycur.fetchall()
            count=0
            for i in res:
                if i[2]=="PF":
                    count+=1
            if count<1:
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image) select * from players where position='PF' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("error", "You already have a Power Forward")
            new2.destroy()
        new2.grab_set()
        #new.grab_release()
        r=StringVar()
        bn=-1
        img = Image.open("Courtn2.png")
        img = img.resize((1300,1200), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(frame2, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l2=[]
        for i in range(0,12):
            l2.append(Radiobutton(frame2,variable=r,value=listpf[i],command=lambda : clicked(r.get()),image=pflist[i]))
        l2[0].grid(row=0,column=1)
        l2[1].grid(row=0,column=3)
        l2[2].grid(row=0, column=5)
        l2[3].grid(row=1, column=2)
        l2[4].grid(row=1, column=4)
        l2[5].grid(row=1, column=6)
        l2[6].grid(row=2, column=1)
        l2[7].grid(row=2, column=3)
        l2[8].grid(row=2, column=5)
        l2[9].grid(row=3, column=2)
        l2[10].grid(row=3, column=4)
        l2[11].grid(row=3, column=6)
        frame2.update()
        canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
        canvas_container.pack(side=RIGHT)
        myscrollbar.pack(side=RIGHT, fill=Y)
        frame_container.pack()

    def center():
        new2=Toplevel(root)
        new2.title("Center")
        frame_container = Frame(new2)
        canvas_container = Canvas(frame_container,height=850,width=1300)
        frame2 = Frame(canvas_container)
        myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
        canvas_container.create_window((0, 0), window=frame2, anchor='nw')
        def clicked(value):
            sql2="select * from myteam"
            mycur.execute(sql2)
            res=mycur.fetchall()
            count=0
            for i in res:
                if i[2]=="C":
                    count+=1
            if count<1:
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image) select * from players where position='C' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("error", "You already have a Center")
            new2.destroy()

        new2.grab_set()
        r=StringVar()
        bn=-1
        img = Image.open("Courtn2.png")
        img = img.resize((1300,1200), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(frame2, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l2=[]
        for i in range(0,12):
            l2.append(Radiobutton(frame2,variable=r,value=listc[i],command=lambda : clicked(r.get()),image=centerlist[i]))
        l2[0].grid(row=0,column=1)
        l2[1].grid(row=0,column=3)
        l2[2].grid(row=0, column=5)
        l2[3].grid(row=1, column=2)
        l2[4].grid(row=1, column=4)
        l2[5].grid(row=1, column=6)
        l2[6].grid(row=2, column=1)
        l2[7].grid(row=2, column=3)
        l2[8].grid(row=2, column=5)
        l2[9].grid(row=3, column=2)
        l2[10].grid(row=3, column=4)
        l2[11].grid(row=3, column=6)
        frame2.update()
        canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
        canvas_container.pack(side=RIGHT)
        myscrollbar.pack(side=RIGHT, fill=Y)
        frame_container.pack()

    sql = "select * from players where position = 'SF' order by Overall desc"
    mycur.execute(sql)
    result = mycur.fetchall()
    l = list(result)
    l4 = []
    for i in range(len(l)):
        l4.append("\'{}\'".format(l[i][1]))

    listsf = l4[:12]
    nlist=[]
    def sf():
        new2=Toplevel(root)
        new2.title("Small Forward")
        frame_container = Frame(new2)
        canvas_container = Canvas(frame_container,height=850,width=1300)
        frame2 = Frame(canvas_container)
        myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
        canvas_container.create_window((0, 0), window=frame2, anchor='nw')
        def clicked(value):
            sql2="select * from myteam"
            mycur.execute(sql2)
            res=mycur.fetchall()
            count=0
            for i in res:
                if i[2]=="SF":
                    count+=1
            if count<1:
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image) select * from players where position='SF' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("error", "You already have a Small Forward")
            new2.destroy()

        new2.grab_set()
        #new.grab_release()
        r=StringVar()
        bn=-1
        img = Image.open("Courtn2.png")
        img = img.resize((1300,1200), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(frame2, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l2=[]
        for i in range(0,12):
            l2.append(Radiobutton(frame2,variable=r,value=listsf[i],command=lambda : clicked(r.get()),image=sflist[i]))
        l2[0].grid(row=0,column=1)
        l2[1].grid(row=0,column=3)
        l2[2].grid(row=0, column=5)
        l2[3].grid(row=1, column=2)
        l2[4].grid(row=1, column=4)
        l2[5].grid(row=1, column=6)
        l2[6].grid(row=2, column=1)
        l2[7].grid(row=2, column=3)
        l2[8].grid(row=2, column=5)
        l2[9].grid(row=3, column=2)
        l2[10].grid(row=3, column=4)
        l2[11].grid(row=3, column=6)
        
        frame2.update()
        canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
        canvas_container.pack(side=RIGHT)
        myscrollbar.pack(side=RIGHT, fill=Y)
        frame_container.pack()

    sql = "select * from players where position = 'PG' order by Overall desc"
    mycur.execute(sql)
    result = mycur.fetchall()
    l = list(result)
    l4 = []
    for i in range(len(l)):
        l4.append("\'{}\'".format(l[i][1]))

    l5 = l4[:12]
    nlist=[]

    def pg():
        new3=Toplevel(root)
        new3.title("Point Guard")
        frame_container = Frame(new3)
        canvas_container = Canvas(frame_container,height=850,width=1300)
        frame3 = Frame(canvas_container)
        myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)
        canvas_container.create_window((0, 0), window=frame3, anchor='nw')
        def clicked(value):
            sql2="select * from myteam"
            mycur.execute(sql2)
            res=mycur.fetchall()
            count=0
            for i in res:
                if i[2]=="PG":
                    count+=1
            if count<1:
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image) select * from players where position='PG' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("error", "You already have a Point Guard")
            new3.destroy()
        new3.grab_set()
        #new.grab_release()
        r=StringVar()
        bn=-1
        img = Image.open("Courtn2.png")
        img = img.resize((1300,1200), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(frame3, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l2=[]
        for i in range(0,12):
            l2.append(Radiobutton(frame3,variable=r,value=l5[i],command=lambda : clicked(r.get()),image=l3[i]))
        l2[0].grid(row=0,column=1)
        l2[1].grid(row=0,column=3)
        l2[2].grid(row=0, column=5)
        l2[3].grid(row=1, column=2)
        l2[4].grid(row=1, column=4)
        l2[5].grid(row=1, column=6)
        l2[6].grid(row=2, column=1)
        l2[7].grid(row=2, column=3)
        l2[8].grid(row=2, column=5)
        l2[9].grid(row=3, column=2)
        l2[10].grid(row=3, column=4)
        l2[11].grid(row=3, column=6)

        frame3.update()
        canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame3.winfo_height())
        canvas_container.pack(side=RIGHT)
        myscrollbar.pack(side=RIGHT, fill=Y)
        frame_container.pack()
    
    def q():
        
        new=Toplevel(root)
        new.geometry('600x600')
        new.title("Music Settings")
        new.attributes("-topmost", True)
        width,height=600,600
        img = Image.open("Courtn2.png")
        img = img.resize((width,height), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(new, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        z=StringVar()
        i=[("Imperial March - Darth Vader Theme","Imp"),("In The End - Linkin Park","ITE"),("We Are the Champions - Queen","CHA"),("Enter Sandman - Metallica","ENS"),("New Divide - Linkin Park","NEW"),("Teenagers - My Chemical Romance","TEN"),("Welcome to the Black Parade- MCR","TBP"),("Sweet Child O' Mine - Guns N' Roses","SCM"),("Don't Cry - Guns N' Roses","DOC"),("Star Wars Main Theme","STW"),("Papercut - Linkin Park","PAP"),("Rap God - Eminem","RAP"),("Lose Yourself - Eminem","LOY"),("Boulevard of Broken Dreams - Green Day","BBD"),("Jesus of Suburbia - Green Day","JSB"),("Why Do We Fall? - Hanz Zimmer","WDW"),("S.T.A.Y - Hans Zimmer (Interstellar Theme)","INT"),("Humble - Kendrick Lamar","HUM"),("DNA - Kendrick Lamar","DNA"),("Master Of Puppets - Metallica","MOP"),("Smells Like Teen Spirit - Nirvana","SLT"),("Sound of Silence - Simon and Garfunkel","SOS")]                                                                                                                                                                                                                                                                                                
        k=[]
        for y in i:
            m=str(y[1]+str('.mp3'))
            pygame.mixer.music.queue(str(m))
        def play():
            pygame.mixer.music.unload()
            o=str(z.get())+ str('.mp3')
            pygame.mixer.music.load(o)
            pygame.mixer.music.play()
        for r in range(0,len(i)):
            k.append(Radiobutton(new,variable=z,command=play,value=str(i[r][1]),text=str(i[r][0])))
        j=0
        f=11
        while j<=10:
            if j==0:
                k[0].place(x=40,y=50)
            else:
                k[j].place(x=40,y=int(50*(j+1)))
            j+=1
        while f>10 and f<=21:
            k[f].place(x=300,y=int(50*(f-10)))
            f+=1
        messagebox.showinfo("Guide","Click on any radio button to change the song")
    pg=Button(root,text="Choose a Point Guard", command=pg)
    pg.place(x=90,y=90,height=50,width=150)
    center=Button(root,text="Choose a Center",command=center)
    center.place(x=325,y=390,height=50,width=150)
    sg=Button(root,text="Choose a Shooting Guard", command=sg)
    sg.place(x=90,y=700,height=50,width=150)
    sf=Button(root,text="Chose a Small Forward", command=sf)
    sf.place(x=600,y=90,height=50,width=150)
    pf=Button(root,text="Choose a Power Forward", command=pf)
    pf.place(x=600,y=700,height=50,width=150)
    MYTEAM=Button(root,text="Check your team and proceed", command=myteam)
    MYTEAM.place(x=305,y=600,height=75,width=200)
    m=Button(root,text="Music Settings",command=q)
    m.place(x=330,y=200,height=50,width=150)
    root.deiconify()
root=Tk()
root.title("Welcome Page")
root.geometry('1000x1000')
pygame.mixer.music.load("STW.mp3")
pygame.mixer.music.play() 
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo 
def k():
    abox=messagebox.askquestion("Are you ready?","Press Yes to start the draft")
    if abox=="yes": 
        root.destroy()
        draft()
def s():
    abox=messagebox.askquestion("Exit","Press Yes to exit game")
    if abox=="yes":
        root.destroy()
def q():
    
    new=Toplevel(root)
    new.geometry('600x600')
    new.title("Music Settings")
    new.attributes("-topmost", True)
    width,height=600,600
    img = Image.open("Courtn2.png")
    img = img.resize((width,height), Image.ANTIALIAS)
    Img =  ImageTk.PhotoImage(img)
    background_label =Label(new, image=Img)
    background_label.Img = Img
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    z=StringVar()
    i=[("Imperial March - Darth Vader Theme","Imp"),("In The End - Linkin Park","ITE"),("We Are the Champions - Queen","CHA"),("Enter Sandman - Metallica","ENS"),("New Divide - Linkin Park","NEW"),("Teenagers - My Chemical Romance","TEN"),("Welcome to the Black Parade- MCR","TBP"),("Sweet Child O' Mine - Guns N' Roses","SCM"),("Don't Cry - Guns N' Roses","DOC"),("Star Wars Main Theme","STW"),("Papercut - Linkin Park","PAP"),("Rap God - Eminem","RAP"),("Lose Yourself - Eminem","LOY"),("Boulevard of Broken Dreams - Green Day","BBD"),("Jesus of Suburbia - Green Day","JSB"),("Why Do We Fall? - Hanz Zimmer","WDW"),("S.T.A.Y - Hans Zimmer (Interstellar Theme)","INT"),("Humble - Kendrick Lamar","HUM"),("DNA - Kendrick Lamar","DNA"),("Master Of Puppets - Metallica","MOP"),("Smells Like Teen Spirit - Nirvana","SLT"),("Sound of Silence - Simon and Garfunkel","SOS")]                                                                                                                                                                                                                                                                                                
    k=[]
    for y in i:
        m=str(y[1]+str('.mp3'))
        pygame.mixer.music.queue(str(m))
    def play():
        pygame.mixer.music.unload()
        o=str(z.get())+ str('.mp3')
        pygame.mixer.music.load(o)
        pygame.mixer.music.play()
    for r in range(0,len(i)):
        k.append(Radiobutton(new,variable=z,command=play,value=str(i[r][1]),text=str(i[r][0])))
    j=0
    f=11
    while j<=10:
        if j==0:
            k[0].place(x=40,y=50)
        else:
            k[j].place(x=40,y=int(50*(j+1)))
        j+=1
    while f>10 and f<=21:
        k[f].place(x=300,y=int(50*(f-10)))
        f+=1
    messagebox.showinfo("Guide","Click on any radio button to change the song")
image = Image.open('courtn2.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)
a=Button(root,text="BEGIN GAME",command=k)
a.place(x=380,y=500,height=100,width=250)
n=Button(root,text="Quit",command=s)
n.place(x=830,y=40,height=40,width=150)
m=Button(root,text="Music Settings",command=q)
m.place(x=425,y=650,height=50,width=150)
root.mainloop()
RUN2=False
if RUN==True:
    s=pygame.display.set_mode([1450,800])
    pygame.display.set_caption("Swisheroo")    
    COURT=pygame.image.load("Courtn2.png").convert()
    icon=pygame.image.load("icon2.jpeg").convert()
    pygame.display.set_icon(icon)
    con=mysql.connector.connect(host='localhost',database='project',user='root',password='Agasthya0112')
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
    cursor=con.cursor(buffered=True)
    sql1="Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside,image from myteam where position = 'PG' "
    sql2="Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside,image from myteam where position = 'SG' "
    sql3="Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside,image from myteam where position = 'SF' "
    sql4="Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside,image from myteam where position = 'PF' "
    sql5="Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside,image from myteam where position = 'C'"
    sql6="""select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where Name not like %s and position = "PG" """
    sql7="""select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where Name not like %s and position = "SG" """
    sql8="""select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where Name not like %s and position = "SF" """
    sql9="""select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where Name not like %s and position = "PF" """
    sql10="""select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where Name not like %s and position = "C" """
    cursor.execute(sql1)
    valp1=cursor.fetchall()[0]
    img1=pygame.image.load(str(valp1[5])).convert()
    cursor.execute(sql2)
    valp2=cursor.fetchall()[0]
    img2=pygame.image.load(str(valp2[5])).convert()
    cursor.execute(sql3)
    valp3=cursor.fetchall()[0]
    img3=pygame.image.load(str(valp3[5])).convert()
    cursor.execute(sql4)
    valp4=cursor.fetchall()[0]
    img4=pygame.image.load(str(valp4[5])).convert()
    cursor.execute(sql5)
    valp5=cursor.fetchall()[0]
    img5=pygame.image.load(str(valp5[5])).convert()
    cursor.execute(sql6,(valp1[0],))
    valo1=cursor.fetchall()[0]
    cursor.execute(sql7,(valp2[0],))
    valo2=cursor.fetchall()[0]
    cursor.execute(sql8,(valp3[0],))
    valo3=cursor.fetchall()[0]
    cursor.execute(sql9,(valp4[0],))
    valo4=cursor.fetchall()[0]
    cursor.execute(sql10,(valp5[0],))
    valo5=cursor.fetchall()[0]
    offopp="pg"
    defplayer="pg"
    activeplayer="pg"
    pass1=True
    pass2=True
    pass3=True
    pass4=True
    pass5=True
    pass1dur = 1
    pass2dur = random.randint(7,9)
    pass3dur = random.randint(11,13)
    pass4dur=  random.randint(15,17)
    pass5dur=random.randint(3,5)
    a1=random.randint(1,10)
    block=False
    shoot=False
    coll=False
    collo=False
    movement=True
    move=True
    fin=False
    setO=False
    setD=False
    OVER=False
    scp=0
    sc=0
    start_ticks=pygame.time.get_ticks()
    fontdef=pygame.font.get_fonts()[23]
    font=pygame.font.SysFont(fontdef,40) 
    textcenter = (675,450)
    fontdef2=pygame.font.get_fonts()[3]
    winfont=pygame.font.SysFont(fontdef2,90)
    wincenter=(560,160)
    cardfont=pygame.font.SysFont(fontdef2,30)
    cardcenter=(200,150)
    scoresh=pygame.font.SysFont(fontdef2,40)
    fontdef3=pygame.font.get_fonts()[0]
    winfont2=pygame.font.SysFont(fontdef3,30)
    wincenter2=(560,270)
    tfont=pygame.font.SysFont(fontdef3,30)
    tcenter=(1180,450)
    stat1="P"
    fontdefst=pygame.font.get_fonts()[12]
    fontst=pygame.font.SysFont(fontdefst,50)
    mtext="MISS!"
    mcenter=(665,40)
    thptext="3 POINTER MADE!"
    thpcenter=(540,40)
    tptext="2 POINTER MADE!"
    tpcenter=(540,40)
    sc1=0
    bltext="BLOCKED!"
    shothap=0
    blcenter=(620,40)
    itext="INTERCEPTED"
    icenter=(580,40)
    status= 'OFFENSE'
    notransit=True
    px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y=500,200,285,90,285,320,85,160,85,255
    ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y=675,200,365,35,370,370,145,120,145,290
    b1=ball(ox,oy+40)
    cx,cy=85,217
    pxo,pyo,p2xo,p2yo,p3xo,p3yo,p4xo,p4yo,p5xo,p5yo=725,200,1050,40,1050,360,1250,120,1250,290
    oxo,oyo,o2xo,o2yo,o3xo,o3yo,o4xo,o4yo,o5xo,o5yo=925,200,1100,90,1100,320,1300,160,1300,255
    B2=ball(pxo,pyo)
    c2x,c2y=1375,225
    blittime=None
    dtime=22000
    otime=22000
    i = True
    coord=[]
    b,b2=280,130
    count=0
    a=465
    tt1=False
    s1,s2,s3,s4,s5=0,0,0,0,0
    k1,k2,k3,k4,k5=0,0,0,0,0
    while i:
        if a<285:
            break
        coord.append([a,b])
        coord.append([a,b2])
        if a==305:
            a-=5
        elif count>=5:
            a-=20
        else:
            a-=10
        b +=10
        b2 -=10
        count+=1
    def TPD(x,y):
        TP= False
        if y==390:
            TP= True
        elif y==15:
            TP= True
        elif x>=285:
            TP= True
        for i in coord:
            if y<=130:
                if y==i[1] or y == i[1]-5 or y==i[1]+5:
                    if x>=i[0]:
                        TP=True
            elif y>=280:
                if y==i[1] or y == i[1]+5:
                    if x>=i[0]:
                        TP=True
        if TP==True:
            return True

    a=945
    b,b2=280,130
    count=0
    while i:
        if a>1105:
            break
        coord.append([a,b])
        count=0
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
    def TPO(x,y):
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

    while RUN:
        s.fill([0,0,0])
        s.blit(COURT,(0,0))
        s.blit(img1,(0,520))
        s.blit(img2,(312,520))
        s.blit(img3,(624,520))
        s.blit(img4,(936,520))
        s.blit(img5,(1250,520))
        
        p1=player("ply.png",px ,py,pxo,pyo)
        p2=player("ply2.png",p2x,p2y,p2xo,p2yo)    
        p3=player("ply3.png",p3x,p3y,p3xo,p3yo)
        p4=player("ply4.png",p4x,p4y,p4xo,p4yo)
        p5=player("ply5.png",p5x,p5y,p5xo,p5yo)
        o1=opponent("opp.png",ox,oy,oxo,oyo)
        o2=opponent("opp2.png",o2x,o2y,o2xo,o2yo)
        o3=opponent("opp3.png",o3x,o3y,o3xo,o3yo)
        o4=opponent("opp4.png",o4x,o4y,o4xo,o4yo)
        o5=opponent("opp5.png",o5x,o5y,o5xo,o5yo)
        scoretxt=str(scp)+ " - " +str(sc)
        zpr=[[ox,oy],[o2x,o2y],[o3x,o3y],[o4x,o4y],[o5x,o5y]]
        text = font.render(scoretxt,True, [155,0,0], [0,0,0])
        nonpcollide()
        s.blit(text,textcenter)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    exit()                                
                elif event.type == pygame.KEYDOWN:
                    if notransit==True:
                        if event.key == pygame.K_p:
                            RUN=False
                            
                        if status=='DEFENSE':
                            if event.key == pygame.K_LEFT or event.key == pygame.K_a:                  
                                player.movement(curplayer(),-20,0)
                            elif event.key == pygame.K_RIGHT or event.key==pygame.K_d:        
                                    player.movement(curplayer(),20,0)
                            elif event.key == pygame.K_UP or event.key==pygame.K_w:
                                    player.movement(curplayer(),0,-20)
                            elif event.key== pygame.K_DOWN or event.key==pygame.K_s:
                                    player.movement(curplayer(),0,20)
                            elif event.key == pygame.K_1:
                                    defplayer="pg"
                            elif event.key == pygame.K_2:
                                    defplayer="sg"
                            elif event.key == pygame.K_3:
                                    defplayer="sf"
                            elif event.key == pygame.K_4:
                                    defplayer="pf"
                            elif event.key == pygame.K_5:
                                    defplayer="c"
                        elif status=='OFFENSE':
                            if event.key == pygame.K_LEFT or event.key == pygame.K_a:                  
                                player.movement(useplayer(),-20,0)
                            elif event.key == pygame.K_RIGHT or event.key==pygame.K_d:        
                                player.movement(useplayer(),20,0)
                            elif event.key == pygame.K_UP or event.key==pygame.K_w:
                                    player.movement(useplayer(),0,-20)
                            elif event.key== pygame.K_DOWN or event.key==pygame.K_s:
                                    player.movement(useplayer(),0,20)
                            elif event.key == pygame.K_1:
                                    if activeplayer!="pg":
                                        ball.movement(B2,pxo,pyo)
                                        activeplayer="pg"
                                        kpr="pg"
                            elif event.key == pygame.K_2:
                                    if activeplayer!="sg":
                                        ball.movement(B2,p2xo,p2yo)
                                        activeplayer="sg"
                                        kpr="sg"
                            elif event.key == pygame.K_3:
                                    if activeplayer!="sf":
                                        ball.movement(B2,p3xo,p3yo)
                                        activeplayer="sf"
                                        kpr="sf"
                            elif event.key == pygame.K_4:
                                    if activeplayer!="pf":
                                        ball.movement(B2,p4xo,p4yo)
                                        activeplayer="pf"
                                        kpr="pf"
                            elif event.key == pygame.K_5:
                                        if activeplayer!="c":
                                            ball.movement(B2,p5xo,p5yo)
                                            activeplayer="c"
                                            kpr="c"
                            if event.key == pygame.K_SPACE:
                                if ball.state2(B2)!="M":
                                    if scp<21:
                                        shoot=True
                                        if activeplayer=="pg":
                                            player.shot(useplayer(),valp1[1:3],curvalD(),activedefender())
                                            s1,scp=s1+player.score(useplayer()),scp+player.score(useplayer())
                                        elif activeplayer=="sg":
                                                player.shot(useplayer(),valp2[1:3],curvalD(),activedefender())
                                                s2,scp=s2+player.score(useplayer()),scp+player.score(useplayer())
                                        elif activeplayer=="sf":
                                                player.shot(useplayer(),valp3[1:3],curvalD(),activedefender())
                                                s3,scp=s3+player.score(useplayer()),scp+player.score(useplayer())
                                        elif activeplayer=="pf":
                                                player.shot(useplayer(),valp4[1:3],curvalD(),activedefender())
                                                s4,scp=s4+player.score(useplayer()),scp+player.score(useplayer())
                                        elif activeplayer=="c":
                                                player.shot(useplayer(),valp5[1:3],curvalD(),activedefender())
                                                s5,scp=s5+player.score(useplayer()),scp+player.score(useplayer())
                                        if player.activecoord(useplayer())[1]>202:
                                            ball.movement(B2,1375,250)
                                        else:
                                            ball.movement(B2,1375,225)
                                        blittime=pygame.time.get_ticks()+1500
                        
                                        
        if stat1=="M":
            if blittime:
                tst=fontst.render(mtext,True, [0,0,0], [155,0,0])
                s.blit(tst,mcenter)
                if pygame.time.get_ticks()>=blittime:
                    blittime=None
            
        elif stat1=="2P":
            if blittime:
                tst=fontst.render(tptext,True, [0,0,0], [155,0,0])
                s.blit(tst,tpcenter)
                if pygame.time.get_ticks()>=blittime:
                    blittime=None
        elif stat1=="3P":        
            if blittime:
                tst=fontst.render(thptext,True, [0,0,0], [155,0,0])
                s.blit(tst,thpcenter)
                if pygame.time.get_ticks()>=blittime:
                    blittime=None
        elif stat1=="B":
            if blittime:
                tst=fontst.render(bltext,True, [0,0,0], [155,0,0])
                s.blit(tst,blcenter)
                if pygame.time.get_ticks()>=blittime:
                    blittime=None
        elif stat1=="I":
            if blittime:
                tst=fontst.render(itext,True, [0,0,0], [155,0,0])
                s.blit(tst,icenter)
                if pygame.time.get_ticks()>=blittime:
                    blittime=None
        if notransit==False:
            sec=5
            tleft="Time Left is : " + str(sec)
        else:
            if status=="OFFENSE":
                sec=((otime-pygame.time.get_ticks())//1000)
                tleft="Time Left is : " + str(sec)
            elif status=="DEFENSE":
                sec=((dtime-pygame.time.get_ticks())//1000)
                tleft="Time Left is : " + str(sec)
                if pass1:
                    if (20-sec)==pass1dur:
                        opponent.opppass(activeopp())
                        pass1=False
                if pass2:
                    if (20-sec)==pass2dur:
                        opponent.opppass(activeopp())
                        pass2=False
                if pass3:
                    if (20-sec)==pass3dur:
                        opponent.opppass(activeopp())
                        pass3=False
                if pass4:
                    if (20-sec)==pass4dur:
                        opponent.opppass(activeopp())
                        pass4=False
        
        
        
        sc+=opponent.score(activeopp())
        over()
        if OVER!=True:
            tblit = tfont.render(tleft,True, [155,0,0], [0,0,0])
            s.blit(tblit,tcenter)
            if status=="DEFENSE":
                ball.draw(b1)
            elif status=="OFFENSE":
                ball.draw(B2)
            if status == "DEFENSE":
                player.update(curplayer())
                opponent.update(activeopp())
            elif status == "OFFENSE":
                player.update(useplayer())
                opponent.update(activedefender())
        
        pygame.display.update()
        if RUN== False:
            pygame.quit()
