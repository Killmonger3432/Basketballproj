import pygame
import random
import math
import mysql.connector
from sys import exit
from over import *
import warnings
warnings.filterwarnings("ignore")
pygame.init()
dz=0
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
        return (o1,"pg")
    elif b==math.dist(z,[o2xo,o2yo]):
        return (o2,"sg")
    elif b==math.dist(z,[o3xo,o3yo]):
        return (o3,"sf")
    elif b==math.dist(z,[o4xo,o4yo]):
        return (o4,"pf")
    else:
        return (o5,"c")
def activepp(): #calculates nearest player to ball when opponent have ball, meant to help with player shot
    z=opponent.activecoord(activeopp())
    b=min(math.dist(z,[px,py]),math.dist(z,[p2x,p2y]),math.dist(z,[p3x,p3y]),math.dist(z,[p4x,p4y]),math.dist(z,[p5x,p5y]))
    if b==math.dist(z,[px,py]):
        return (p1,"pg")
    elif b==math.dist(z,[p2x,p2y]):
        return (p2,"sg")
    elif b==math.dist(z,[p3x,p3y]):
        return (p3,"sf")
    elif b==math.dist(z,[p4x,p4y]):
        return (p4,"pf")
    else:
        return (p5,"c")
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
def useplayer():
    global textp #returns current player when we have ball
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
def blittext():
    if status == "OFFENSE":
        posblit=posfont.render(pgtext,True,[0,0,0],[255,255,255])
        posblit.set_colorkey((255,255,255))
        s.blit(posblit,((pxo+25),(pyo+90)))
        posblit2=posfont.render(sgtext,True,[0,0,0],[255,255,255])
        posblit2.set_colorkey((255,255,255))
        s.blit(posblit2,((p2xo+25),(p2yo+90)))
        posblit3=posfont.render(sftext,True,[0,0,0],[255,255,255])
        posblit3.set_colorkey((255,255,255))
        s.blit(posblit3,((p3xo+25),(p3yo+90)))
        posblit4=posfont.render(pftext,True,[0,0,0],[255,255,255])
        posblit4.set_colorkey((255,255,255))
        s.blit(posblit4,((p4xo+25),(p4yo+90)))
        posblit5=posfont.render(ctext,True,[0,0,0],[255,255,255])
        posblit5.set_colorkey((255,255,255))
        s.blit(posblit5,((p5xo+25),(p5yo+90)))
    elif status == "DEFENSE":
        posblit=posfont.render(pgtext,True,[0,0,0],[255,255,255])
        posblit.set_colorkey((255,255,255))
        s.blit(posblit,((px+25),(py+90)))
        posblit2=posfont.render(sgtext,True,[0,0,0],[255,255,255])
        posblit2.set_colorkey((255,255,255))
        s.blit(posblit2,((p2x+25),(p2y+90)))
        posblit3=posfont.render(sftext,True,[0,0,0],[255,255,255])
        posblit3.set_colorkey((255,255,255))
        s.blit(posblit3,((p3x+25),(p3y+90)))
        posblit4=posfont.render(pftext,True,[0,0,0],[255,255,255])
        posblit4.set_colorkey((255,255,255))
        s.blit(posblit4,((p4x+25),(p4y+90)))
        posblit5=posfont.render(ctext,True,[0,0,0],[255,255,255])
        posblit5.set_colorkey((255,255,255))
        s.blit(posblit5,((p5x+25),(p5y+90)))
        
        
def plytextmaker():
    if status=="OFFENSE":
        if activeplayer=="pg" :
            plytext="Current Player:" + str(valp1[0]) + "(Point Guard)"
            plyblit=plyfont.render(plytext,True,[155,0,0],[0,0,0])
            s.blit(plyblit,plyfontcenter)
        elif activeplayer=="sg" :
            plytext="Current Player:" + str(valp2[0]) + "(Shooting Guard)"
            plyblit=plyfont.render(plytext,True,[155,0,0],[0,0,0])
            s.blit(plyblit,plyfontcenter)
        elif activeplayer=="sf" :
            plytext="Current Player:" + str(valp3[0]) + "(Small Forward)"
            plyblit=plyfont.render(plytext,True,[155,0,0],[0,0,0])
            s.blit(plyblit,plyfontcenter)
        elif activeplayer=="pf" :
            plytext="Current Player:" + str(valp4[0]) + "(Power Forward)"
            plyblit=plyfont.render(plytext,True,[155,0,0],[0,0,0])
            s.blit(plyblit,plyfontcenter)
        elif activeplayer=="c" :
            plytext="Current Player:" + str(valp5[0]) + "(Center)"
            plyblit=plyfont.render(plytext,True,[155,0,0],[0,0,0])
            s.blit(plyblit,plyfontcenter)
    else:
        if defplayer=="pg" :
            plytext="Current Player:" + str(valp1[0]) + "(Point Guard)"
            plyblit=plyfont.render(plytext,True,[155,0,0],[0,0,0])
            s.blit(plyblit,plyfontcenter)
        elif defplayer=="sg" :
            plytext="Current Player:" + str(valp2[0]) + "(Shooting Guard)"
            plyblit=plyfont.render(plytext,True,[155,0,0],[0,0,0])
            s.blit(plyblit,plyfontcenter)
        elif defplayer=="sf" :
            plytext="Current Player:" + str(valp3[0]) + "(Small Forward)"
            plyblit=plyfont.render(plytext,True,[155,0,0],[0,0,0])
            s.blit(plyblit,plyfontcenter)
        elif defplayer=="pf" :
            plytext="Current Player:" + str(valp4[0]) + "(Power Forward)"
            plyblit=plyfont.render(plytext,True,[155,0,0],[0,0,0])
            s.blit(plyblit,plyfontcenter)
        elif defplayer=="c" :
            plytext="Current Player:" + str(valp5[0]) + "(Center)"
            plyblit=plyfont.render(plytext,True,[155,0,0],[0,0,0])
            s.blit(plyblit,plyfontcenter)
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
    def __init__(self, imagefile, x, y, xo, yo):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.load = pygame.image.load(imagefile).convert()
        self.rect = self.load.get_rect()
        self.movex = 0
        self.movey = 0
        if status == "OFFENSE":
            self.rect.x = xo
            self.rect.y = yo
        elif status == "DEFENSE":
            self.rect.x = x
            self.rect.y = y

        self.Z = 0
        self.shotprob, self.dis, self.defprob = 0, 0, 0

    def boundaryD(self):
        if self.rect.x >= 675:
            self.rect.x = 675
        if self.rect.x <= 30:
            self.rect.x = 30
        if self.rect.y <= 15:
            self.rect.y = 15
        if self.rect.y >= 390:
            self.rect.y = 390

    def boundaryO(self):
        if self.rect.x >= 1365:
            self.rect.x = 1365
        if self.rect.x <= 725:
            self.rect.x = 725
        if self.rect.y <= 15:
            self.rect.y = 15
        if self.rect.y >= 390:
            self.rect.y = 390

    def oppmove(self):
        global ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y
        global fin
        
        hoopdis = math.dist([self.rect.x, self.rect.y], [65, 202.5])
        if a1 == 1:
            ax, ay = 405, 80
            bx, by = 85, 15
            cx, cy = 405, 330
            dx, dy = 330, 200
            ex, ey = 115, 300
            a2x, a2y = 310, 250
            b2x, b2y = 405, 320
            c2x, c2y = 85, 339.5
            d2x, d2y = 85, 250
            e2x, e2y = 185, 155
        elif a1 == 2:
            ax, ay = 400, 330
            bx, by = 400, 80
            cx, cy = 85, 339.5
            dx, dy = 105, 120
            ex, ey = 330, 200
            a2x, a2y = 305, 160
            b2x, b2y = 90, 15
            c2x, c2y = 400, 80
            d2x, d2y = 150, 250
            e2x, e2y = 90, 120
        elif a1 == 3:
            ax, ay = 85, 339.5
            bx, by = 85, 0
            cx, cy = 450, 120
            dx, dy = 270, 280
            ex, ey = 270, 130
            a2x, a2y = 85, 330
            b2x, b2y = 85, 80
            c2x, c2y = 330, 200
            d2x, d2y = 270, 300
            e2x, e2y = 270, 110
        elif a1 == 4:
            ax, ay = 85, 0
            bx, by = 465, 200
            cx, cy = 85, 339.5
            dx, dy = 240, 280
            ex, ey = 240, 130
            a2x, a2y = 85, 80
            b2x, b2y = 330, 200
            c2x, c2y = 85, 330
            d2x, d2y = 270, 300
            e2x, e2y = 270, 110

        elif a1 == 5:
            ax, ay = 185, 300
            bx, by = 130, 100
            cx, cy = 70, 339.5
            dx, dy = 390, 80
            ex, ey = 310, 150
            a2x, a2y = 325, 220
            b2x, b2y = 450, 120
            c2x, c2y = 270, 0
            d2x, d2y = 230, 120
            e2x, e2y = 130, 250
        elif a1 == 6:
            ax, ay = 205, 120
            bx, by = 90, 15
            cx, cy = 150, 310
            dx, dy = 310, 240
            ex, ey = 390, 330
            a2x, a2y = 325, 180
            b2x, b2y = 290, 20
            c2x, c2y = 390, 340
            d2x, d2y = 130, 160
            e2x, e2y = 230, 290
        elif a1 == 7:
            ax, ay = 160, 339.5
            bx, by = 250, 120
            cx, cy = 250, 290
            dx, dy = 110, 0
            ex, ey = 110, 339.5
            a2x, a2y = 265, 339.5
            b2x, b2y = 110, 290
            c2x, c2y = 110, 110
            d2x, d2y = 310, 110
            e2x, e2y = 310, 290
        elif a1 == 8:
            ax, ay = 160, 0
            bx, by = 250, 120
            cx, cy = 250, 290
            dx, dy = 110, 0
            ex, ey = 110, 339.5
            a2x, a2y = 265, 0
            b2x, b2y = 110, 110
            c2x, c2y = 110, 290
            d2x, d2y = 290, 290
            e2x, e2y = 290, 110
        elif a1 == 9:
            ax, ay = 305, 280
            bx, by = 85, 339.5
            cx, cy = 310, 0
            dx, dy = 390, 200
            ex, ey = 130, 150
            a2x, a2y = 125, 320
            b2x, b2y = 270, 339.5
            c2x, c2y = 465, 195
            d2x, d2y = 290, 110
            e2x, e2y = 90, 90
        elif a1 == 10:
            ax, ay = 305, 120
            bx, by = 350, 339.5
            cx, cy = 90, 0
            dx, dy = 150, 250
            ex, ey = 390, 210
            a2x, a2y = 145, 80
            b2x, b2y = 470, 210
            c2x, c2y = 305, 0
            d2x, d2y = 90, 310
            e2x, e2y = 310, 290

            
        step = max(abs(ax - ox), abs(ay - oy))
        step2 = max(abs(bx - o2x), abs(by - o2y))
        step3 = max(abs(cx - o3x), abs(cy - o3y))
        step4 = max(abs(dx - o4x), abs(dy - o4y))
        step5 = max(abs(ex - o5x), abs(ey - o5y))
        step6 = max(abs(a2x - ox), abs(a2y - oy))
        step7 = max(abs(b2x - o2x), abs(b2y - o2y))
        step8 = max(abs(c2x - o3x), abs(c2y - o3y))
        step9 = max(abs(d2x - o4x), abs(d2y - o4y))
        step10 = max(abs(e2x - o5x), abs(e2y - o5y))
        
        if fin == True:
            if math.dist([a2x, a2y], [ox, oy]) <= 15:
                ox = a2x
                oy = a2y
                if math.dist([b2x, b2y], [o2x, o2y]) <= 15:
                    o2x = b2x
                    o2y = b2y
                    if math.dist([c2x, c2y], [o3x, o3y]) <= 15:
                        o3x = c2x
                        o3y = c2y
                        if math.dist([d2x, d2y], [o4x, o4y]) <= 15:
                            o4x = d2x
                            o4y = d2y
                            if math.dist([e2x, e2y], [o5x, o5y]) <= 15:
                                o5x = e2x
                                o5y = e2y
                            else:
                                o5x += ((e2x - o5x) / step10) * 20
                                o5y += ((e2y - o5y) / step10) * 20
                        else:
                            o4x += ((d2x - o4x) / step9) * 20
                            o4y += ((d2y - o4y) / step9) * 20
                    else:
                        o3x += ((c2x - o3x) / step8) * 20
                        o3y += ((c2y - o3y) / step8) * 20
                else:
                    o2x += ((b2x - o2x) / step7) * 20
                    o2y += ((b2y - o2y) / step7) * 20
                
            else:
                ox += ((a2x - ox) / step6) * 20
                oy += ((a2y - oy) / step6) * 20
        else:
            if math.dist([ax, ay], [ox, oy]) <= 20:
                ox = ax
                oy = ay
                if math.dist([bx, by], [o2x, o2y]) <= 20:
                    o2x = bx
                    o2y = by
                    if math.dist([cx, cy], [o3x, o3y]) <= 20:
                        o3x = cx
                        o3y = cy
                        if math.dist([dx, dy], [o4x, o4y]) <= 20:
                            o4x = dx
                            o4y = dy
                    
                            if math.dist([ex, ey], [o5x, o5y]) <= 20:
                                o5x = ex
                                o5y = ey
                                fin = True
                            else:
                                o5x += ((ex - o5x) / step5) * 25
                                o5y += ((ey - o5y) / step5) * 25
                        else:
                            o4x += ((dx - o4x) / step4) * 25
                            o4y += ((dy - o4y) / step4) * 25
                            
                    else:
                        o3x += ((cx - o3x) / step3) * 25
                        o3y += ((cy - o3y) / step3) * 25
                        
                else:
                    o2x += ((bx - o2x) / step2) * 25
                    o2y += ((by - o2y) / step2) * 25
            else:
                ox += ((ax - ox) / step) * 25
                oy += ((ay - oy) / step) * 25

    def move_towards_player(self):
        global oxo, oyo, o2xo, o2yo, o3xo, o3yo, o4xo, o4yo, o5xo, o5yo
        dx = 0
        dy = 0
        if math.dist(player.activecoord(useplayer()), opponent.activecoord(activedefender()[0])) < 400:
            step = max(abs(player.activecoord(useplayer())[0] - opponent.activecoord(activedefender()[0])[0]),
                       abs(player.activecoord(useplayer())[1] - opponent.activecoord(activedefender()[0])[1]))
            dx += float(player.activecoord(useplayer())[0] - opponent.activecoord(activedefender()[0])[0]) / step
            dy += float(player.activecoord(useplayer())[1] - opponent.activecoord(activedefender()[0])[1]) / step
        if math.dist(player.activecoord(useplayer()), opponent.activecoord(activedefender()[0])) <= 25:
            dx = 0
            dy = 0
        if activedefender()[1] == "pg":
            oxo += (dx/3.2)  *clock.tick(20)
            oyo += (dy/3.2)*clock.tick(20)
        if activedefender()[1] == "sg":
            o2xo += (dx/3.2) *clock.tick(20)
            o2yo += (dy/3.2)*clock.tick(20)
        if activedefender()[1] == "sf":
            o3xo += (dx / 3.2)*clock.tick(20)
            o3yo += (dy / 3.2)*clock.tick(20)
        if activedefender()[1] == "pf":
            o4xo += (dx / 3.2)*clock.tick(20)
            o4yo += (dy / 3.2)*clock.tick(20)
        if activedefender()[1] == "c":
            o5xo += (dx / 3.2)*clock.tick(20)
            o5yo += (dy / 3.2)*clock.tick(20)

    def activecoord(x):
        if status == "DEFENSE":
            if x == o1:
                z = [ox, oy]
            elif x == o3:
                z = [o3x, o3y]
            elif x == o2:
                z = [o2x, o2y]
            elif x == o4:
                z = [o4x, o4y]
            elif x == o5:
                z = [o5x, o5y]
            return z
        elif status == "OFFENSE":
            if x == o1:
                z = [oxo, oyo]
            elif x == o3:
                z = [o3xo, o3yo]
            elif x == o2:
                z = [o2xo, o2yo]
            elif x == o4:
                z = [o4xo, o4yo]
            elif x == o5:
                z = [o5xo, o5yo]
            return z

    def opppass(self):
        global offopp, movement
        pos1 = zpr[0]
        pos2 = zpr[1]
        pos3 = zpr[2]
        pos4 = zpr[3]
        pos5 = zpr[4]
        dis1 = math.dist(opponent.activecoord(self), pos1)
        dis2 = math.dist(opponent.activecoord(self), pos2)
        dis3 = math.dist(opponent.activecoord(self), pos3)
        dis4 = math.dist(opponent.activecoord(self), pos4)
        dis5 = math.dist(opponent.activecoord(self), pos5)
        dislist = [dis1, dis2, dis3, dis4, dis5]
        dislist.sort()
        if dislist[1] == dis1:
            prob1 = "pg"
            moveloc = [ox, oy]
        if dislist[2] == dis1:
            prob2 = "pg"
            moveloc2 = [ox, oy]
        if dislist[1] == dis2:
            prob1 = "sg"
            moveloc = [o2x, o2y]
        if dislist[2] == dis2:
            prob2 = "sg"
            moveloc2 = [o2x, o2y]
        if dislist[1] == dis3:
            prob1 = "sf"
            moveloc = [o3x, o3y]
        if dislist[2] == dis3:
            prob2 = "sf"
            moveloc2 = [o3x, o3y]
        if dislist[1] == dis4:
            prob1 = "pf"
            moveloc = [o4x, o4y]
        if dislist[2] == dis4:
            prob2 = "pf"
            moveloc2 = [o4x, o4y]
        if dislist[1] == dis5:
            prob1 = "c"
            moveloc = [o5x, o5y]
        if dislist[2] == dis5:
            prob2 = "c"
            moveloc2 = [o5x, o5y]
        pprob = random.randint(1, 10)
        if shoot == False:
            if coll == False:
                if pprob in range(1, 7):
                    temp12 = prob1
                    moveball = moveloc
                else:
                    temp12 = prob2
                    moveball = moveloc2
                ball.movement(b1,moveball[0],moveball[1])
                offopp=temp12

    def shot2(self, x, y):
        if TPD(opponent.activecoord(self)[0], opponent.activecoord(self)[1]):
            self.K = True
        else:
            self.K = False

        if math.dist(opponent.activecoord(self), [65, 202.5]) <= 100:
            self.dis = 10
        elif math.dist(opponent.activecoord(self), [65, 202.5]) <= 200 and math.dist(opponent.activecoord(self),
                                                                                     [65, 202.5]) > 100:
            self.dis = 8
        elif math.dist(opponent.activecoord(self), [65, 202.5]) <= 300 and math.dist(opponent.activecoord(self),
                                                                                     [65, 202.5]) > 200:
            self.dis = 6
        elif math.dist(opponent.activecoord(self), [65, 202.5]) <= 400 and math.dist(opponent.activecoord(self),
                                                                                     [65, 202.5]) > 300:
            self.dis = 4
        elif math.dist(opponent.activecoord(self), [65, 202.5]) <= 550 and math.dist(opponent.activecoord(self),
                                                                                     [65, 202.5]) > 400:
            self.dis = 2
        else:
            self.dis = 0
        if self.K:
            if x[1] - y[1] >= 20:
                self.shotprob = 8 + random.randint(0, 2)
            elif x[1] - y[1] >= 15 and x[1] - y[1] < 20:
                self.shotprob = 7 + random.randint(0, 3)
            elif x[1] - y[1] >= 10 and x[1] - y[1] < 15:
                self.shotprob = 6 + random.randint(0, 4)
            elif x[1] - y[1] >= 7 and x[1] - y[1] < 10:
                self.shotprob = 5 + random.randint(0, 5)
            else:
                self.shotprob = 2 + random.randint(0, 8)
        else:
            if x[0] - y[0] >= 20:
                self.shotprob = 8 + random.randint(0, 2)
            elif x[0] - y[0] >= 15 and x[0] - y[0] < 20:
                self.shotprob = 7 + random.randint(0, 3)
            elif x[0] - y[0] >= 10 and x[0] - y[0] < 15:
                self.shotprob = 6 + random.randint(0, 4)
            elif x[0] - y[0] >= 7 and x[0] - y[0] < 10:
                self.shotprob = 5 + random.randint(0, 5)
            else:
                self.shotprob = 2 + random.randint(0, 8)
        if math.dist(opponent.activecoord(activeopp()), player.activecoord(curplayer())) < 80:
            self.defprob = random.randint(1, 10)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        blockprob = random.randint(1, 2)
                        if blockprob == 1:
                            block = True
                        else:
                            block = False
        elif math.dist(opponent.activecoord(activeopp()), player.activecoord(curplayer())) < 100 and math.dist(
                opponent.activecoord(self), player.activecoord(curplayer())) >= 80:
            self.defprob = 2 + random.randint(0, 8)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        blockprob = random.randint(0, 3)
                        if blockprob == 1:
                            block = True
                        else:
                            block = False
        elif math.dist(opponent.activecoord(self), player.activecoord(curplayer())) >= 100 and math.dist(
                opponent.activecoord(self), player.activecoord(curplayer())) < 120:
            self.defprob = 4 + random.randint(0, 6)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        blockprob = random.randint(0, 9)
                        if blockprob == 1:
                            block = True
                        else:
                            block = False
        elif math.dist(opponent.activecoord(self), player.activecoord(curplayer())) >= 120 and math.dist(
                opponent.activecoord(self), player.activecoord(curplayer())) < 140:
            self.defprob = 6 + random.randint(0, 4)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        block = False
        else:
            self.defprob = 8 + random.randint(0, 2)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        block = False
        self.Z = self.shotprob + self.defprob + self.dis
    def shot(self, x, y):
        global RUN
        if TPD(opponent.activecoord(self)[0], opponent.activecoord(self)[1]):
            self.K = True
        else:
            self.K = False

        if math.dist(opponent.activecoord(activeopp()), player.activecoord(activepp()[0])) >= 100:
            if self.K:
                if math.dist(opponent.activecoord(self), [65, 202.5]) <= 450:
                    if x[1] - y[1] >= 20:
                        chance = random.randint(1, 100)
                        if chance == 1:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[1] - y[1] >= 15 and x[1] - y[1] < 20:
                        chance = random.randint(1, 200)
                        if chance == 1:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[1] - y[1] >= 10 and x[1] - y[1] < 15:
                        chance = random.randint(1, 300)
                        if chance == 1:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[1] - y[1] >= 5 and x[1] - y[1] < 10:
                        chance = random.randint(1, 400)
                        if chance == 1:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    else:
                        chance = random.randint(1, 500)
                        if chance == 1:
                            opponent.shot2(activeopp(), curvalO(), plycurval())

            else:
                if math.dist(opponent.activecoord(self), [65, 202.5]) <= 100:
                    if x[0] - y[0] >= 20:
                        chance = random.randint(1, 50)
                        if chance == 6:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[0] - y[0] >= 15 and x[0] - y[0] < 20:
                        chance = random.randint(1, 100)
                        if chance == 5:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[0] - y[0] >= 10 and x[0] - y[0] < 15:
                        chance = random.randint(1, 150)
                        if chance == 4:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[0] - y[0] >= 5 and x[0] - y[0] < 10:
                        chance = random.randint(1, 200)
                        if chance == 3:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    else:
                        chance = random.randint(1, 250)
                        if chance == 2:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                elif math.dist(opponent.activecoord(self), [65, 202.5]) <= 200 and math.dist(opponent.activecoord(self),
                                                                                             [65, 202.5]) > 100:
                    if x[0] - y[0] >= 20:
                        chance = random.randint(1, 100)
                        if chance == 5:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[0] - y[0] >= 15 and x[0] - y[0] < 20:
                        chance = random.randint(1, 200)
                        if chance == 4:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[0] - y[0] >= 10 and x[0] - y[0] < 15:
                        chance = random.randint(1, 300)
                        if chance == 3:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[0] - y[0] >= 5 and x[0] - y[0] < 10:
                        chance = random.randint(1, 400)
                        if chance == 2:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    else:
                        chance = random.randint(1, 500)
                        if chance == 1:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                elif math.dist(opponent.activecoord(self), [65, 202.5]) <= 300 and math.dist(opponent.activecoord(self),
                                                                                             [65, 202.5]) > 200:
                    if x[0] - y[0] >= 20:
                        chance = random.randint(1, 150)
                        if chance == 3:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[0] - y[0] >= 15 and x[0] - y[0] < 20:
                        chance = random.randint(1, 250)
                        if chance == 2:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[0] - y[0] >= 10 and x[0] - y[0] < 15:
                        chance = random.randint(1, 350)
                        if chance == 2:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[0] - y[0] >= 5 and x[0] - y[0] < 10:
                        chance = random.randint(1, 450)
                        if chance == 2:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    else:
                        chance = random.randint(1, 550)
                        if chance == 1:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                elif math.dist(opponent.activecoord(self), [65, 202.5]) <= 400 and math.dist(opponent.activecoord(self),
                                                                                             [65, 202.5]) > 300:
                    if x[0] - y[0] >= 20:
                        chance = random.randint(1, 200)
                        if chance == 5:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[0] - y[0] >= 15 and x[0] - y[0] < 20:
                        chance = random.randint(1, 300)
                        if chance == 2:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[0] - y[0] >= 10 and x[0] - y[0] < 15:
                        chance = random.randint(1, 400)
                        if chance == 2:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    elif x[0] - y[0] >= 7 and x[0] - y[0] < 10:
                        chance = random.randint(1, 500)
                        if chance == 2:
                            opponent.shot2(activeopp(), curvalO(), plycurval())
                    else:
                        chance = random.randint(1, 600)
                        if chance == 1:
                            opponent.shot2(activeopp(), curvalO(), plycurval())

    def score(self):
        global stat1, RUN, shoot, status, movement, blittime, k1, k2, k3, k4, k5
        if status == 'DEFENSE':
            if shoot == False:
                if movement == True:
                    opponent.shot(self, curvalO(), plycurval())
            
            

        score = 0
        if TPD(opponent.activecoord(self)[0], opponent.activecoord(self)[1]):
            self.K = True
        else:
            self.K = False
        if block == True:
            score = 0
            stat1 = "B"

        elif self.Z > 0:
            if movement:
                if coll == False:
                    shoot = True
                    if self.Z >= 23:
                        if self.K:
                            score = 3
                            stat1 = '3P'
                        else:
                            score = 2
                            stat1 = '2P'
                    else:
                        stat1 = "M"
                        score = 0
                    if offopp == "pg":
                        k1 += score
                    elif offopp == "sg":
                        k2 += score
                    elif offopp == "sf":
                        k3 += score
                    elif offopp == "pf":
                        k4 += score
                    elif offopp == "c":
                        k5 += score
                    ball.movement(b1, cx, cy)
                    movement = False
                    blittime = pygame.time.get_ticks() + 1500

        return score


    def update(self):
        global ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y ,dz1
        global movestat1,movestat2,movestat3,movestat4,movestat5
        global oxo, oyo, o2xo, o2yo, o3xo, o3yo, o4xo, o4yo, o5xo, o5yo
        global oldox,oldoy,oldo2x,oldo2y,oldo3x,oldo3y,oldo4x,oldo4y,oldo5x,oldo5y
        global oldoxo, oldoyo, oldo2xo, oldo2yo, oldo3xo, oldo3yo, oldo4xo, oldo4yo, oldo5xo, oldo5yo
        if status == 'DEFENSE':
            if notransit:
                if shoot == False:
                    if coll == False:
                        if pause==False:
                            opponent.oppmove(self)

                    opponent.boundaryD(self)
        elif status == 'OFFENSE':
           self = activedefender()[0]
           if notransit:
                if shoot == False:
                    if coll == False:
                        if pause==False:
                            opponent.move_towards_player(self)
                opponent.boundaryO(self)


        if status == "DEFENSE":
            if oldox > ox  + 0 and oldoy == oy:
                s.blit(f1[1][dz], (ox, oy))
                movestat1="L"
            elif oldox + 0 < ox and oldoy == oy:
                s.blit(f1[2][dz], (ox, oy))
                movestat1="R"
            elif abs(oldox-ox)<=10 and oldoy < oy + 0:
                s.blit(f1[0][dz], (ox, oy))
                movestat1="D"
            elif abs(oldox - ox)<=10 and oldoy > oy + 0:
                s.blit(f1[3][dz], (ox, oy))
                movestat1="U"
            elif oldox > ox + 0 and oldoy + 0 < oy:
                s.blit(f1[1][dz], (ox, oy))
                movestat1="L"
            elif oldox + 0 < ox and oldoy > oy + 0:
                s.blit(f1[2][dz], (ox, oy))
                movestat1="R"
            elif oldox + 0 < ox and oldoy + 0 < oy:
                s.blit(f1[2][dz], (ox, oy))
                movestat1="R"
            elif oldox > ox + 0 and oldoy > oy + 0:
                s.blit(f1[1][dz], (ox, oy))
                movestat1="L"
            elif oldox==ox and oldoy==oy:
                s.blit(f1[0][0], (ox, oy))
                movestat1="S"

            if oldo2x > o2x + 0 and oldo2y == o2y:
                s.blit(f2[1][dz], (o2x, o2y))
                movestat2="L"
            elif oldo2x + 0 < o2x and oldo2y == o2y:
                s.blit(f2[2][dz], (o2x, o2y))
                movestat2="R"
            elif abs(oldo2x - o2x)<=10 and oldo2y + 0 < o2y :
                s.blit(f2[0][dz], (o2x, o2y))
                movestat2="D"

            elif abs(oldo2x-o2x)<=10 and oldo2y > o2y + 0:
                s.blit(f2[3][dz], (o2x, o2y))
                movestat2="U"
            elif oldo2x > o2x + 0 and oldo2y + 0 < o2y:
                s.blit(f2[1][dz], (o2x, o2y))
                movestat2="L"
            elif oldo2x + 0 < o2x and oldo2y > o2y + 0:
                s.blit(f2[2][dz], (o2x, o2y))
                movestat2="L"
            elif oldo2x + 0 < o2x and oldo2y + 0 < o2y:
                s.blit(f2[2][dz], (o2x, o2y))
                movestat2="R"
            elif oldo2x > o2x + 0 and oldo2y > o2y + 0:
                s.blit(f2[1][dz], (o2x, o2y))
                movestat2="L"
            elif oldo2x==o2x and oldo2y==o2y:
                s.blit(f2[0][0], (o2x, o2y))
                movestat2="S"
            if oldo3x > o3x + 0 and oldo3y == o3y:
                s.blit(f3[1][dz], (o3x, o3y))
                movestat3="L"
            elif oldo3x + 0 < o3x and oldo3y == o3y:
                s.blit(f3[2][dz], (o3x, o3y))
                movestat3="R"
            elif abs(oldo3x-o3x)<=10 and oldo3y + 0 < o3y:
                s.blit(f3[0][dz], (o3x, o3y))
                movestat3="D"
            elif abs(oldo3x-o3x)<=10 and oldo3y > o3y + 0:
                s.blit(f3[3][dz], (o3x, o3y))
                movestat3="U"
            elif oldo3x > o3x + 0 and oldo3y + 0 < o3y:
                s.blit(f3[1][dz], (o3x, o3y))
                movestat3="L"
            elif oldo3x + 0 < o3x and oldo3y > o3y + 0:
                s.blit(f3[2][dz], (o3x, o3y))
                movestat3="R"
            elif oldo3x + 0 < o3x and oldo3y + 0 < o3y:
                s.blit(f3[2][dz], (o3x, o3y))
                movestat3="R"
            elif oldo3x > o3x + 0 and oldo3y > o3y + 0:
                s.blit(f3[1][dz], (o3x, o3y))
                movestat3="L"
            elif oldo3x==o3x and oldo3y==o3y:
                s.blit(f3[0][0], (o3x, o3y))
                movestat3="S"

            if oldo4x > o4x + 0 and oldo4y == o4y:
                
                s.blit(f4[1][dz], (o4x, o4y))
                movestat4="L"
            elif oldo4x + 0 < o4x and oldo4y == o4y:
                s.blit(f4[2][dz], (o4x, o4y))
                movestat4="R"
            elif abs(oldo4x-o4x)<=10 and oldo4y + 0 < o4y:
                
                s.blit(f4[0][dz], (o4x, o4y))
                movestat4="D"
            elif abs(oldo4x-o4x)<=10 and oldo4y > o4y + 0:
               
                s.blit(f4[3][dz], (o4x, o4y))
                movestat4="U"
            elif oldo4x > o4x + 0 and oldo4y + 0 < o4y:
                s.blit(f4[1][dz], (o4x, o4y))
                movestat4="L"
            elif oldo4x + 0 < o4x and oldo4y > o4y + 0:
                s.blit(f4[2][dz], (o4x, o4y))
                movestat4="R"
            elif oldo4x + 0 < o4x and oldo4y + 0 < o4y:
                movestat4="R"
                s.blit(f4[2][dz], (o4x, o4y))
            elif oldo4x > o4x + 0 and oldo4y > o4y + 0:
                s.blit(f4[1][dz], (o4x, o4y))
                movestat4="L"
            elif oldo4x==o4x and oldo4y==o4y:
                s.blit(f4[0][0], (o4x, o4y))
                movestat4="S"

            if oldo5x > o5x + 0 and oldo5y == o5y:
                s.blit(f5[1][dz], (o5x, o5y))
                movestat5="L"
            elif oldo5x + 0 < o5x and oldo5y == o5y:
                s.blit(f5[2][dz], (o5x, o5y))
                movestat5="R"
            elif abs(oldo5x-o5x)<=10 and oldo5y + 0 < o5y:
                s.blit(f5[0][dz], (o5x, o5y))
                movestat5="D"
            elif abs(oldo5x-o5x)<=10 and oldo5y > o5y + 0:
                s.blit(f5[3][dz], (o5x, o5y))
                movestat5="U"
            elif oldo5x > o5x + 0 and oldo5y + 0 < o5y:
                s.blit(f5[1][dz], (o5x, o5y))
                movestat5="L"
            elif oldo5x + 0 < o5x and oldo5y > o5y + 0:
                s.blit(f5[2][dz], (o5x, o5y))
                movestat5="R"
            elif oldo5x + 0 < o5x and oldo5y + 0 < o5y:
                s.blit(f5[2][dz], (o5x, o5y))
                movestat5="R"
            elif oldo5x > o5x + 0 and oldo5y > o5y + 0:
                s.blit(f5[1][dz], (o5x, o5y))
                movestat5="L"
            elif oldo5x==o5x and oldo5y==o5y:
                s.blit(f5[0][0], (o5x, o5y))
                movestat5="S"
        elif status == "OFFENSE":



            if oldoxo > oxo + 0 and oldoyo == oyo:
                s.blit(f1[1][dz], (oxo, oyo))
            elif oldoxo + 0 < oxo and oldoyo == oyo:
                s.blit(f1[2][dz], (oxo, oyo))
            elif oldoxo == oxo and oldoyo + 0 < oyo:
                s.blit(f1[0][dz], (oxo, oyo))
            elif oldoxo == oxo and oldoyo > oyo + 0:
                s.blit(f1[3][dz], (oxo, oyo))
            elif oldoxo > oxo + 0 and oldoyo + 0 < oyo:
                s.blit(f1[1][dz], (oxo, oyo))
            elif oldoxo + 0 < oxo and oldoyo > oyo + 0:
                s.blit(f1[2][dz], (oxo, oyo))
            elif oldoxo + 0 < oxo and oldoyo + 0 < oyo:
                s.blit(f1[2][dz], (oxo, oyo))
            elif oldoxo > oxo + 0 and oldoyo > oyo + 0:
                s.blit(f1[1][dz], (oxo, oyo))
            else:
                s.blit(f1[0][0], (oxo, oyo))


            if oldo2xo > o2xo + 0 and oldo2yo == o2yo:
                s.blit(f2[1][dz], (o2xo, o2yo))
            elif oldo2xo + 0 < o2xo and oldo2yo == o2yo:
                s.blit(f2[2][dz], (o2xo, o2yo))
            elif oldo2xo == o2xo and oldo2yo + 0 < o2yo:
                s.blit(f2[0][dz], (o2xo, o2yo))
            elif oldo2xo == o2xo and oldo2yo > o2yo + 0:
                s.blit(f2[3][dz], (o2xo, o2yo))
            elif oldo2xo > o2xo + 0 and oldo2yo + 0 < o2yo:
                s.blit(f2[1][dz], (o2xo, o2yo))
            elif oldo2xo + 0 < o2xo and oldo2yo > o2yo + 0:
                s.blit(f2[2][dz], (o2xo, o2yo))
            elif oldo2xo + 0 < o2xo and oldo2yo + 0 < o2yo:
                s.blit(f2[2][dz], (o2xo, o2yo))
            elif oldo2xo > o2xo + 0 and oldo2yo > o2yo + 0:
                s.blit(f2[1][dz], (o2xo, o2yo))
            else:
                s.blit(f2[0][0], (o2xo, o2yo))


            if oldo3xo > o3xo + 0 and oldo3yo == o3yo:
                s.blit(f3[1][dz], (o3xo, o3yo))
            elif oldo3xo + 0 < o3xo and oldo3yo == o3yo:
                s.blit(f3[2][dz], (o3xo, o3yo))
            elif oldo3xo == o3xo and oldo3yo + 0 < o3yo:
                s.blit(f3[0][dz], (o3xo, o3yo))
            elif oldo3xo == o3xo and oldo3yo > o3yo + 0:
                s.blit(f3[3][dz], (o3xo, o3yo))
            elif oldo3xo > o3xo + 0 and oldo3yo + 0 < o3yo:
                s.blit(f3[1][dz], (o3xo, o3yo))
            elif oldo3xo + 0 < o3xo and oldo3yo > o3yo + 0:
                s.blit(f3[2][dz], (o3xo, o3yo))
            elif oldo3xo + 0 < o3xo and oldo3yo + 0 < o3yo:
                s.blit(f3[2][dz], (o3xo, o3yo))
            elif oldo3xo > o3xo + 0 and oldo3yo > o3yo + 0:
                s.blit(f3[1][dz], (o3xo, o3yo))
            else:
                s.blit(f3[0][0], (o3xo, o3yo))


            if oldo4xo > o4xo + 0 and oldo4yo == o4yo:
                s.blit(f4[1][dz], (o4xo, o4yo))
            elif oldo4xo + 0 < o4xo and oldo4yo == o4yo:
                s.blit(f4[2][dz], (o4xo, o4yo))
            elif oldo4xo == o4xo and oldo4yo + 0 < o4yo:
                s.blit(f4[0][dz], (o4xo, o4yo))
            elif oldo4xo == o4xo and oldo4yo > o4yo + 0:
                s.blit(f4[3][dz], (o4xo, o4yo))
            elif oldo4xo > o4xo + 0 and oldo4yo + 0 < o4yo:
                s.blit(f4[1][dz], (o4xo, o4yo))
            elif oldo4xo + 0 < o4xo and oldo4yo > o4yo + 0:
                s.blit(f4[2][dz], (o4xo, o4yo))
            elif oldo4xo + 0 < o4xo and oldo4yo + 0 < o4yo:
                s.blit(f4[2][dz], (o4xo, o4yo))
            elif oldo4xo > o4xo + 0 and oldo4yo > o4yo + 0:
                s.blit(f4[1][dz], (o4xo, o4yo))
            else:
                s.blit(f4[0][0], (o4xo, o4yo))


            if oldo5xo > o5xo + 0 and oldo5yo == o5yo:
                s.blit(f5[1][dz], (o5xo, o5yo))
            elif oldo5xo + 0 < o5xo and oldo5yo == o5yo:
                s.blit(f5[2][dz], (o5xo, o5yo))
            elif oldo5xo == o5xo and oldo5yo + 0 < o5yo:
                s.blit(f5[0][dz], (o5xo, o5yo))
            elif oldo5xo == o5xo and oldo5yo > o5yo + 0:
                s.blit(f5[3][dz], (o5xo, o5yo))
            elif oldo5xo > o5xo + 0 and oldo5yo + 0 < o5yo:
                s.blit(f5[1][dz], (o5xo, o5yo))
            elif oldo5xo + 0 < o5xo and oldo5yo > o5yo + 0:
                s.blit(f5[2][dz], (o5xo, o5yo))
            elif oldo5xo + 0 < o5xo and oldo5yo + 0 < o5yo:
                s.blit(f5[2][dz], (o5xo, o5yo))
            elif oldo5xo > o5xo + 0 and oldo5yo > o5yo + 0:
                s.blit(f5[1][dz], (o5xo, o5yo))
            else:
                s.blit(f5[0][0], (o5xo, o5yo))

        if dz1 +1 == 4 :
            dz1= 0
        else :
            dz1= dz +1
        oldox, oldoy, oldo2x, oldo2y, oldo3x, oldo3y, oldo4x, oldo4y, oldo5x, oldo5y = ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y
        oldoxo, oldoyo, oldo2xo, oldo2yo, oldo3xo, oldo3yo, oldo4xo, oldo4yo, oldo5xo, oldo5yo = oxo, oyo, o2xo, o2yo, o3xo, o3yo, o4xo, o4yo, o5xo, o5yo
    
                    
                
class player(pygame.sprite.Sprite):
    def __init__(self, imagefile, x, y, xo, yo):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.load = pygame.image.load(imagefile).convert()
        self.movex = 0
        self.movey = 0
        self.rect = self.load.get_rect()
        if status == "DEFENSE":
            self.rect.x = x
            self.rect.y = y
        if status == "OFFENSE":
            self.rect.x = xo
            self.rect.y = yo
        self.score = 0

    def boundaryD(self):
        global px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y
        if px >= 675:
            px = 675
        if px <= 30:
            px = 30
        if py <= 0:
            py = 0
        if py >= 339.5:
            py = 339.5
        if p2x >= 675:
            p2x = 675
        if p2x <= 30:
            p2x = 30
        if p2y <= 0:
            p2y = 0
        if p2y >= 339.5:
            p2y = 339.5
        if p3x >= 675:
            p3x = 675
        if p3x <= 30:
            p3x = 30
        if p3y <= 0:
            p3y = 0
        if p3y >= 339.5:
            p3y = 339.5
        if p4x >= 675:
            p4x = 675
        if p4x <= 30:
            p4x = 30
        if p4y <= 0:
            p4y = 0
        if p4y >= 339.5:
            p4y = 339.5
        if p5x >= 675:
            p5x = 675
        if p5x <= 30:
            p5x = 30
        if p5y <= 0:
            p5y = 0
        if p5y >= 339.5:
            p5y = 339.5

    def boundaryO(self):
        global pxo, pyo, p2xo, p2yo, p3xo, p3yo, p4xo, p4yo, p5xo, p5yo
        if pxo >= 1365:
            pxo = 1365
        if pxo <= 725:
            pxo = 725
        if pyo <=0:
            pyo = 0
        if pyo >= 339.5:
            pyo = 339.5
        if p2xo >= 1365:
            p2xo = 1365
        if p2xo <= 725:
            p2xo = 725
        if p2yo <= 0:
            p2yo = 0
        if p2yo >= 339.5:
            p2yo = 339.5
        if p3xo >= 1365:
            p3xo = 1365
        if p3xo <= 725:
            p3xo = 725
        if p3yo <= 0:
            p3yo = 0
        if p3yo >= 339.5:
            p3yo = 339.5
        if p4xo >= 1365:
            p4xo = 1365
        if p4xo <= 725:
            p4xo = 725
        if p4yo <= 0:
            p4yo = 0
        if p4yo >= 339.5:
            p4yo = 339.5
        if p5xo >= 1365:
            p5xo = 1365
        if p5xo <= 725:
            p5xo = 725
        if p5yo <= 0:
            p5yo = 0
        if p5yo >= 339.5:
            p5yo = 339.5

    def collide(self, y, x2, y2):
        if pygame.sprite.collide_rect(self, y):
            if status=="OFFENSE":
                if self.rect.x < x2:
                    self.movex = -0.5
                elif self.rect.x > x2:
                    self.movex = 0.5
                if self.rect.y < y2:
                    self.movey = -0.5
                elif self.rect.y > y2:
                    self.movey = 0.5
            else:
                if self.rect.x < x2:
                    self.movex = -0.3
                elif self.rect.x > x2:
                    self.movex = 0.3
                if self.rect.y < y2:
                    self.movey = -0.3
                elif self.rect.y > y2:
                    self.movey = 0.3
                
    def activecoord(self):
        if status == "DEFENSE":
            if self == p1:
                z = [px, py]
            elif self == p3:
                z = [p3x, p3y]
            elif self == p2:
                z = [p2x, p2y]
            elif self == p4:
                z = [p4x, p4y]
            elif self == p5:
                z = [p5x, p5y]
            return z
        elif status == "OFFENSE":
            if self == p1:
                z = [pxo, pyo]
            elif self == p3:
                z = [p3xo, p3yo]
            elif self == p2:
                z = [p2xo, p2yo]
            elif self == p4:
                z = [p4xo, p4yo]
            elif self == p5:
                z = [p5xo, p5yo]
            return z

    def movement(self, x, y):
        if pause ==False:

                
            
            self.movex += x
            self.movey += y
            if status == "DEFENSE":
                player.collide(self, o1, ox, oy)
                player.collide(self, o2, o2x, o2y)
                player.collide(self, o3, o3x, o3y)
                player.collide(self, o4, o4x, o4y)
                player.collide(self, o5, o5x, o5y)
            elif status == "OFFENSE":
                player.collide(self, o1, oxo, oyo)
                player.collide(self, o2, o2xo, o2yo)
                player.collide(self, o3, o3xo, o3yo)
                player.collide(self, o4, o4xo, o4yo)
                player.collide(self, o5, o5xo, o5yo)
            if status == "DEFENSE":
                if defplayer == "pg":
                    player.collide(self, p2, p2x, p2y)
                    player.collide(self, p3, p3x, p3y)
                    player.collide(self, p4, p4x, p4y)
                    player.collide(self, p5, p5x, p5y)
                elif defplayer == "sg":
                    player.collide(self, p1, px, py)
                    player.collide(self, p3, p3x, p3y)
                    player.collide(self, p4, p4x, p4y)
                    player.collide(self, p5, p5x, p5y)
                elif defplayer == "sf":
                    player.collide(self, p1, px, py)
                    player.collide(self, p2, p2x, p2y)
                    player.collide(self, p4, p4x, p4y)
                    player.collide(self, p5, p5x, p5y)
                elif defplayer == "pf":
                    player.collide(self, p1, px, py)
                    player.collide(self, p3, p3x, p3y)
                    player.collide(self, p2, p2x, p2y)
                    player.collide(self, p5, p5x, p5y)
                else:
                    player.collide(self, p1, px, py)
                    player.collide(self, p3, p3x, p3y)
                    player.collide(self, p4, p4x, p4y)
                    player.collide(self, p2, p2x, p2y)
            elif status == "OFFENSE":
                if activeplayer == "pg":
                    player.collide(self, p2, p2xo, p2yo)
                    player.collide(self, p3, p3xo, p3yo)
                    player.collide(self, p4, p4xo, p4yo)
                    player.collide(self, p5, p5xo, p5yo)
                elif activeplayer == "sg":
                    player.collide(self, p1, pxo, pyo)
                    player.collide(self, p3, p3xo, p3yo)
                    player.collide(self, p4, p4xo, p4yo)
                    player.collide(self, p5, p5xo, p5yo)
                elif activeplayer == "sf":
                    player.collide(self, p1, pxo, pyo)
                    player.collide(self, p2, p2xo, p2yo)
                    player.collide(self, p4, p4xo, p4yo)
                    player.collide(self, p5, p5xo, p5yo)
                elif activeplayer == "pf":
                    player.collide(self, p1, pxo, pyo)
                    player.collide(self, p3, p3xo, p3yo)
                    player.collide(self, p2, p2xo, p2yo)
                    player.collide(self, p5, p5xo, p5yo)
                else:
                    player.collide(self, p1, pxo, pyo)
                    player.collide(self, p3, p3xo, p3yo)
                    player.collide(self, p4, p4xo, p4yo)
                    player.collide(self, p2, p2xo, p2yo)

    def shot(self, x, y, opponent):
        shotprob = 0
        if TPO(player.activecoord(useplayer())[0], player.activecoord(useplayer())[1]):
            self.K = True
        else:
            self.K = False
        if math.dist(player.activecoord(useplayer()), [1331, 202.5]) <= 100:
            dis = 10
        elif math.dist(player.activecoord(useplayer()), [1331, 202.5]) <= 200 and math.dist(
                player.activecoord(useplayer()), [1331, 202.5]) > 100:
            dis = 8
        elif math.dist(player.activecoord(useplayer()), [1331, 202.5]) <= 300 and math.dist(
                player.activecoord(useplayer()), [1331, 202.5]) > 200:
            dis = 6
        elif math.dist(player.activecoord(useplayer()), [1331, 202.5]) <= 400 and math.dist(
                player.activecoord(useplayer()), [1331, 202.5]) > 300:
            dis = 4
        elif math.dist(player.activecoord(useplayer()), [1331, 202.5]) <= 550 and math.dist(
                player.activecoord(useplayer()), [1331, 202.5]) > 400:
            dis = 2
        else:
            dis = 0
        if self.K:
            if x[1] - y[1] >= 20:
                shotprob = 8 + random.randint(0, 2)
            elif x[1] - y[1] >= 15 and x[1] - y[1] < 20:
                shotprob = 7 + random.randint(0, 3)
            elif x[1] - y[1] >= 10 and x[1] - y[1] < 15:
                shotprob = 6 + random.randint(0, 4)
            elif x[1] - y[1] >= 7 and x[1] - y[1] < 10:
                shotprob = 5 + random.randint(0, 5)
            else:
                shotprob = 2 + random.randint(0, 8)
        else:
            if x[0] - y[0] >= 20:
                shotprob = 8 + random.randint(0, 2)
            elif x[0] - y[0] >= 15 and x[0] - y[0] < 20:
                shotprob = 7 + random.randint(0, 3)
            elif x[0] - y[0] >= 10 and x[0] - y[0] < 15:
                shotprob = 6 + random.randint(0, 4)
            elif x[0] - y[0] >= 7 and x[0] - y[0] < 10:
                shotprob = 5 + random.randint(0, 5)
            else:
                shotprob = 2 + random.randint(0, 8)
        if math.dist(player.activecoord(useplayer()), [opponent.rect.x, opponent.rect.y]) < 80:
            blockprob = random.randint(0, 1)
            if blockprob == 1:
                self.block = True
            else:
                self.block = False

            defprob = random.randint(0, 10)
        elif math.dist(player.activecoord(useplayer()), [opponent.rect.x, opponent.rect.y]) < 100 and math.dist(
                player.activecoord(useplayer()), [opponent.rect.x, opponent.rect.y]) >= 80:
            defprob = 2 + random.randint(0, 8)
            blockprob = random.randint(0, 3)
            if blockprob == 1:
                self.block = True
            else:
                self.block = False
        elif math.dist(player.activecoord(useplayer()), [opponent.rect.x, opponent.rect.y]) >= 100 and math.dist(
                player.activecoord(useplayer()), [opponent.rect.x, opponent.rect.y]) < 120:
            defprob = 4 + random.randint(0, 6)
            blockprob = random.randint(0, 9)
            if blockprob == 1:
                self.block = True
            else:
                self.block = False
        elif math.dist(player.activecoord(useplayer()), [opponent.rect.x, opponent.rect.y]) >= 120 and math.dist(
                player.activecoord(useplayer()), [opponent.rect.x, opponent.rect.y]) <= 140:
            self.block = False
            defprob = 6 + random.randint(0, 4)
        else:
            self.block = False
            defprob = 8 + random.randint(0, 2)
        self.shotchance = shotprob + defprob + dis
        self.shotchance = 25


    def score(self):
        global status, stat1
        if status == "OFFENSE":
            if self.block == True:
                self.score = 0
                stat1 = "B"
            elif self.shotchance >= 20:
                if self.K:
                    stat1 = "3P"
                    self.score = 25
                else:
                    self.score = 2

                    stat1 = "2P"
            elif self.shotchance < 20:
                stat1 = "M"
                self.score = 0
            return self.score
    def update(self):
        global UP, DOWN, RIGHT, LEFT, dz
        player1 = False
        player2 = False
        player3 = False
        player4 = False
        player5 = False
        global px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y
        global pxo, pyo, p2xo, p2yo, p3xo, p3yo, p4xo, p4yo, p5xo, p5yo
        global oldpx, oldpy, oldp2x, oldp2y, oldp3x, oldp3y, oldp4x, oldp4y, oldp5x, oldp5y
        global oldpxo, oldpyo, oldp2xo, oldp2yo, oldp3xo, oldp3yo, oldp4xo, oldp4yo, oldp5xo, oldp5yo
        
        if status == "DEFENSE":
            if defplayer == "pg":
                player1 = True
                px += self.movex*clock.tick(10)
                py += self.movey*clock.tick(10)
            elif defplayer == "sg":
                player2 = True
                p2x += self.movex*clock.tick(10)
                p2y += self.movey*clock.tick(10)
            elif defplayer == "sf":
                player3 = True
                p3x += self.movex*clock.tick(10)
                p3y += self.movey*clock.tick(10)
            elif defplayer == "pf":
                player4 = True
                p4x += self.movex*clock.tick(10)
                p4y += self.movey*clock.tick(10)
            elif defplayer == "c":
                player5 = True
                p5x += self.movex*clock.tick(10)
                p5y += self.movey*clock.tick(10)
            if notransit:
                player.boundaryD(self)
        elif status == "OFFENSE":

            if activeplayer == "pg":
                player1 = True
                pxo += self.movex*clock.tick(20)
                pyo += self.movey*clock.tick(20)
            elif activeplayer == "sg":
                player2 = True
                p2xo += self.movex*clock.tick(20)
                p2yo += self.movey*clock.tick(20)
            elif activeplayer == "sf":
                player3 = True
                p3xo += self.movex*clock.tick(20)
                p3yo += self.movey*clock.tick(20)
            elif activeplayer == "pf":
                player4 = True
                p4xo += self.movex*clock.tick(20)
                p4yo += self.movey*clock.tick(20)
            elif activeplayer == "c":
                player5 = True
                p5xo += self.movex*clock.tick(20)
                p5yo += self.movey*clock.tick(20)
            if notransit:
                player.boundaryO(self)
        if status == "DEFENSE":

            if oldpx > px + 0 and oldpy == py:
                s.blit(l1[1][dz], (px, py))
            elif oldpx + 0 < px and  oldpy == py:
                s.blit(l1[2][dz], (px, py))
            elif oldpx == px and  oldpy + 0 < py:
                s.blit(l1[0][dz], (px, py))
            elif oldpx == px and  oldpy > py + 0:
                s.blit(l1[3][dz], (px, py))
            elif oldpx > px + 0 and oldpy + 0 < py:
                s.blit(l1[1][dz], (px, py))
            elif oldpx + 0 < px and oldpy > py + 0:
                s.blit(l1[2][dz], (px, py))
            elif oldpx + 0 < px and oldpy + 0 < py:
                s.blit(l1[2][dz], (px, py))
            elif oldpx > px + 0 and oldpy > py + 0:
                s.blit(l1[1][dz], (px, py))
            else:
                s.blit(l1[0][0], (px, py))
            
            if oldp2x > p2x + 0 and oldp2y == p2y:
                s.blit(l2[1][dz], (p2x, p2y))
            elif oldp2x + 0 < p2x and  oldp2y == p2y:
                s.blit(l2[2][dz], (p2x, p2y))
            elif oldp2x == p2x and  oldp2y + 0 < p2y:
                s.blit(l2[0][dz], (p2x, p2y))
            elif oldp2x == p2x and  oldp2y > p2y + 0:
                s.blit(l2[3][dz], (p2x, p2y))
            elif oldp2x > p2x + 0 and oldp2y + 0 < p2y:
                s.blit(l2[1][dz], (p2x, p2y))
            elif oldp2x + 0 < p2x and oldp2y > p2y + 0:
                s.blit(l2[2][dz], (p2x, p2y))
            elif oldp2x + 0 < p2x and oldp2y + 0 < p2y:
                s.blit(l2[2][dz], (p2x, p2y))
            elif oldp2x > p2x + 0 and oldp2y > p2y + 0:
                s.blit(l2[1][dz], (p2x, p2y))
            else:
                s.blit(l2[0][0], (p2x, p2y))
            

            if oldp3x > p3x + 0 and oldp3y == p3y:
                s.blit(l3[1][dz], (p3x, p3y))
            elif oldp3x + 0 < p3x and  oldp3y == p3y:
                s.blit(l3[2][dz], (p3x, p3y))
            elif oldp3x == p3x and  oldp3y + 0 < p3y:
                s.blit(l3[0][dz], (p3x, p3y))
            elif oldp3x == p3x and  oldp3y > p3y + 0:
                s.blit(l3[3][dz], (p3x, p3y))
            elif oldp3x > p3x + 0 and oldp3y + 0 < p3y:
                s.blit(l3[1][dz], (p3x, p3y))
            elif oldp3x + 0 < p3x and oldp3y > p3y + 0:
                s.blit(l3[2][dz], (p3x, p3y))
            elif oldp3x + 0 < p3x and oldp3y + 0 < p3y:
                s.blit(l3[2][dz], (p3x, p3y))
            elif oldp3x > p3x + 0 and oldp3y > p3y + 0:
                s.blit(l3[1][dz], (p3x, p3y))
            else:
                s.blit(l3[0][0], (p3x, p3y))
            


            if oldp4x > p4x + 0 and oldp4y == p4y :
                s.blit(l4[1][dz], (p4x, p4y))
            elif oldp4x + 0 < p4x and  oldp4y == p4y:
                s.blit(l4[2][dz], (p4x, p4y))
            elif oldp4x == p4x and  oldp4y + 0 < p4y:
                s.blit(l4[0][dz], (p4x, p4y))
            elif oldp4x == p4x and  oldp4y > p4y + 0:
                s.blit(l4[3][dz], (p4x, p4y))
            elif oldp4x > p4x + 0 and oldp4y + 0 < p4y:
                s.blit(l4[1][dz], (p4x, p4y))
            elif oldp4x + 0 < p4x and oldp4y > p4y + 0:
                s.blit(l4[2][dz], (p4x, p4y))
            elif oldp4x + 0 < p4x and oldp4y + 0 < p4y:
                s.blit(l4[2][dz], (p4x, p4y))
            elif oldp4x > p4x + 0 and oldp4y > p4y + 0:
                s.blit(l4[1][dz], (p4x, p4y))
            else:
                s.blit(l4[0][0], (p4x, p4y))
            


            if oldp5x > p5x + 0 and oldp5y == p5y:
                s.blit(l5[1][dz], (p5x, p5y))
            elif oldp5x + 0 < p5x and oldp5y == p5y:
                s.blit(l5[2][dz], (p5x, p5y))
            elif oldp5x == p5x and  oldp5y + 0 < p5y:
                s.blit(l5[0][dz], (p5x, p5y))
            elif oldp5x == p5x and  oldp5y > p5y + 0:
                s.blit(l5[3][dz], (p5x, p5y))
            elif oldp5x > p5x + 0 and oldp5y + 0 < p5y:
                s.blit(l5[1][dz], (p5x, p5y))
            elif oldp5x + 0 < p5x and oldp5y > p5y + 0:
                s.blit(l5[2][dz], (p5x, p5y))
            elif oldp5x + 0 < p5x and oldp5y + 0 < p5y:
                s.blit(l5[2][dz], (p5x, p5y))
            elif oldp5x > p5x + 0 and oldp5y > p5y + 0:
                s.blit(l5[1][dz], (p5x, p5y))
            else:
                s.blit(l5[0][0], (p5x, p5y))
            
        elif status == "OFFENSE":
          
            if oldpxo > pxo + 0 and oldpyo == pyo:
                s.blit(l1[1][dz], (pxo, pyo))
            elif oldpxo + 0 < pxo and oldpyo == pyo:
                s.blit(l1[2][dz], (pxo, pyo))
            elif oldpxo == pxo and oldpyo + 0 < pyo:
                s.blit(l1[0][dz], (pxo, pyo))
            elif oldpxo == pxo and oldpyo > pyo + 0:
                s.blit(l1[3][dz], (pxo, pyo))
            elif oldpxo > pxo + 0 and oldpyo + 0 < pyo:
                s.blit(l1[1][dz], (pxo, pyo))
            elif oldpxo + 0 < pxo and oldpyo > pyo + 0:
                s.blit(l1[2][dz], (pxo, pyo))
            elif oldpxo + 0 < pxo and oldpyo + 0 < pyo:
                s.blit(l1[2][dz], (pxo, pyo))
            elif oldpxo > pxo + 0 and oldpyo > pyo + 0:
                s.blit(l1[1][dz], (pxo, pyo))
            else:
                s.blit(l1[0][0], (pxo, pyo))

            

            
            if oldp2xo > p2xo + 0 and oldp2yo == p2yo:
                s.blit(l2[1][dz], (p2xo, p2yo))
            elif oldp2xo + 0 < p2xo and oldp2yo == p2yo:
                s.blit(l2[2][dz], (p2xo, p2yo))
            elif oldp2xo == p2xo and oldp2yo + 0 < p2yo:
                s.blit(l2[0][dz], (p2xo, p2yo))
            elif oldp2xo == p2xo and oldp2yo > p2yo + 0:
                s.blit(l2[3][dz], (p2xo, p2yo))
            elif oldp2xo > p2xo + 0 and oldp2yo + 0 < p2yo:
                s.blit(l2[1][dz], (p2xo, p2yo))
            elif oldp2xo + 0 < p2xo and oldp2yo > p2yo + 0:
                s.blit(l2[2][dz], (p2xo, p2yo))
            elif oldp2xo + 0 < p2xo and oldp2yo + 0 < p2yo:
                s.blit(l2[2][dz], (p2xo, p2yo))
            elif oldp2xo > p2xo + 0 and oldp2yo > p2yo + 0:
                s.blit(l2[1][dz], (p2xo, p2yo))
            else:
                s.blit(l2[0][0], (p2xo, p2yo))
            
            if oldp3xo > p3xo + 0 and oldp3yo == p3yo:
                s.blit(l3[1][dz], (p3xo, p3yo))
            elif oldp3xo + 0 < p3xo and oldp3yo == p3yo:
                s.blit(l3[2][dz], (p3xo, p3yo))
            elif oldp3xo == p3xo and oldp3yo + 0 < p3yo:
                s.blit(l3[0][dz], (p3xo, p3yo))
            elif oldp3xo == p3xo and oldp3yo > p3yo + 0:
                s.blit(l3[3][dz], (p3xo, p3yo))
            elif oldp3xo > p3xo + 0 and oldp3yo + 0 < p3yo:
                s.blit(l3[1][dz], (p3xo, p3yo))
            elif oldp3xo + 0 < p3xo and oldp3yo > p3yo + 0:
                s.blit(l3[2][dz], (p3xo, p3yo))
            elif oldp3xo + 0 < p3xo and oldp3yo + 0 < p3yo:
                s.blit(l3[2][dz], (p3xo, p3yo))
            elif oldp3xo > p3xo + 0 and oldp3yo > p3yo + 0:
                s.blit(l3[1][dz], (p3xo, p3yo))
            else:
                s.blit(l3[0][0], (p3xo, p3yo))
            
            if oldp4xo > p4xo + 0 and oldp4yo == p4yo:
                s.blit(l4[1][dz], (p4xo, p4yo))
            elif oldp4xo + 0 < p4xo and oldp4yo == p4yo:
                s.blit(l4[2][dz], (p4xo, p4yo))
            elif oldp4xo == p4xo and oldp4yo + 0 < p4yo:
                s.blit(l4[0][dz], (p4xo, p4yo))
            elif oldp4xo == p4xo and oldp4yo > p4yo + 0:
                s.blit(l4[3][dz], (p4xo, p4yo))
            elif oldp4xo > p4xo + 0 and oldp4yo + 0 < p4yo:
                s.blit(l4[1][dz], (p4xo, p4yo))
            elif oldp4xo + 0 < p4xo and oldp4yo > p4yo + 0:
                s.blit(l4[2][dz], (p4xo, p4yo))
            elif oldp4xo + 0 < p4xo and oldp4yo + 0 < p4yo:
                s.blit(l4[2][dz], (p4xo, p4yo))
            elif oldp4xo > p4xo + 0 and oldp4yo > p4yo + 0:
                s.blit(l4[1][dz], (p4xo, p4yo))
            else:
                s.blit(l4[0][0], (p4xo, p4yo))
            
            if oldp5xo > p5xo + 0 and oldp5yo == p5yo:
                s.blit(l5[1][dz], (p5xo, p5yo))
            elif oldp5xo + 0 < p5xo and oldp5yo == p5yo:
                s.blit(l5[2][dz], (p5xo, p5yo))
            elif oldp5xo == p5xo and oldp5yo + 0 < p5yo:
                s.blit(l5[0][dz], (p5xo, p5yo))
            elif oldp5xo == p5xo and oldp5yo > p5yo + 0:
                s.blit(l5[3][dz], (p5xo, p5yo))
            elif oldp5xo > p5xo + 0 and oldp5yo + 0 < p5yo:
                s.blit(l5[1][dz], (p5xo, p5yo))
            elif oldp5xo + 0 < p5xo and oldp5yo > p5yo + 0:
                s.blit(l5[2][dz], (p5xo, p5yo))
            elif oldp5xo + 0 < p5xo and oldp5yo + 0 < p5yo:
                s.blit(l5[2][dz], (p5xo, p5yo))
            elif oldp5xo > p5xo + 0 and oldp5yo > p5yo + 0:
                s.blit(l5[1][dz], (p5xo, p5yo))
            else:
                s.blit(l5[0][0], (p5xo, p5yo))
            
        if dz +1 == 4 :
            dz= 0
        else :
            dz = dz +1
        
        oldpxo, oldpyo, oldp2xo, oldp2yo, oldp3xo, oldp3yo, oldp4xo, oldp4yo, oldp5xo, oldp5yo = pxo, pyo, p2xo, p2yo, p3xo, p3yo, p4xo, p4yo, p5xo, p5yo
        oldpx, oldpy, oldp2x, oldp2y, oldp3x, oldp3y, oldp4x, oldp4y, oldp5x, oldp5y = px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y
class ball:
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.rad = 10
        self.ballmovex, self.ballmovey = 0, 0
        self.screen = s
        self.state = "P"
        self.number = 0

    def boundaryO(self):
        if self.x >= 1375:
            self.x = 1375
        if self.x <= 30:
            self.x = 30
        if self.y <= 15:
            self.y = 15
        if self.y >= 390:
            self.y = 390

    def boundaryD(self):
        if self.x >= 675:
            self.x = 675
        if self.x <= 30:
            self.x = 30
        if self.y <= 15:
            self.y = 15
        if self.y >= 390:
            self.y = 390

    def state(self,x): 
        self.state=x
    def state2(self):
        return self.state

    def collision(self, x2, y2):
        if math.dist([self.x],[x2])<=30:
            if math.dist([self.y],[y2])<=30:
                
            
                self.ballmovex = 0
                self.ballmovey = 0
                return True

    def collisionb(self, x2, y2):
        
        if math.dist([self.x], [x2]) <= 50:
            if math.dist([self.y], [y2]) <= 30:
                self.ballmovex = 0
                self.ballmovey = 0
                return True


    def movement(self, x2, y2):

        self.number = max(abs(x2 - self.x), abs(y2 - self.y))
        self.ballmovex = float(x2 - self.x) / self.number
        self.ballmovey = float(y2 - self.y) / self.number
        self.state = "M"


    def draw(self):
        global shoot, movement, status, coll, collo, setO, setD, stat1, blittime
        if status == "DEFENSE":
            if shoot == False:
                if notransit == True:
                    if self.state == "M":
                        if ball.collision(self, px, py):
                            self.state = "D1"
                            coll = True
                        elif ball.collision(self, p2x, p2y):
                            self.state = "D2"
                            coll = True
                        elif ball.collision(self, p3x, p3y):
                            self.state = "D3"
                            coll = True
                        elif ball.collision(self, p4x, p4y):
                            self.state = "D4"
                            coll = True
                        elif ball.collision(self, p5x, p5y):
                            self.state = "D5"
                            coll = True
                    if ball.collision(self, ox, oy) or ball.collision(self, o2x, o2y) or ball.collision(self, o3x,
                                                                                                        o3y) or ball.collision(
                            self, o4x, o4y) or ball.collision(self, o5x, o5y):
                        self.state = "P"
                        movement = True
                
                if coll:
                    blittime = pygame.time.get_ticks() + 1500
                    stat1 = "I"
                    setD=True
            if ball.collisionb(self, cx, cy):
                setD = True
            if sec==2:
                blittime=pygame.time.get_ticks()+1500
                stat1="F"
                setD=True
            if setD == True:
                self.state = "D1"
                self.x=px+70
                self.y=py+60
                transitiond()
            ball.boundaryD(self)
            if self.state == "M":

                self.x += self.ballmovex * 50
                self.y += self.ballmovey * 50
            elif self.state == "P":
                if offopp == "pg":
                    if movestat1=="U":
                        self.x = ox + 50
                        self.y = oy + 20
                    elif movestat1=="D":
                        self.x=ox+50
                        self.y=oy+90
                    elif movestat1=="L":
                        self.x=ox
                        self.y=oy+60
                    elif movestat1=="R":
                        self.x=ox+75
                        self.y=oy+60
                    else:
                        self.x=ox+60
                        self.y=oy+50
                elif offopp == "sg":
                    if movestat2=="U":
                        self.x = o2x + 50
                        self.y = o2y + 20
                    elif movestat2=="D":
                        self.x=o2x+50
                        self.y=o2y+90
                    elif movestat2=="L":
                        self.x=o2x
                        self.y=o2y+60
                    elif movestat2=="R":
                        self.x=o2x+75
                        self.y=o2y+60
                    else:
                        self.x=o2x+60
                        self.y=o2y+50
                elif offopp == "sf":
                    if movestat3=="U":
                        self.x = o3x + 50
                        self.y = o3y + 20
                    elif movestat3=="D":
                        self.x=o3x+50
                        self.y=o3y+90
                    elif movestat3=="L":
                        self.x=o3x
                        self.y=o3y+60
                    elif movestat3=="R":
                        self.x=o3x+75
                        self.y=o3y+60
                    else:
                        self.x=o3x+60
                        self.y=o3y+50
                elif offopp == "pf":
                    if movestat4=="U":
                        self.x = o4x + 50
                        self.y = o4y + 20
                    elif movestat4=="D":
                        self.x=o4x+50
                        self.y=o4y+90
                    elif movestat4=="L":
                        self.x=o4x
                        self.y=o4y+60
                    elif movestat4=="R":
                        self.x=o4x+75
                        self.y=o4y+60
                    else:
                        self.x=o4x+60
                        self.y=o4y+50
                elif offopp == "c":
                    if movestat5=="U":
                        self.x = o5x + 50
                        self.y = o5y + 20
                    elif movestat5=="D":
                        self.x=o5x+50
                        self.y=o5y+90
                    elif movestat5=="L":
                        self.x=o5x
                        self.y=o5y+60
                    elif movestat5=="R":
                        self.x=o5x+75
                        self.y=o5y+60
                    else:
                        self.x=o5x+60
                        self.y=o5y+50
            else:
                if self.state == "D1":
                    self.x = px + 75
                    self.y = py + 60
                    defplayer = "pg"
                elif self.state == "D2":
                    self.x = p2x + 75
                    self.y = p2y + 60
                    defplayer = "sg"
                elif self.state == "D3":
                    self.x = p3x + 75
                    self.y = p3y + 50
                    defplayer = "sf"
                elif self.state == "D4":
                    self.x = p4x + 75
                    self.y = p4y + 60
                    defplayer = "pf"
                elif self.state == "D5":
                    self.x = p5x + 75
                    self.y = p5y + 60
                    defplayer = "c"
                transitiond()

        elif status == "OFFENSE":
            if shoot == False:
                if notransit == True:
                    if self.state == "M":
                        if ball.collision(self, pxo, pyo) or ball.collision(self, p2xo, p2yo) or ball.collision(self, p3xo,p3yo) or ball.collision(self, p4xo, p4yo) or ball.collision(self, p5xo, p5yo):
                            self.state = "P"
                            collo=False
                        elif ball.collision(self, oxo, oyo):
                            self.state = "D1"
                            collo = True
                        elif ball.collision(self, o2xo, o2yo):
                            self.state = "D2"
                            collo = True
                        elif ball.collision(self, o3xo, o3yo):
                            self.state = "D3"
                            collo = True
                        elif ball.collision(self, o4xo, o4yo):
                            self.state = "D4"
                            collo = True
                        elif ball.collision(self, o5xo, o5yo):
                            self.state = "D5"
                            collo = True
                        
                if collo == True:
                    blittime = pygame.time.get_ticks() + 1500
                    stat1 = "I"
            
            if ball.collisionb(self, c2x, c2y):
                setO = True
            if sec<=2:
                blittime=pygame.time.get_ticks()+1500
                stat1="F"
                setO=True
                
            if setO == True:
                
                self.x = oxo
                self.y = oyo + 60
                transitiono()
            ball.boundaryO(self)
            if self.state == "M":
                self.x += self.ballmovex*50
                
                self.y += self.ballmovey*50
                
            elif self.state == "P":
                if activeplayer == "pg":
                    if UP:
                        self.x = pxo + 50
                        self.y = pyo + 20
                    elif DOWN:
                        self.x=pxo+50
                        self.y=pyo+90
                    elif RIGHT:
                        self.x=pxo+75
                        self.y=pyo+60
                    elif LEFT:
                        self.x=pxo
                        self.y=pyo+60
                    else:
                        self.x=pxo+60
                        self.y=pyo+50
                elif activeplayer == "sg":
                    if UP:
                        self.x = p2xo + 50
                        self.y = p2yo + 20
                    elif DOWN:
                        self.x=p2xo+50
                        self.y=p2yo+90
                    elif RIGHT:
                        self.x=p2xo+75
                        self.y=p2yo+60
                    elif LEFT:
                        self.x=p2xo
                        self.y=p2yo+60
                    else:
                        self.x=p2xo+60
                        self.y=p2yo+50
                elif activeplayer == "sf":
                    if UP:
                        self.x = p3xo + 50
                        self.y = p3yo + 20
                    elif DOWN:
                        self.x=p3xo+50
                        self.y=p3yo+90
                    elif RIGHT:
                        self.x=p3xo+75
                        self.y=p3yo+60
                    elif LEFT:
                        self.x=p3xo
                        self.y=p3yo+60
                    else:
                        self.x=p3xo+60
                        self.y=p3yo+50
                elif activeplayer == "pf":
                    if UP:
                        self.x = p4xo + 50
                        self.y = p4yo + 20
                    elif DOWN:
                        self.x=p4xo+50
                        self.y=p4yo+90
                    elif RIGHT:
                        self.x=p4xo+75
                        self.y=p4yo+60
                    elif LEFT:
                        self.x=p4xo
                        self.y=p4yo+60
                    else:
                        self.x=p4xo+60
                        self.y=p4yo+50
                elif activeplayer == "c":
                    if UP:
                        self.x = p5xo + 50
                        self.y = p5yo + 20
                    elif DOWN:
                        self.x=p5xo+50
                        self.y=p5yo+90
                    elif RIGHT:
                        self.x=p5xo+75
                        self.y=p5yo+60
                    elif LEFT:
                        self.x=p5xo
                        self.y=p5yo+60
                    else:
                        self.x=p5xo+60
                        self.y=p5yo+50
            else:
                if self.state == "D1":
                    self.x = oxo
                    self.y = oyo+60
                elif self.state == "D2":
                    self.x = o2xo
                    self.y = o2yo+60
                elif self.state == "D3":
                    self.x = o3xo
                    self.y = o3yo+60
                elif self.state == "D4":
                    self.x = o4xo
                    self.y = o4yo+60
                elif self.state == "D5":
                    self.x = o5xo
                    self.y = o5yo+60
                transitiono()
        pygame.draw.circle(s, (255, 140, 0), [self.x, self.y], self.rad)
def curvalD(): 
    if activedefender()[0]==o1:
        return valo1[3:5]
    elif activedefender()[0]==o2:
        return valo2[3:5]
    elif activedefender()[0]==o3:
        return valo3[3:5]
    elif activedefender()[0]==o4:
        return valo4[3:5]
    elif activedefender()[0]==o5:
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
    if activepp()[1]=='pg':
        return valp1[3:5]
    elif activepp()[1]=='sg':
        return valp2[3:5]
    elif activepp()[1]=='sf':
        return valp3[3:5]
    elif activepp()[1]=='pf':
        return valp4[3:5]
    elif activepp()[1]=='c':
        return valp5[3:5]
def plycurvalO():
    if activeplayer=='pg':
        return valp1[1:3]
    elif activeplayer=='sg':
        return valp2[1:3]
    elif activeplayer=='sf':
        return valp3[1:3]
    elif activeplayer=='pf':
        return valp4[1:3]
    elif activeplayer=='c':
        return valp5[1:3]
def transitiono():
    global oxo, oyo, o2xo, o2yo, o3xo, o3yo, o4xo, o4yo, o5xo, o5yo
    global pxo, pyo, p2xo, p2yo, p3xo, p3yo, p4xo, p4yo, p5xo, p5yo
    global status, setO, sec, a1, collo, stat1,pass1,pass2,pass3,pass4,pass5
    global notransit, shoot, dtime, otime, movement,defplayer,traover
    notransit = False
    sec = 5
    traover=False
    collo = False
    shoot = False
    ax, ay = 500, 160
    bx, by = 285, 50
    cx, cy = 285, 320
    dx, dy = 90, 110
    ex, ey = 85, 250
    fx, fy = 675, 160
    gx, gy = 365, 0
    hx, hy = 370, 339.5
    ix, iy = 145, 70
    jx, jy = 145, 260
    step1 = max(abs(ax - pxo), abs(ay - pyo))
    step2 = max(abs(bx - p2xo), abs(by - p2yo))
    step3 = max(abs(cx - p3xo), abs(cy - p3yo))
    step4 = max(abs(dx - p4xo), abs(dy - p4yo))
    step5 = max(abs(ex - p5xo), abs(ey - p5yo))
    step6 = max(abs(fx - oxo), abs(fy - oyo))
    step7 = max(abs(gx - o2xo), abs(gy - o2yo))
    step8 = max(abs(hx - o3xo), abs(hy - o3yo))
    step9 = max(abs(ix - o4xo), abs(iy - o4yo))
    step10 = max(abs(jx - o5xo), abs(jy - o5yo))
    if math.dist([pxo, pyo], [ax, ay]) <= 10:
        pxo, pyo = ax, ay
        step1 = 0
    else:
        pxo += ((ax - pxo) / step1)*20
        pyo += ((ay - pyo) / step1)*20
    if math.dist([p2xo, p2yo], [bx, by]) <= 10:
        p2xo, p2yo = bx, by
        step2 = 0
    else:
        p2xo += ((bx - p2xo) / step2)*20
        p2yo += ((by - p2yo) / step2)*20
    if math.dist([p3xo, p3yo], [cx, cy]) <= 10:
        p3xo, p3yo = cx, cy
        step3 = 0
    else:
        p3xo += ((cx - p3xo) / step3)*20
        p3yo += ((cy - p3yo) / step3)*20
        
    if math.dist([p4xo, p4yo], [dx, dy]) <= 10:
        p4xo, p4yo = dx, dy
        step4 = 0
    else:
        p4xo += ((dx - p4xo) / step4)*20
        p4yo += ((dy - p4yo) / step4)*20
    if math.dist([p5xo, p5yo], [ex, ey]) <= 10:
        p5xo, p5yo = ex, ey
        step5 = 0
    else:
        p5xo += ((ex - p5xo) / step5)*20
        p5yo += ((ey - p5yo) / step5)*20
    if math.dist([oxo, oyo], [fx, fy]) <= 10:
        oxo, oyo = fx, fy
        step6 = 0
    else:
        oxo += ((fx - oxo) / step6)*20
        oyo += ((fy - oyo) / step6)*20
    if math.dist([o2xo, o2yo], [gx, gy]) <= 10:
        o2xo, o2yo = gx, gy

    else:
        o2xo += ((gx - o2xo) / step7)*20
        o2yo += ((gy - o2yo) / step7)*20
        
    if math.dist([o3xo, o3yo], [hx, hy]) <= 11:
        o3xo, o3yo = hx, hy
    else:
        o3xo += ((hx - o3xo) / step8)*20
        o3yo += ((hy - o3yo) / step8)*20
        
    if math.dist([o4xo, o4yo], [ix, iy]) <= 10:
        o4xo, o4yo = ix, iy
    else:
        o4xo += ((ix - o4xo) / step9)*20
        o4yo += ((iy - o4yo) / step9)*20
        
    if math.dist([o5xo, o5yo], [jx, jy]) <= 10:
        o5xo, o5yo = jx, jy
        
    else:
        o5xo += ((jx - o5xo) / step10)*20
        o5yo += ((jy - o5yo) / step10)*20
        
    if step1 == 0 and step2 == 0 and step3 == 0 and step4 == 0 and step5 == 0 and step6 == 0 and step7 == 0 and step8 == 0 and step9 == 0 and step10 == 0:
        notransit=True
        a1 = random.randint(1, 10)
        dtime = pygame.time.get_ticks() + 21000
        otime = 0
        defplayer = "pg"
        ball.state(b1, "P")
        activeopp = "pg"
        setO = False
        stat1 = "P"
        status = "DEFENSE"
        pass1,pass2,pass3,pass4,pass5=True,True,True,True,True
        pxo, pyo, p2xo, p2yo, p3xo, p3yo, p4xo, p4yo, p5xo, p5yo = 725, 160, 1050, 0, 1050, 339.5, 1250, 70, 1250, 260
        oxo, oyo, o2xo, o2yo, o3xo, o3yo, o4xo, o4yo, o5xo, o5yo = 925, 160, 1100, 30, 1100, 320, 1300, 110, 1300, 240


def transitiond():
    global px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y
    global ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y
    global status, coll, setD, sec, stat1
    global notransit,shoot, dtime, otime, activeplayer, movement,traover,happened
    happened=True
    notransit = False
    sec=5
    coll = False
    shoot = False
    ax, ay = 725, 160
    bx, by = 1050, 0
    cx, cy = 1050, 339.5
    dx, dy = 1250, 70
    ex, ey = 1250, 260
    fx, fy = 925, 160
    gx, gy = 1100, 30
    hx, hy = 1100, 320
    ix, iy = 1300, 110
    jx, jy = 1300, 240
    step1 = max(abs(ax - px), abs(ay - py))
    step2 = max(abs(bx - p2x), abs(by - p2y))
    step3 = max(abs(cx - p3x), abs(cy - p3y))
    step4 = max(abs(dx - p4x), abs(dy - p4y))
    step5 = max(abs(ex - p5x), abs(ey - p5y))
    step6 = max(abs(fx - ox), abs(fy - oy))
    step7 = max(abs(gx - o2x), abs(gy - o2y))
    step8 = max(abs(hx - o3x), abs(hy - o3y))
    step9 = max(abs(ix - o4x), abs(iy - o4y))
    step10 = max(abs(jx - o5x), abs(jy - o5y))
    if math.dist([px, py], [ax, ay]) <= 15:
        px, py = ax, ay
        step1 = 0
    else:
        px += ((ax - px) / step1)*20
        py += ((ay - py) / step1)*20
    if math.dist([p2x, p2y], [bx, by]) <= 15:
        p2x, p2y = bx, by
        step2 = 0
    else:
        p2x += ((bx - p2x) / step2)*20
        p2y += ((by - p2y) / step2)*20
    if math.dist([p3x, p3y], [cx, cy]) <= 15:
        p3x, p3y = cx, cy
        step3 = 0
    else:
        p3x += ((cx - p3x) / step3)*20
        p3y += ((cy - p3y) / step3)*20
    if math.dist([p4x, p4y], [dx, dy]) <= 15:
        p4x, p4y = dx, dy
        step4 = 0
    else:
        p4x += ((dx - p4x) / step4)*20
        p4y += ((dy - p4y) / step4)*20
    if math.dist([p5x, p5y], [ex, ey]) <= 15:
        p5x, p5y = ex, ey
        step5 = 0
    else:
        p5x += ((ex - p5x) / step5)*20
        p5y += ((ey - p5y) / step5)*20
    if math.dist([ox, oy], [fx, fy]) <= 15:
        ox, oy = fx, fy
        step6 = 0
    else:
        ox += ((fx - ox) / step6)*20
        oy += ((fy - oy) / step6)*20
    if math.dist([o2x, o2y], [gx, gy]) <= 15:
        o2x, o2y = gx, gy
        step7=0
    else:
        o2x += ((gx - o2x) / step7)*20
        o2y += ((gy - o2y) / step7)*20
        
    if math.dist([o3x, o3y], [hx, hy]) <= 15:
        o3x, o3y = hx, hy
        step8=0
    else:
        o3x += ((hx - o3x) / step8)*20
        o3y += ((hy - o3y) / step8)*20
        
    if math.dist([o4x, o4y], [ix, iy]) <=15:
        o4x, o4y = ix, iy
        step9=0
    else:
        o4x += ((ix - o4x) / step9)*20
        o4y += ((iy - o4y) / step9)*20
        
    if math.dist([o5x, o5y], [jx, jy]) <= 15:
        o5x, o5y = jx, jy
        step10=0
        
    else:
        o5x += ((jx - o5x) / step10)*20
        o5y += ((jy - o5y) / step10)*20
    if step1 == 0 and step2 == 0 and step3 == 0 and step4 == 0 and step5 == 0 and step6 == 0 and step7 == 0 and step8 == 0 and step9 == 0 and step10 == 0:
        traover = True
        coll=False
        setD = False
        ball.state(B2, "P")
        dtime = 0
        stat1='P'
        movement = True
        activeplayer = "pg"
        otime = pygame.time.get_ticks() + 21000
        status = "OFFENSE"
        px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y = 500, 160, 285, 50, 285, 320, 90, 110, 85, 250
        ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y = 675, 160, 365, 0, 370, 339.5, 145, 70, 145, 260
            

def over(): # after game finisheds
    if scp>=5 or sc>=5:
        abc(s1,s2,s3,s4,s5,k1,k2,k3,k4,k5,valp1,valp2,valp3,valp4,valp5,valo1,valo2,valo3,valo4,valo5)
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
    img=Image.open("icon.png")
    img=ImageTk.PhotoImage(img)
    root.iconphoto(False,img)
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
        img=Image.open("icon.png")
        img=ImageTk.PhotoImage(img)
        new.iconphoto(False,img)
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
        def g():
            messagebox.showinfo("How to play?","Press the arrow keys or W,A,S,D to move your players and the spacebar to shoot, to pass or switch between players use the number key (1 - Point Guard, 2- Shooting Guard, 3- Small Forward, 4- Power Forward, 5- Center). On defense, player movement is NOT automated and you will have to move each player by switching. You can see each player's stats below in the cards and plan accordingly. The first team to reach 21 wins. Good Luck, May the force be with you.")
            
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
                a=messagebox.askquestion("READY","By pressing ok you will close the entire draft section and move to game. Music will be queued from this point and you will not be able to change it in-game. We recommend looking at the instructions first. Press yes only if you are ready")
                if a == "yes":
                    new.destroy()
                    root.destroy()
                    RUN=True
        
            
            
        frame2.update()
        canvas_container.configure(yscrollcommand=myscrollbar.set, scrollregion="0 0 0 %s" % frame2.winfo_height())
        canvas_container.pack(side=RIGHT)
        myscrollbar.pack(side=RIGHT, fill=Y)
        b1=Button(new,text="Proceed", command=mainl)
        b1.place(x=800,y=100,height=50,width=150)
        b2=Button(new,text="Delete",state="disabled",command=dele)
        b2.place(x=800,y=300,height=50,width=150)
        m=Button(new,text="Music Settings",command=q)
        m.place(x=800,y=500,height=50,width=150)
        k=Button(new,text="How to Play?",command=g)
        k.place(x=800,y=700,height=50,width=150)
        frame_container.pack()



    def sg():
        new2=Toplevel(root)
        img=Image.open("icon.png")
        img=ImageTk.PhotoImage(img)
        new2.iconphoto(False,img)
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
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image,points) select * from players where position='SG' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("Error", "You already have a Shooting Guard")
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
        img=Image.open("icon.png")
        img=ImageTk.PhotoImage(img)
        new2.iconphoto(False,img)
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
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image,points) select * from players where position='PF' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("Error", "You already have a Power Forward")
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
        img=Image.open("icon.png")
        img=ImageTk.PhotoImage(img)
        new2.iconphoto(False,img)
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
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image,points) select * from players where position='C' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("Error", "You already have a Center")
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
        img=Image.open("icon.png")
        img=ImageTk.PhotoImage(img)
        new2.iconphoto(False,img)
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
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image,points) select * from players where position='SF' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("Error", "You already have a Small Forward")
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
        img=Image.open("icon.png")
        img=ImageTk.PhotoImage(img)
        new3.iconphoto(False,img)
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
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image,points) select * from players where position='PG' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("Error", "You already have a Point Guard")
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
        img=Image.open("icon.png")
        img=ImageTk.PhotoImage(img)
        new.iconphoto(False,img)
        new.geometry('650x650')
        new.title("Music Settings")
        new.attributes("-topmost", True)
        width,height=650,650
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
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()
        def stop():
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
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
        l3=Radiobutton(new,command=stop,text="Stop Music")
        l3.place(x=250,y=600)
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
img=Image.open("icon.png")
img=ImageTk.PhotoImage(img)

root.iconphoto(False,img)
pygame.mixer.music.load("STW.mp3")
pygame.mixer.music.set_volume(0.2)
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
    global RUN
    RUN=True
    root.destroy()
def q():
    
    new=Toplevel(root)
    img=Image.open("icon.png")
    img=ImageTk.PhotoImage(img)
    new.iconphoto(False,img)
    new.geometry('650x650')
    new.title("Music Settings")
    new.attributes("-topmost", True)
    width,height=650,650
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
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()
    def stop():
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
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
    l3=Radiobutton(new,command=stop,text="Stop Music")
    l3.place(x=250,y=600)

    messagebox.showinfo("Guide","Click on any radio button to change the song")
image = Image.open('courtn3.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)
a=Button(root,text="BEGIN GAME",command=k)
a.place(x=380,y=600,height=100,width=250)
n=Button(root,text="Quit",command=s)
n.place(x=830,y=40,height=40,width=150)
m=Button(root,text="Music Settings",command=q)
m.place(x=425,y=750,height=50,width=150)
root.mainloop()
if RUN==True:
    s = pygame.display.set_mode([1450, 800])
    pygame.display.set_caption("Swisheroo")
    COURT = pygame.image.load("Courtn2.png").convert()
    icon = pygame.image.load("icon2.jpeg").convert()
    pygame.display.set_icon(icon)
    l1 = [[pygame.image.load("down1.png").convert_alpha(), pygame.image.load("down2.png").convert_alpha(),
          pygame.image.load("down3.png").convert_alpha(), pygame.image.load("down4.png").convert_alpha()],
          [pygame.image.load("left1.png").convert_alpha(), pygame.image.load("left2.png").convert_alpha(),
          pygame.image.load("left3.png").convert_alpha(), pygame.image.load("left4.png").convert_alpha()],
          [pygame.image.load("right1.png").convert_alpha(),pygame.image.load("right2.png").convert_alpha(),
          pygame.image.load("right3.png").convert_alpha(),pygame.image.load("right4.png").convert_alpha()],
          [pygame.image.load("up1.png").convert_alpha(),pygame.image.load("up2.png").convert_alpha(),
          pygame.image.load("up3.png").convert_alpha(),pygame.image.load("up4.png").convert_alpha()]]
    for i in l1:
        for j in i:
            j.set_colorkey((255,255,255))
    l2 = [[pygame.image.load("down1.png").convert_alpha(), pygame.image.load("down2.png").convert_alpha(),
          pygame.image.load("down3.png").convert_alpha(), pygame.image.load("down4.png").convert_alpha()],
          [pygame.image.load("left1.png").convert_alpha(), pygame.image.load("left2.png").convert_alpha(),
          pygame.image.load("left3.png").convert_alpha(), pygame.image.load("left4.png").convert_alpha()],
          [pygame.image.load("right1.png").convert_alpha(),pygame.image.load("right2.png").convert_alpha(),
          pygame.image.load("right3.png").convert_alpha(),pygame.image.load("right4.png").convert_alpha()],
          [pygame.image.load("up1.png").convert_alpha(),pygame.image.load("up2.png").convert_alpha(),
          pygame.image.load("up3.png").convert_alpha(),pygame.image.load("up4.png").convert_alpha()]]
    for i in l2:
        for j in i:
            j.set_colorkey((255,255,255))
    l3 = [[pygame.image.load("down1.png").convert_alpha(), pygame.image.load("down2.png").convert_alpha(),
          pygame.image.load("down3.png").convert_alpha(), pygame.image.load("down4.png").convert_alpha()],
          [pygame.image.load("left1.png").convert_alpha(), pygame.image.load("left2.png").convert_alpha(),
          pygame.image.load("left3.png").convert_alpha(), pygame.image.load("left4.png").convert_alpha()],
          [pygame.image.load("right1.png").convert_alpha(),pygame.image.load("right2.png").convert_alpha(),
          pygame.image.load("right3.png").convert_alpha(),pygame.image.load("right4.png").convert_alpha()],
          [pygame.image.load("up1.png").convert_alpha(),pygame.image.load("up2.png").convert_alpha(),
          pygame.image.load("up3.png").convert_alpha(),pygame.image.load("up4.png").convert_alpha()]]
    for i in l3:
        for j in i:
            j.set_colorkey((255,255,255))
    l4 = [[pygame.image.load("down1.png").convert_alpha(), pygame.image.load("down2.png").convert_alpha(),
          pygame.image.load("down3.png").convert_alpha(), pygame.image.load("down4.png").convert_alpha()],
          [pygame.image.load("left1.png").convert_alpha(), pygame.image.load("left2.png").convert_alpha(),
          pygame.image.load("left3.png").convert_alpha(), pygame.image.load("left4.png").convert_alpha()],
          [pygame.image.load("right1.png").convert_alpha(),pygame.image.load("right2.png").convert_alpha(),
          pygame.image.load("right3.png").convert_alpha(),pygame.image.load("right4.png").convert_alpha()],
          [pygame.image.load("up1.png").convert_alpha(),pygame.image.load("up2.png").convert_alpha(),
          pygame.image.load("up3.png").convert_alpha(),pygame.image.load("up4.png").convert_alpha()]]
    for i in l4:
        for j in i:
            j.set_colorkey((255,255,255))
    l5 = [[pygame.image.load("down1.png").convert_alpha(), pygame.image.load("down2.png").convert_alpha(),
          pygame.image.load("down3.png").convert_alpha(), pygame.image.load("down4.png").convert_alpha()],
          [pygame.image.load("left1.png").convert_alpha(), pygame.image.load("left2.png").convert_alpha(),
          pygame.image.load("left3.png").convert_alpha(), pygame.image.load("left4.png").convert_alpha()],
          [pygame.image.load("right1.png").convert_alpha(),pygame.image.load("right2.png").convert_alpha(),
          pygame.image.load("right3.png").convert_alpha(),pygame.image.load("right4.png").convert_alpha()],
          [pygame.image.load("up1.png").convert_alpha(),pygame.image.load("up2.png").convert_alpha(),
          pygame.image.load("up3.png").convert_alpha(),pygame.image.load("up4.png").convert_alpha()]]
    for i in l5:
        for j in i:
            j.set_colorkey((255,255,255))
    f1 = [[pygame.image.load("odown1.png").convert_alpha(), pygame.image.load("odown2.png").convert_alpha(),
          pygame.image.load("odown3.png").convert_alpha(), pygame.image.load("odown4.png").convert_alpha()],
          [pygame.image.load("oleft1.png").convert_alpha(), pygame.image.load("oleft2.png").convert_alpha(),
          pygame.image.load("oleft3.png").convert_alpha(), pygame.image.load("oleft4.png").convert_alpha()],
          [pygame.image.load("oright1.png").convert_alpha(),pygame.image.load("oright2.png").convert_alpha(),
          pygame.image.load("oright3.png").convert_alpha(),pygame.image.load("oright4.png").convert_alpha()],
          [pygame.image.load("oup1.png").convert_alpha(),pygame.image.load("oup2.png").convert_alpha(),
          pygame.image.load("oup3.png").convert_alpha(),pygame.image.load("oup4.png").convert_alpha()]]
    for i in f1:
        for j in i:
            j.set_colorkey((255,255,255))
    f2 = [[pygame.image.load("odown1.png").convert_alpha(), pygame.image.load("odown2.png").convert_alpha(),
          pygame.image.load("odown3.png").convert_alpha(), pygame.image.load("odown4.png").convert_alpha()],
          [pygame.image.load("oleft1.png").convert_alpha(), pygame.image.load("oleft2.png").convert_alpha(),
          pygame.image.load("oleft3.png").convert_alpha(), pygame.image.load("oleft4.png").convert_alpha()],
          [pygame.image.load("oright1.png").convert_alpha(),pygame.image.load("oright2.png").convert_alpha(),
          pygame.image.load("oright3.png").convert_alpha(),pygame.image.load("oright4.png").convert_alpha()],
          [pygame.image.load("oup1.png").convert_alpha(),pygame.image.load("oup2.png").convert_alpha(),
          pygame.image.load("oup3.png").convert_alpha(),pygame.image.load("oup4.png").convert_alpha()]]
    for i in f2:
        for j in i:
            j.set_colorkey((255,255,255))
    f3 = [[pygame.image.load("odown1.png").convert_alpha(), pygame.image.load("odown2.png").convert_alpha(),
          pygame.image.load("odown3.png").convert_alpha(), pygame.image.load("odown4.png").convert_alpha()],
          [pygame.image.load("oleft1.png").convert_alpha(), pygame.image.load("oleft2.png").convert_alpha(),
          pygame.image.load("oleft3.png").convert_alpha(), pygame.image.load("oleft4.png").convert_alpha()],
          [pygame.image.load("oright1.png").convert_alpha(),pygame.image.load("oright2.png").convert_alpha(),
          pygame.image.load("oright3.png").convert_alpha(),pygame.image.load("oright4.png").convert_alpha()],
          [pygame.image.load("oup1.png").convert_alpha(),pygame.image.load("oup2.png").convert_alpha(),
          pygame.image.load("oup3.png").convert_alpha(),pygame.image.load("oup4.png").convert_alpha()]]
    for i in f3:
        for j in i:
            j.set_colorkey((255,255,255))
    f4 = [[pygame.image.load("odown1.png").convert_alpha(), pygame.image.load("odown2.png").convert_alpha(),
          pygame.image.load("odown3.png").convert_alpha(), pygame.image.load("odown4.png").convert_alpha()],
          [pygame.image.load("oleft1.png").convert_alpha(), pygame.image.load("oleft2.png").convert_alpha(),
          pygame.image.load("oleft3.png").convert_alpha(), pygame.image.load("oleft4.png").convert_alpha()],
          [pygame.image.load("oright1.png").convert_alpha(),pygame.image.load("oright2.png").convert_alpha(),
          pygame.image.load("oright3.png").convert_alpha(),pygame.image.load("oright4.png").convert_alpha()],
          [pygame.image.load("oup1.png").convert_alpha(),pygame.image.load("oup2.png").convert_alpha(),
          pygame.image.load("oup3.png").convert_alpha(),pygame.image.load("oup4.png").convert_alpha()]]
    for i in f4:
        for j in i:
            j.set_colorkey((255,255,255))
    f5 = [[pygame.image.load("odown1.png").convert_alpha(), pygame.image.load("odown2.png").convert_alpha(),
          pygame.image.load("odown3.png").convert_alpha(), pygame.image.load("odown4.png").convert_alpha()],
          [pygame.image.load("oleft1.png").convert_alpha(), pygame.image.load("oleft2.png").convert_alpha(),
          pygame.image.load("oleft3.png").convert_alpha(), pygame.image.load("oleft4.png").convert_alpha()],
          [pygame.image.load("oright1.png").convert_alpha(),pygame.image.load("oright2.png").convert_alpha(),
          pygame.image.load("oright3.png").convert_alpha(),pygame.image.load("oright4.png").convert_alpha()],
          [pygame.image.load("oup1.png").convert_alpha(),pygame.image.load("oup2.png").convert_alpha(),
          pygame.image.load("oup3.png").convert_alpha(),pygame.image.load("oup4.png").convert_alpha()]]
    for i in f5:
        for j in i:
            j.set_colorkey((255,255,255))
    
    con=mysql.connector.connect(host='localhost',database='project',user='root',password='Agasthya0112')
    cursor = con.cursor(buffered=True)
    cheer=pygame.mixer.Sound("cheer.wav")
    boo=pygame.mixer.Sound("boo.wav")
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
    pause = False
    offopp = "pg"
    defplayer = "pg"
    activeplayer = "pg"
    pass1 = True
    pass2 = True
    pass3 = True
    pass4 = True
    pass5 = True
    movestat1="N"
    movestat2="N"
    movestat3="N"
    movestat4="N"
    movestat5="N"
    pass1dur = random.randint(3,6)
    pass2dur = random.randint(7, 9)
    pass3dur = random.randint(11, 13)
    pass4dur = random.randint(15, 17)
    a1 = random.randint(1, 10)
    block = False
    shoot = False
    coll = False
    collo = False
    movement = True
    move = True
    traover= False
    fin = False
    dz ,dz1 = 0 , 0
    setO = False
    setD = False
    OVER = False
    happened=False
    scp = 0
    sc = 0
    start_ticks = pygame.time.get_ticks()
    fontdef = pygame.font.get_fonts()[23]
    font = pygame.font.SysFont(fontdef, 40)
    textcenter = (675, 450)
    fontdef2 = pygame.font.get_fonts()[3]
    winfont = pygame.font.SysFont(fontdef2, 90)
    wincenter = (560, 160)
    cardfont = pygame.font.SysFont(fontdef2, 30)
    cardcenter = (200, 150)
    scoresh = pygame.font.SysFont(fontdef2, 40)
    fontdef3 = pygame.font.get_fonts()[0]
    winfont2 = pygame.font.SysFont(fontdef3, 30)
    wincenter2 = (560, 270)
    tfont = pygame.font.SysFont(fontdef3, 30)
    tcenter = (1180, 450)
    plyfontdef=pygame.font.get_fonts()[3]
    posfont=pygame.font.SysFont(plyfontdef,20)
    stat1 = "P"
    clock=pygame.time.Clock()
    pgtext="PG"
    sgtext="SG"
    sftext="SF"
    pftext="PF"
    ctext="C"
    fontdefst = pygame.font.get_fonts()[12]
    fontst = pygame.font.SysFont(fontdefst, 50)
    mtext = "MISS!"
    mcenter = (665, 40)
    thptext = "3 POINTER MADE!"
    thpcenter = (540, 40)
    tptext = "2 POINTER MADE!"
    tpcenter = (540, 40)
    plyfont=pygame.font.SysFont(plyfontdef,35)
    plyfontcenter=(10,450)
    sc1 = 0
    bltext = "BLOCKED!"
    shothap = 0
    blcenter = (620, 40)
    itext = "INTERCEPTED"
    icenter = (580, 40)
    ftext="SHOT CLOCK VIOLATION"
    fcenter=(500,40)
    status = 'OFFENSE'
    notransit = True
    px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y = 500, 160, 285, 50, 285, 320, 90, 110, 85, 240
    oldpx,oldpy,oldp2x,oldp2y,oldp3x,oldp3y,oldp4x,oldp4y,oldp5x,oldp5y = px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y
    ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y = 675, 160, 365, 0, 370, 339.5, 145, 70, 145, 260
    oldox,oldoy,oldo2x,oldo2y,oldo3x,oldo3y,oldo4x,oldo4y,oldo5x,oldo5y = ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y
    b1 = ball(ox, oy + 40)
    cx, cy = 85, 217
    pxo, pyo, p2xo, p2yo, p3xo, p3yo, p4xo, p4yo, p5xo, p5yo = 725, 160, 1050, 0, 1050, 339.5, 1250, 70, 1250, 260
    oldpxo,oldpyo,oldp2xo,oldp2yo,oldp3xo,oldp3yo,oldp4xo,oldp4yo,oldp5xo,oldp5yo = pxo, pyo, p2xo, p2yo, p3xo, p3yo, p4xo, p4yo, p5xo, p5yo
    oxo, oyo, o2xo, o2yo, o3xo, o3yo, o4xo, o4yo, o5xo, o5yo = 925, 160, 1100, 30, 1100, 320, 1300, 110, 1300, 240
    oldoxo, oldoyo, oldo2xo, oldo2yo, oldo3xo, oldo3yo, oldo4xo, oldo4yo, oldo5xo, oldo5yo = oxo, oyo, o2xo, o2yo, o3xo, o3yo, o4xo, o4yo, o5xo, o5yo
    B2 = ball(pxo, pyo)
    c2x, c2y = 1375, 225
    blittime = None
    dtime = start_ticks+21000
    otime = start_ticks+21000
    i = True
    coord = []
    b, b2 = 280, 130
    count = 0
    a = 465
    tt1=False
    s1, s2, s3, s4, s5 = 0, 0, 0, 0, 0
    k1, k2, k3, k4, k5 = 0, 0, 0, 0, 0
    while i:
        if a < 285:
            break
        coord.append([a, b])
        coord.append([a, b2])
        if a == 305:
            a -= 5
        elif count >= 5:
            a -= 20
        else:
            a -= 10
        b += 10
        b2 -= 10
        count += 1


    def TPD(x, y):
        TP = False
        if y == 390:
            TP = True
        elif y == 15:
            TP = True
        elif x >= 285:
            TP = True
        for i in coord:
            if y <= 130:
                if y == i[1] or y == i[1] - 5 or y == i[1] + 5:
                    if x >= i[0]:
                        TP = True
            elif y >= 280:
                if y == i[1] or y == i[1] + 5:
                    if x >= i[0]:
                        TP = True
        if TP == True:
            return True

    UP,DOWN,LEFT,RIGHT=False,False,False,False
    a = 945
    b, b2 = 280, 130
    count = 0
    while i:
        if a > 1105:
            break
        coord.append([a, b])
        count = 0
        coord.append([a, b2])
        if a == 1095:
            a += 5
        elif count >= 5:
            a += 20
        else:
            a += 10
        b += 10
        b2 -= 10
        count += 1


    def TPO(x, y):
        TP = False
        if y == 390:
            TP = True
        elif y == 15:
            TP = True
        elif x <= 940:
            TP = True
        for i in coord:
            if y <= 130:
                if y == i[1] or y == i[1] - 5 or y == i[1] + 5:
                    if x <= i[0]:
                        TP = True
            elif y >= 280:
                if y == i[1] or y == i[1] + 5:
                    if x <= i[0]:
                        TP = True
        if TP == True:
            return True


    while RUN:
        s.fill([0, 0, 0])
        s.blit(COURT, (0, 0))
        s.blit(img1, (0, 520))
        s.blit(img2, (312, 520))
        s.blit(img3, (624, 520))
        s.blit(img4, (936, 520))
        s.blit(img5, (1250, 520))
        p1 = player("ply.png", px, py, pxo, pyo)
        p2 = player("ply2.png", p2x, p2y, p2xo, p2yo)
        p3 = player("ply3.png", p3x, p3y, p3xo, p3yo)
        p4 = player("ply4.png", p4x, p4y, p4xo, p4yo)
        p5 = player("ply5.png", p5x, p5y, p5xo, p5yo)
        o1 = opponent("opp.png", ox, oy, oxo, oyo)
        o2 = opponent("opp2.png", o2x, o2y, o2xo, o2yo)
        o3 = opponent("opp3.png", o3x, o3y, o3xo, o3yo)
        o4 = opponent("opp4.png", o4x, o4y, o4xo, o4yo)
        o5 = opponent("opp5.png", o5x, o5y, o5xo, o5yo)
        scoretxt = str(scp) + " - " + str(sc)
        zpr = [[ox, oy], [o2x, o2y], [o3x, o3y], [o4x, o4y], [o5x, o5y]]
        text = font.render(scoretxt, True, [155, 0, 0], [0, 0, 0])
        #nonpcollide()
        s.blit(text, textcenter)
        if traover==True:
            notransit=True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
           
            
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    sc=27
                if notransit == True:
                    if status == 'DEFENSE':
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            LEFT = True
                            RIGHT = False
                            UP = False
                            DOWN = False
                            if status!="DEFENSE":
                                player.movement(curplayer(),-0.5, 0)
                            else:
                                player.movement(curplayer(),-0.3, 0)
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            if status!="DEFENSE":
                                player.movement(curplayer(),+0.5, 0)
                            else:
                                player.movement(curplayer(),+0.3, 0)
                            RIGHT = True
                            LEFT = False
                            UP = False
                            DOWN = False
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            UP = True
                            LEFT = False
                            RIGHT = False
                            DOWN = False
                            if status!="DEFENSE":
                                player.movement(curplayer(),0, -0.5)

                            else:
                                player.movement(curplayer(),0, -0.3)
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            DOWN = True
                            LEFT = False
                            RIGHT = False
                            UP = False
                            if status!="DEFENSE":
                                player.movement(curplayer(),0, 0.5)
                            else:
                                player.movement(curplayer(),0, 0.3)
                        elif event.key==pygame.K_v:
                                opponent.shot2(activeopp(), curvalO(), plycurval())
                        elif event.key == pygame.K_1:
                            defplayer = "pg"
                        elif event.key == pygame.K_2:
                            defplayer = "sg"
                        elif event.key == pygame.K_3:
                            defplayer = "sf"
                        elif event.key == pygame.K_4:
                            defplayer = "pf"
                        elif event.key == pygame.K_5:
                            defplayer = "c"
                    elif status=="OFFENSE":
                        
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            LEFT = True
                            RIGHT = False
                            UP = False
                            DOWN = False
                            player.movement(useplayer(), -0.5, 0)
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            RIGHT = True
                            LEFT = False
                            UP = False
                            DOWN = False
                            player.movement(useplayer(), 0.5, 0)
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            UP = True
                            LEFT = False
                            RIGHT = False
                            DOWN = False
                            player.movement(useplayer(), 0, -0.5)
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            DOWN = True
                            LEFT = False
                            RIGHT = False
                            UP = False
                            player.movement(useplayer(), 0, 0.5)
                        elif event.key == pygame.K_1:
                            if activeplayer != "pg":
                                ball.movement(B2, pxo, pyo)
                                activeplayer = "pg"
                                kpr = "pg"
                        elif event.key == pygame.K_2:
                            if activeplayer != "sg":
                                ball.movement(B2, p2xo, p2yo)
                                activeplayer = "sg"
                                kpr = "sg"
                        elif event.key == pygame.K_3:
                            if activeplayer != "sf":
                                ball.movement(B2, p3xo, p3yo)
                                activeplayer = "sf"
                                kpr = "sf"
                        elif event.key == pygame.K_4:
                            if activeplayer != "pf":
                                ball.movement(B2, p4xo, p4yo)
                                activeplayer = "pf"
                                kpr = "pf"
                        elif event.key == pygame.K_5:
                            if activeplayer != "c":
                                ball.movement(B2, p5xo, p5yo)
                                activeplayer = "c"
                                kpr = "c"
                        if event.key == pygame.K_SPACE:
                            if ball.state2(B2) != "M":
                                if scp < 5:
                                    shoot = True
                                    
                                    if activeplayer == "pg":
                                        player.shot(useplayer(), plycurvalO(), curvalD(), activedefender()[0])
                                        alpha=player.score(useplayer())
                                        s1, scp = s1 + alpha,scp+alpha
                                    elif activeplayer == "sg":
                                        player.shot(useplayer(), plycurvalO(), curvalD(), activedefender()[0])
                                        alpha=player.score(useplayer())
                                        s2, scp = s2 + alpha,scp+alpha
                                    elif activeplayer == "sf":
                                        player.shot(useplayer(), plycurvalO(), curvalD(), activedefender()[0])
                                        alpha=player.score(useplayer())
                                        s3, scp = s3 + alpha,scp+alpha
                                    elif activeplayer == "pf":
                                        player.shot(useplayer(), plycurvalO(), curvalD(), activedefender()[0])
                                        alpha=player.score(useplayer())
                                        s4, scp = s4 + alpha,scp+alpha
                                    elif activeplayer == "c":
                                        player.shot(useplayer(), plycurvalO(), curvalD(), activedefender()[0])
                                        alpha=player.score(useplayer())
                                        s5, scp = s5 + alpha,scp+alpha
                                    if player.activecoord(useplayer())[1] > 202:
                                        ball.movement(B2, 1375, 250)
                                    else:
                                        ball.movement(B2, 1375, 225)
                                    blittime = pygame.time.get_ticks() + 1500

        if stat1 == "M":
            if blittime:
                tst = fontst.render(mtext, True, [0, 0, 0], [155, 0, 0])
                s.blit(tst, mcenter)
                if pygame.time.get_ticks() >= blittime:
                    blittime = None

        elif stat1 == "2P":
            if blittime:
                tst = fontst.render(tptext, True, [0, 0, 0], [155, 0, 0])
                s.blit(tst, tpcenter)
                if pygame.time.get_ticks() >= blittime:
                    blittime = None
        elif stat1 == "3P":
            if blittime:
                tst = fontst.render(thptext, True, [0, 0, 0], [155, 0, 0])
                s.blit(tst, thpcenter)
                if pygame.time.get_ticks() >= blittime:
                    blittime = None


        elif stat1 == "B":
            if blittime:
                tst = fontst.render(bltext, True, [0, 0, 0], [155, 0, 0])
                s.blit(tst, blcenter)
                if pygame.time.get_ticks() >= blittime:
                    blittime = None
        elif stat1 == "I":
            if blittime:
                tst = fontst.render(itext, True, [0, 0, 0], [155, 0, 0])
                s.blit(tst, icenter)
                if pygame.time.get_ticks() >= blittime:
                    blittime = None
        elif stat1=="F":
            if blittime:
                tst = fontst.render(ftext, True, [0, 0, 0], [155, 0, 0])
                s.blit(tst, fcenter)
                if pygame.time.get_ticks() >= blittime:
                    blittime = None
        if notransit == False:
            sec = 5
            tleft = "Time Left is : " + str(sec)
        else:
            if status == "OFFENSE":
                sec = ((otime - pygame.time.get_ticks()) // 1000)
                tleft = "Time Left is : " + str(sec)
            elif status == "DEFENSE" :
                sec = ((dtime - pygame.time.get_ticks()) // 1000)
                tleft = "Time Left is : " + str(sec)
                if pass1:
                    if (20 - sec) == pass1dur:
                        
                        opponent.opppass(activeopp())
                        pass1 = False
                if pass2:
                    if (20 - sec) == pass2dur:
                        opponent.opppass(activeopp())
                        pass2 = False
                if pass3:
                    if (20 - sec) == pass3dur:
                        opponent.opppass(activeopp())
                        pass3 = False
                if pass4:
                    if (20 - sec) == pass4dur:
                        opponent.opppass(activeopp())
                        pass4 = False
        plytextmaker()
        blittext()
        if status=="DEFENSE":
            sc += opponent.score(activeopp())

        over()
        if OVER != True:
            tblit = tfont.render(tleft, True, [155, 0, 0], [0, 0, 0])
            s.blit(tblit, tcenter)
        if OVER == False:
            if status == "DEFENSE":
                ball.draw(b1)
            elif status == "OFFENSE":
                ball.draw(B2)
            if status == "DEFENSE":
                player.update(curplayer())
                opponent.update(activeopp())
            elif status == "OFFENSE":
                player.update(useplayer())
                opponent.update(activedefender()[0])

        pygame.display.update()
        if RUN == False:
            pygame.quit()
