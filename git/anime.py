import pygame
import random
import math
import mysql.connector
from sys import exit
import warnings

warnings.filterwarnings("ignore")
pygame.init()
dz ,dz1 = 0 , 0


def activeopp():
    if offopp == "pg":
        return o1
    elif offopp == "sg":
        return o2
    elif offopp == "sf":
        return o3
    elif offopp == "pf":
        return o4
    elif offopp == "c":
        return o5


def activedefender():
    z = player.activecoord(useplayer())
    b = min(math.dist(z, [oxo, oyo]), math.dist(z, [o2xo, o2yo]), math.dist(z, [o3xo, o3yo]),
            math.dist(z, [o4xo, o4yo]), math.dist(z, [o5xo, o5yo]))
    if b == math.dist(z, [oxo, oyo]):
        return o1
    elif b == math.dist(z, [o2xo, o2yo]):
        return o2
    elif b == math.dist(z, [o3xo, o3yo]):
        return o3
    elif b == math.dist(z, [o4xo, o4yo]):
        return o4
    else:
        return o5


def activepp():
    z = opponent.activecoord(activeopp())
    b = min(math.dist(z, [px, py]), math.dist(z, [p2x, p2y]), math.dist(z, [p3x, p3y]), math.dist(z, [p4x, p4y]),
            math.dist(z, [p5x, p5y]))
    if b == math.dist(z, [px, py]):
        return p1
    elif b == math.dist(z, [p2x, p2y]):
        return p2
    elif b == math.dist(z, [p3x, p3y]):
        return p3
    elif b == math.dist(z, [p4x, p4y]):
        return p4
    else:
        return p5


def curopp():
    if activepp() == p1:
        return "pg"
    elif activepp() == p2:
        return "sg"
    elif activepp() == p3:
        return "sf"
    elif activepp() == p4:
        return "pf"
    elif activepp() == p5:
        return "c"


def plah():
    if activedefender() == o1:
        return "pg"
    elif activedefender() == o2:
        return "sg"
    elif activedefender() == o3:
        return "sf"
    elif activedefender() == o4:
        return "pf"
    elif activedefender() == o5:
        return "c"


def curplayer():
    if defplayer == "pg":
        return p1
    elif defplayer == "sg":
        return p2
    elif defplayer == "sf":
        return p3
    elif defplayer == "pf":
        return p4
    elif defplayer == "c":
        return p5


def useplayer():
    if activeplayer == "pg":
        return p1
    elif activeplayer == "sg":
        return p2
    elif activeplayer == "sf":
        return p3
    elif activeplayer == "pf":
        return p4
    elif activeplayer == "c":
        return p5


def collside(x1, x2, y1, y2):
    global h1, L1, h2
    if x1 > y1:
        if x2 > y2:
            h1 = 1
            L1 = 1
            h2 = -1
        else:
            h1 = -1
            L1 = 1
            h2 = 1
    elif x1 < y1:
        if x2 > y2:
            h1 = 1
            L1 = -1
            h2 = 1
        elif x2 < y2:
            h1 = -1
            L1 = -1
            h2 = 1
        else:
            h2 = -1
    else:
        if x2 > y2:
            h1 = 1
            L1 = 1
        else:
            h1 = -1
            L1 = -1
    return [h1, L1]


def nonpcollide():
    global ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y
    global px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y

    if pygame.sprite.collide_rect(o1, o2):
        oy += collside(ox, oy, o2x, o2y)[0]
        ox += collside(ox, oy, o2x, o2y)[1]
    if pygame.sprite.collide_rect(o1, o3):
        oy += collside(ox, oy, o3x, o3y)[0]
        ox += collside(ox, oy, o3x, o3y)[1]
    if pygame.sprite.collide_rect(o1, o4):
        oy += collside(ox, oy, o4x, o4y)[0]
        ox += collside(ox, oy, o4x, o4y)[1]
    if pygame.sprite.collide_rect(o1, o5):
        oy += collside(ox, oy, o5x, o5y)[0]
        ox += collside(ox, oy, o5x, o5y)[1]
    if pygame.sprite.collide_rect(o3, o2):
        o3y += collside(o3x, o3y, o2x, o2y)[0]
        o3x += collside(o3x, o3y, o2x, o2y)[1]
    if pygame.sprite.collide_rect(o4, o2):
        o4y += collside(o4x, o4y, o2x, o2y)[0]
        o4x += collside(o4x, o4y, o2x, o2y)[1]
    if pygame.sprite.collide_rect(o5, o2):
        o5y += collside(o5x, o5y, o2x, o2y)[0]
        o5x += collside(o5x, o5y, o2x, o2y)[1]
    if pygame.sprite.collide_rect(o3, o4):
        o3y += collside(o3x, o3y, o4x, o4y)[0]
        o3x += collside(o3x, o3y, o4x, o4y)[1]
    if pygame.sprite.collide_rect(o4, o5):
        o4y += collside(o4x, o4y, o5x, o5y)[0]
        o4x += collside(o4x, o4y, o5x, o5y)[1]
    if pygame.sprite.collide_rect(o3, o5):
        o3y += collside(o3x, o3y, o5x, o5y)[0]
        o3x += collside(o3x, o3y, o5x, o5y)[1]
    if pygame.sprite.collide_rect(o1, p1):
        oy += collside(ox, oy, px, py)[0]
        ox += collside(ox, oy, px, py)[1]
    if pygame.sprite.collide_rect(o1, p2):
        oy += collside(ox, oy, p2x, p2y)[0]
        ox += collside(ox, oy, p2x, p2y)[1]
    if pygame.sprite.collide_rect(o1, p3):
        oy += collside(ox, oy, p3x, p3y)[0]
        ox += collside(ox, oy, p3x, p3y)[1]
    if pygame.sprite.collide_rect(o1, p4):
        oy += collside(ox, oy, p4x, p4y)[0]
        ox += collside(ox, oy, p4x, p4y)[1]
    if pygame.sprite.collide_rect(o1, p5):
        oy += collside(ox, oy, p2x, p2y)[0]
        ox += collside(ox, oy, p2x, p2y)[1]
    if pygame.sprite.collide_rect(o2, p1):
        o2y += collside(o2x, o2y, px, py)[0]
        o2x += collside(o2x, o2y, px, py)[1]
    if pygame.sprite.collide_rect(o2, p2):
        o2y += collside(o2x, o2y, p2x, p2y)[0]
        o2x += collside(o2x, o2y, p2x, p2y)[1]
    if pygame.sprite.collide_rect(o2, p3):
        o2y += collside(o2x, o2y, p3x, p3y)[0]
        o2x += collside(o2x, o2y, p3x, p3y)[1]
    if pygame.sprite.collide_rect(o2, p4):
        o2y += collside(o2x, o2y, p4x, p4y)[0]
        o2x += collside(o2x, o2y, p4x, p4y)[1]
    if pygame.sprite.collide_rect(o2, p5):
        o2y += collside(o2x, o2y, p5x, p5y)[0]
        o2x += collside(o2x, o2y, p5x, p5y)[1]
    if pygame.sprite.collide_rect(o3, p1):
        o3y += collside(o3x, o3y, px, py)[0]
        o3x += collside(o3x, o3y, px, py)[1]
    if pygame.sprite.collide_rect(o3, p2):
        o3y += collside(o3x, o3y, p2x, p2y)[0]
        o3x += collside(o3x, o3y, p2x, p2y)[1]
    if pygame.sprite.collide_rect(o3, p3):
        o3y += collside(o3x, o3y, p3x, p3y)[0]
        o3x += collside(o3x, o3y, p3x, p3y)[1]
    if pygame.sprite.collide_rect(o3, p4):
        o3y += collside(o3x, o3y, p4x, p4y)[0]
        o3x += collside(o3x, o3y, p4x, p4y)[1]
    if pygame.sprite.collide_rect(o3, p5):
        o3y += collside(o5x, o5y, p5x, p5y)[0]
        o3x += collside(o5x, o5y, p5x, p5y)[1]
    if pygame.sprite.collide_rect(o4, p1):
        o4y += collside(o4x, o4y, px, py)[0]
        o4x += collside(o4x, o4y, px, py)[1]
    if pygame.sprite.collide_rect(o4, p2):
        o4y += collside(o4x, o4y, p2x, p2y)[0]
        o4x += collside(o4x, o4y, p2x, p2y)[1]
    if pygame.sprite.collide_rect(o4, p3):
        o4y += collside(o4x, o4y, p3x, p3y)[0]
        o4x += collside(o4x, o4y, p3x, p3y)[1]
    if pygame.sprite.collide_rect(o4, p4):
        o4y += collside(o4x, o4y, p4x, p4y)[0]
        o4x += collside(o4x, o4y, p4x, p4y)[1]
    if pygame.sprite.collide_rect(o4, p5):
        o4y += collside(o4x, o4y, p5x, p5y)[0]
        o4x += collside(o4x, o4y, p5x, p5y)[1]
    if pygame.sprite.collide_rect(o5, p1):
        o5y += collside(o5x, o5y, px, py)[0]
        o5x += collside(o5x, o5y, px, py)[1]
    if pygame.sprite.collide_rect(o5, p2):
        o5y += collside(o5x, o5y, p2x, p2y)[0]
        o5x += collside(o5x, o5y, p2x, p2y)[1]
    if pygame.sprite.collide_rect(o5, p3):
        o5y += collside(o5x, o5y, p3x, p3y)[0]
        o5x += collside(o5x, o5y, p3x, p3y)[1]
    if pygame.sprite.collide_rect(o5, p4):
        o5y += collside(o5x, o5y, p4x, p4y)[0]
        o5x += collside(o5x, o5y, p4x, p4y)[1]
    if pygame.sprite.collide_rect(o5, p5):
        o5y += collside(o5x, o5y, p5x, p5y)[0]
        o5x += collside(o5x, o5y, p5x, p5y)[1]
    if pygame.sprite.collide_rect(p1, p2):
        collside(px, py, p2x, p2y)
    if pygame.sprite.collide_rect(p1, p3):
        collside(px, py, p3x, p3y)
    if pygame.sprite.collide_rect(p1, p4):
        collside(px, py, p4x, p4y)
    if pygame.sprite.collide_rect(p1, p5):
        collside(px, py, p5x, p5y)
    if pygame.sprite.collide_rect(p3, p2):
        collside(p2x, p2y, p3x, p3y)
    if pygame.sprite.collide_rect(p4, p2):
        collside(p2x, p2y, p4x, p4y)
    if pygame.sprite.collide_rect(p5, p2):
        collside(p2x, p2y, p5x, p5y)
    if pygame.sprite.collide_rect(p3, p4):
        collside(p3x, p3y, p4x, p4y)
    if pygame.sprite.collide_rect(p4, p5):
        collside(p4x, p4y, p5x, p5y)
    if pygame.sprite.collide_rect(p3, p5):
        collside(p3x, p3y, p5x, p5y)


def coll2():
    global ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y
    if a1 == 1:
        if pygame.sprite.collide_rect(o1, o4):
            o4x -= 3
        if pygame.sprite.collide_rect(o2, o4):
            o4x += 3
            o4y -= 3
        if pygame.sprite.collide_rect(o2, o1):
            o2x -= 3
            o2y += 3
        if pygame.sprite.collide_rect(o2, o3):
            o3y += 5
        if pygame.sprite.collide_rect(o5, o4):
            o5y += 3
    elif a1 == 2:
        if pygame.sprite.collide_rect(o1, o5):
            if sec <= 8:
                o5x += 3
            else:
                oy += 3
        if pygame.sprite.collide_rect(o3, o5):
            o5x -= 3
            o5y += 3
        if pygame.sprite.collide_rect(o3, o1):
            o3x -= 3
            oy -= 3
    elif a1 == 5:
        if pygame.sprite.collide_rect(o2, o4):
            if sec <= 7:
                o4y += 3
            else:
                o4y -= 3
        if pygame.sprite.collide_rect(o1, o5):
            o5y -= 3
    elif a1 == 6:
        if pygame.sprite.collide_rect(o3, o5):
            o5y -= 3
    elif a1 == 8:
        if pygame.sprite.collide_rect(o1, o4):
            o4x -= 3
    elif a1 == 9:
        if pygame.sprite.collide_rect(o2, o5):
            o5x -= 3
    elif a1 == 10:
        if pygame.sprite.collide_rect(o2, o3):
            o3x += 5
        if pygame.sprite.collide_rect(o3, o4):
            o4x -= 5


def boundforall():
    global px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y
    if px >= 675:
        px = 675
    if px <= 30:
        px = 30
    if py <= 15:
        py = 15
    if py >= 390:
        py = 390
    if p2x >= 675:
        p2x = 675
    if p2x <= 30:
        p2x = 30
    if p2y <= 15:
        p2y = 15
    if p2y >= 390:
        p2y = 390
    if p3x >= 675:
        p3x = 675
    if p3x <= 30:
        p3x = 30
    if p3y <= 15:
        p3y = 15
    if p3y >= 390:
        p3y = 390
    if p4x >= 675:
        p4x = 675
    if p4x <= 30:
        p4x = 30
    if p4y <= 15:
        p4y = 15
    if p4y >= 390:
        p4y = 390
    if p5x >= 675:
        p5x = 675
    if p5x <= 30:
        p5x = 30
    if p5y <= 15:
        p5y = 15
    if p5y >= 390:
        p5y = 390


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
            c2x, c2y = 85, 390
            d2x, d2y = 85, 280
            e2x, e2y = 185, 155
        elif a1 == 2:
            ax, ay = 400, 330
            bx, by = 400, 80
            cx, cy = 85, 390
            dx, dy = 105, 120
            ex, ey = 330, 200
            a2x, a2y = 305, 160
            b2x, b2y = 90, 15
            c2x, c2y = 400, 80
            d2x, d2y = 150, 250
            e2x, e2y = 90, 120
        elif a1 == 3:
            ax, ay = 85, 390
            bx, by = 85, 20
            cx, cy = 450, 120
            dx, dy = 270, 280
            ex, ey = 270, 130
            a2x, a2y = 85, 330
            b2x, b2y = 85, 80
            c2x, c2y = 330, 200
            d2x, d2y = 270, 300
            e2x, e2y = 270, 110
        elif a1 == 4:
            ax, ay = 85, 20
            bx, by = 465, 200
            cx, cy = 85, 390
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
            cx, cy = 70, 390
            dx, dy = 390, 80
            ex, ey = 310, 150
            a2x, a2y = 325, 220
            b2x, b2y = 450, 120
            c2x, c2y = 270, 30
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
            ax, ay = 160, 390
            bx, by = 250, 120
            cx, cy = 250, 290
            dx, dy = 110, 15
            ex, ey = 110, 390
            a2x, a2y = 265, 390
            b2x, b2y = 110, 290
            c2x, c2y = 110, 110
            d2x, d2y = 310, 110
            e2x, e2y = 310, 290
        elif a1 == 8:
            ax, ay = 160, 20
            bx, by = 250, 120
            cx, cy = 250, 290
            dx, dy = 110, 15
            ex, ey = 110, 390
            a2x, a2y = 265, 15
            b2x, b2y = 110, 110
            c2x, c2y = 110, 290
            d2x, d2y = 290, 290
            e2x, e2y = 290, 110
        elif a1 == 9:
            ax, ay = 305, 280
            bx, by = 85, 390
            cx, cy = 310, 15
            dx, dy = 390, 200
            ex, ey = 130, 150
            a2x, a2y = 125, 320
            b2x, b2y = 270, 390
            c2x, c2y = 465, 195
            d2x, d2y = 290, 110
            e2x, e2y = 90, 90
        elif a1 == 10:
            ax, ay = 305, 120
            bx, by = 350, 390
            cx, cy = 90, 15
            dx, dy = 150, 250
            ex, ey = 390, 210
            a2x, a2y = 145, 80
            b2x, b2y = 470, 210
            c2x, c2y = 305, 15
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
            if math.dist([a2x, a2y], [ox, oy]) <= 3:
                ox = a2x
                oy = a2y
                if math.dist([b2x, b2y], [o2x, o2y]) <= 3:
                    o2x = b2x
                    o2y = b2y
                    if math.dist([c2x, c2y], [o3x, o3y]) <= 3:
                        o3x = c2x
                        o3y = c2y
                        if math.dist([d2x, d2y], [o4x, o4y]) <= 3:
                            o4x = d2x
                            o4y = d2y
                            if math.dist([e2x, e2y], [o5x, o5y]) <= 3:
                                o5x = e2x
                                o5y = e2y
                            else:
                                o5x += ((e2x - o5x) / step10) * 1.2
                                o5y += ((e2y - o5y) / step10) * 1.2
                        else:
                            o4x += ((d2x - o4x) / step9) * 1.2
                            o4y += ((d2y - o4y) / step9) * 1.2
                    else:
                        o3x += ((c2x - o3x) / step8) * 1.2
                        o3y += ((c2y - o3y) / step8) * 1.2
                else:
                    o2x += ((b2x - o2x) / step7) * 1.2
                    o2y += ((b2y - o2y) / step7) * 1.2
            else:
                ox += ((a2x - ox) / step6) * 1.2
                oy += ((a2y - oy) / step6) * 1.2
        else:
            if math.dist([ax, ay], [ox, oy]) <= 3:
                ox = ax
                oy = ay
                if math.dist([bx, by], [o2x, o2y]) <= 3:
                    o2x = bx
                    o2y = by
                    if math.dist([cx, cy], [o3x, o3y]) <= 3:
                        o3x = cx
                        o3y = cy
                        if math.dist([dx, dy], [o4x, o4y]) <= 3:
                            o4x = dx
                            o4y = dy
                            if math.dist([ex, ey], [o5x, o5y]) <= 3:
                                o5x = ex
                                o5y = ey
                                fin = True
                            else:
                                o5x += ((ex - o5x) / step5) * 1.2
                                o5y += ((ey - o5y) / step5) * 1.2
                        else:
                            o4x += ((dx - o4x) / step4) * 1.2
                            o4y += ((dy - o4y) / step4) * 1.2
                    else:
                        o3x += ((cx - o3x) / step3) * 1.2
                        o3y += ((cy - o3y) / step3) * 1.2
                else:
                    o2x += ((bx - o2x) / step2) * 1.2
                    o2y += ((by - o2y) / step2) * 1.2
            else:
                ox += ((ax - ox) / step) * 1.2
                oy += ((ay - oy) / step) * 1.2

    def move_towards_player(self):
        global oxo, oyo, o2xo, o2yo, o3xo, o3yo, o4xo, o4yo, o5xo, o5yo
        dx = 0
        dy = 0
        if math.dist(player.activecoord(useplayer()), opponent.activecoord(activedefender())) < 400:
            step = max(abs(player.activecoord(useplayer())[0] - opponent.activecoord(activedefender())[0]),
                       abs(player.activecoord(useplayer())[1] - opponent.activecoord(activedefender())[1]))
            dx += float(player.activecoord(useplayer())[0] - opponent.activecoord(activedefender())[0]) / step
            dy += float(player.activecoord(useplayer())[1] - opponent.activecoord(activedefender())[1]) / step
        if math.dist(player.activecoord(useplayer()), opponent.activecoord(activedefender())) <= 25:
            dx = 0
            dy = 0
        if plah() == "pg":
            oxo += (dx / 2)
            oyo += (dy / 2)
        if plah() == "sg":
            o2xo += (dx / 3)
            o2yo += (dy / 3)
        if plah() == "sf":
            o3xo += (dx / 3)
            o3yo += (dy / 3)
        if plah() == "pf":
            o4xo += (dx / 3)
            o4yo += (dy / 3)
        if plah() == "c":
            o5xo += (dx / 3)
            o5yo += (dy / 3)

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
                    offopp = prob1
                    moveball = moveloc
                else:
                    offopp = prob2
                    moveball = moveloc2

                if offopp == "pg":
                    ball.movement(b1, ox, oy)
                elif offopp == "sg":
                    ball.movement(b1, o2x, o2y)
                elif offopp == "sf":
                    ball.movement(b1, o3x, o3y)
                elif offopp == "pf":
                    ball.movement(b1, o4x, o4y)
                elif offopp == "c":
                    ball.movement(b1, o5x, o5y)
                movement = False
                print(offopp, prob1, prob2, moveball[0], moveball[1])

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

        if math.dist(opponent.activecoord(activeopp()), player.activecoord(activepp())) >= 150:
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

            elif self.K == False:
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
            if sec == 18:
                self.Z = 25

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

    def win(self):
        if sc >= 21:
            wintext = "YOU LOSE"
            winblit = winfont.render(wintext, True, [0, 0, 0], [155, 0, 0])
            s.blit(winblit, wincenter)
            wintext2 = "Exit window to close game"
            winblit2 = winfont2.render(wintext2, True, [0, 0, 0], [155, 0, 0])
            s.blit(winblit2, wincenter2)

    def update(self):
        global ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y ,dz1
        global oxo, oyo, o2xo, o2yo, o3xo, o3yo, o4xo, o4yo, o5xo, o5yo
        global oldox,oldoy,oldo2x,oldo2y,oldo3x,oldo3y,oldo4x,oldo4y,oldo5x,oldo5y
        global oldoxo, oldoyo, oldo2xo, oldo2yo, oldo3xo, oldo3yo, oldo4xo, oldo4yo, oldo5xo, oldo5yo
        if status == 'DEFENSE':
            if notransit:
                if shoot == False:
                    if coll == False:
                        opponent.oppmove(self)
                opponent.boundaryD(self)
        elif status == 'OFFENSE':
            self = activedefender()
            if notransit:
                if shoot == False:
                    if coll == False:
                        opponent.move_towards_player(self)
                opponent.boundaryO(self)


        if status == "DEFENSE":
            if oldox > px  + 0 and oldoy == oy:
                s.blit(f1[1][dz], (ox, oy))
            elif oldox + 0 < px and oldoy == oy:
                s.blit(f1[2][dz], (ox, oy))
            elif oldox == ox and oldoy < oy + 0:
                s.blit(f1[0][dz], (ox, oy))
            elif oldox == ox and oldoy > oy + 0:
                s.blit(f1[3][dz], (ox, oy))
            elif oldox > ox + 0 and oldoy + 0 < oy:
                s.blit(f1[1][dz], (ox, oy))
            elif oldox + 0 < ox and oldoy > oy + 0:
                s.blit(f1[2][dz], (ox, oy))
            elif oldox + 0 < ox and oldoy + 0 < oy:
                s.blit(f1[2][dz], (ox, oy))
            elif oldox > ox + 0 and oldoy > oy + 0:
                s.blit(f1[1][dz], (ox, oy))
             else:
                s.blit(f1[0][0], (ox, oy))

            if oldo2x > o2x + 0 and oldo2y == o2y:
                s.blit(f2[1][dz], (o2x, o2y))
            elif oldo2x + 0 < o2x and oldo2y == o2y:
                s.blit(f2[2][dz], (o2x, o2y))
            elif oldo2x == o2x and oldo2y + 0 < o2y :
                s.blit(f2[0][dz], (o2x, o2y))
            elif oldo2x == o2x and oldo2y > o2y + 0:
                s.blit(f2[3][dz], (o2x, o2y))
            elif oldo2x > o2x + 0 and oldo2y + 0 < o2y:
                s.blit(f2[1][dz], (o2x, o2y))
            elif oldo2x + 0 < o2x and oldo2y > o2y + 0:
                s.blit(f2[2][dz], (o2x, o2y))
            elif oldo2x + 0 < o2x and oldo2y + 0 < o2y:
                s.blit(f2[2][dz], (o2x, o2y))
            elif oldo2x > o2x + 0 and oldo2y > o2y + 0:
                s.blit(f2[1][dz], (o2x, o2y))
            else:
                s.blit(f2[0][0], (o2x, o2y))

            if oldo3x > o3x + 0 and oldo3y == o3y:
                s.blit(f3[1][dz], (o3x, o3y))
            elif oldo3x + 0 < o3x and oldo3y == o3y:
                s.blit(f3[2][dz], (o3x, o3y))
            elif oldo3x == o3x and oldo3y + 0 < o3y:
                s.blit(f3[0][dz], (o3x, o3y))
            elif oldo3x == o3x and oldo3y > o3y + 0:
                s.blit(f3[3][dz], (o3x, o3y))
            elif oldo3x > o3x + 0 and oldo3y + 0 < o3y:
                s.blit(f3[1][dz], (o3x, o3y))
            elif oldo3x + 0 < o3x and oldo3y > o3y + 0:
                s.blit(f3[2][dz], (o3x, o3y))
            elif oldo3x + 0 < o3x and oldo3y + 0 < o3y:
                s.blit(f3[2][dz], (o3x, o3y))
            elif oldo3x > o3x + 0 and oldo3y > o3y + 0:
                s.blit(f3[1][dz], (o3x, o3y))
            else:
                s.blit(f3[0][0], (o3x, o3y))

            if oldo4x > o4x + 0 and oldo4y == o4y:
                s.blit(f4[1][dz], (o4x, o4y))
            elif oldo4x + 0 < o4x and oldo4y == o4y:
                s.blit(f4[2][dz], (o4x, o4y))
            elif oldo4x == o4x and oldo4y + 0 < o4y:
                s.blit(f4[0][dz], (o4x, o4y))
            elif oldo4x == o4x and oldo4y > o4y + 0:
                s.blit(f4[3][dz], (o4x, o4y))
            elif oldo4x > o4x + 0 and oldo4y + 0 < o4y:
                s.blit(f4[1][dz], (o4x, o4y))
            elif oldo4x + 0 < o4x and oldo4y > o4y + 0:
                s.blit(f4[2][dz], (o4x, o4y))
            elif oldo4x + 0 < o4x and oldo4y + 0 < o4y:
                s.blit(f4[2][dz], (o4x, o4y))
            elif oldo4x > o4x + 0 and oldo4y > o4y + 0:
                s.blit(f4[1][dz], (o4x, o4y))
            else:
                s.blit(f4[0][0], (o4x, o4y))


            if oldo5x > o5x + 0 and oldo5y == o5x:
                s.blit(f5[1][dz], (o5x, o5x))
            elif oldo5x + 0 < o5x and oldo5y == o5x:
                s.blit(f5[2][dz], (o5x, o5x))
            elif oldo5x == o5x and oldo5y + 0 < o5x:
                s.blit(f5[0][dz], (o5x, o5x))
            elif oldo5x == o5x and oldo5y > o5x + 0:
                s.blit(f5[3][dz], (o5x, o5x))
            elif oldo5x > o5x + 0 and oldo5y + 0 < o5x:
                s.blit(f5[1][dz], (o5x, o5x))
            elif oldo5x + 0 < o5x and oldo5y > o5x + 0:
                s.blit(f5[2][dz], (o5x, o5x))
            elif oldo5x + 0 < o5x and oldo5y + 0 < o5x:
                s.blit(f5[2][dz], (o5x, o5x))
            elif oldo5x > o5x + 0 and oldo5y > o5x + 0:
                s.blit(f5[1][dz], (o5x, o5x))
            else:
                s.blit(f5[0][0], (o5x, o5x))
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
        if py <= 15:
            py = 15
        if py >= 390:
            py = 390
        if p2x >= 675:
            p2x = 675
        if p2x <= 30:
            p2x = 30
        if p2y <= 15:
            p2y = 15
        if p2y >= 390:
            p2y = 390
        if p3x >= 675:
            p3x = 675
        if p3x <= 30:
            p3x = 30
        if p3y <= 15:
            p3y = 15
        if p3y >= 390:
            p3y = 390
        if p4x >= 675:
            p4x = 675
        if p4x <= 30:
            p4x = 30
        if p4y <= 15:
            p4y = 15
        if p4y >= 390:
            p4y = 390
        if p5x >= 675:
            p5x = 675
        if p5x <= 30:
            p5x = 30
        if p5y <= 15:
            p5y = 15
        if p5y >= 390:
            p5y = 390

    def boundaryO(self):
        global pxo, pyo, p2xo, p2yo, p3xo, p3yo, p4xo, p4yo, p5xo, p5yo
        if pxo >= 1365:
            pxo = 1365
        if pxo <= 725:
            pxo = 725
        if pyo <= 15:
            pyo = 15
        if pyo >= 390:
            pyo = 390
        if p2xo >= 1365:
            p2xo = 1365
        if p2xo <= 725:
            p2xo = 725
        if p2yo <= 15:
            p2yo = 15
        if p2yo >= 390:
            p2yo = 390
        if p3xo >= 1365:
            p3xo = 1365
        if p3xo <= 725:
            p3xo = 725
        if p3yo <= 15:
            p3yo = 15
        if p3yo >= 390:
            p3yo = 390
        if p4xo >= 1365:
            p4xo = 1365
        if p4xo <= 725:
            p4xo = 725
        if p4yo <= 15:
            p4yo = 15
        if p4yo >= 390:
            p4yo = 390
        if p5xo >= 1365:
            p5xo = 1365
        if p5xo <= 725:
            p5xo = 725
        if p5yo <= 15:
            p5yo = 15
        if p5yo >= 390:
            p5yo = 390

    def collide(self, y, x2, y2):
        if pygame.sprite.collide_rect(self, y):
            if self.rect.x < x2:
                self.movex = -20
            elif self.rect.x > x2:
                self.movex = 20
            if self.rect.y < y2:
                self.movey = -20
            elif self.rect.y > y2:
                self.movey = 20

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

    def sta(self):
        return self.rect.x, self.rect.y

    def movement(self, x, y):
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

        print(self.shotchance, shotprob, defprob, dis)

    def score(self):
        global status, stat1
        if status == "OFFENSE":
            if sec <= 3:
                self.shotchance = random.randint(5, 30)
            if self.block == True:
                self.score = 0
                stat1 = "B"
            elif self.shotchance >= 23:
                if self.K:
                    stat1 = "3P"
                    self.score = 25
                else:
                    self.score = 2

                    stat1 = "2P"
            elif self.shotchance < 23:
                stat1 = "M"
                self.score = 0
            notransit = False

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
                px += self.movex
                py += self.movey
            elif defplayer == "sg":
                player2 = True
                p2x += self.movex
                p2y += self.movey
            elif defplayer == "sf":
                player3 = True
                p3x += self.movex
                p3y += self.movey
            elif defplayer == "pf":
                player4 = True
                p4x += self.movex
                p4y += self.movey
            elif defplayer == "c":
                player5 = True
                p5x += self.movex
                p5y += self.movey
            if notransit:
                player.boundaryD(self)
        elif status == "OFFENSE":

            if activeplayer == "pg":
                player1 = True
                pxo += self.movex
                pyo += self.movey
            elif activeplayer == "sg":
                player2 = True
                p2xo += self.movex
                p2yo += self.movey
            elif activeplayer == "sf":
                player3 = True
                p3xo += self.movex
                p3yo += self.movey
            elif activeplayer == "pf":
                player4 = True
                p4xo += self.movex
                p4yo += self.movey
            elif activeplayer == "c":
                player5 = True
                p5xo += self.movex
                p5yo += self.movey
            if notransit:
                player.boundaryO(self)


        if status == "DEFENSE":
            if notransit:
                pass
            else:
                self.rect.x = player.activecoord(useplayer())[0]
                self.rect.y = player.activecoord(useplayer())[1]
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
            if notransit:
                pass
            else:
                self.rect.x = player.activecoord(curplayer())[0]
                self.rect.y = player.activecoord(curplayer())[1]
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
        oldpx, oldpy, oldp2x, oldp2y, oldp3x, oldp3y, oldp4x, oldp4y, oldp5x, oldp5y = px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y
        oldpxo, oldpyo, oldp2xo, oldp2yo, oldp3xo, oldp3yo, oldp4xo, oldp4yo, oldp5xo, oldp5yo = pxo, pyo, p2xo, p2yo, p3xo, p3yo, p4xo, p4yo, p5xo, p5yo
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

    def state(self, x):
        self.state = x

    def state2(self):
        return self.state

    def collision(self, x2, y2):
        if math.dist((self.x, self.y), (x2, y2)) < 20:
            self.ballmovex = 0
            self.ballmovey = 0
            return True

    def collisionb(self, x2, y2):
        if math.dist([self.x], [x2]) <= 10:
            if math.dist([self.y], [y2]) <= 5:
                self.ballmovex = 0
                self.ballmovey = 0
                return True

    def collisionO(self, x2, y2):
        if math.dist((self.x, self.y), (x2, y2)) <= 10:
            self.ballmovex, self.ballmovey = 0, 0
            return True

    def movement(self, x2, y2):
        global disfn

        self.number = max(abs(x2 - self.x), abs(y2 - self.y))
        self.ballmovex = float(x2 - self.x) / self.number
        self.ballmovey = float(y2 - self.y) / self.number
        self.state = "M"
        if shoot == False:

            if math.dist((self.x, self.y), (x2, y2)) <= 100:
                disfn = "T1"
            elif math.dist((self.x, self.y), (x2, y2)) <= 300 and math.dist((self.x, self.y), (x2, y2)) > 100:
                disfn = "T2"
            else:
                disfn = "T3"
        else:
            disfn = "T0"

    def cor(self):
        return [self.x, self.y]

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
            if ball.collisionb(self, cx, cy):
                setD = True
            if setD == True:
                self.state = "D1"
                transition()

            ball.boundaryD(self)
            if self.state == "M":

                if disfn == "T1":
                    fx = 1.5
                elif disfn == "T2":
                    fx = 2
                elif disfn == "T0":
                    fx = 3
                else:
                    fx = 1.5
                self.x += self.ballmovex * 1.5
                self.y += self.ballmovey * 1.5

            elif self.state == "P":
                if offopp == "pg":
                    self.x = ox
                    self.y = oy + 20
                elif offopp == "sg":
                    self.x = o2x
                    self.y = o2y + 20
                elif offopp == "sf":
                    self.x = o3x
                    self.y = o3y + 20
                elif offopp == "pf":
                    self.x = o4x
                    self.y = o4y + 20
                elif offopp == "c":
                    self.x = o5x
                    self.y = o5y + 20
            else:
                if self.state == "D1":
                    self.x = px + 50
                    self.y = py + 20
                    defplayer = "pg"
                elif self.state == "D2":
                    self.x = p2x + 50
                    self.y = p2y + 20
                    defplayer = "sg"
                elif self.state == "D3":
                    self.x = p3x + 50
                    self.y = p3y + 20
                    defplayer = "sf"
                elif self.state == "D4":
                    self.x = p4x + 50
                    self.y = p4y + 20
                    defplayer = "pf"
                elif self.state == "D5":
                    self.x = p5x + 50
                    self.y = p5y + 20
                    defplayer = "c"
                transition()

        elif status == "OFFENSE":
            if shoot == False:
                if notransit == True:
                    if self.state == "M":
                        if ball.collision(self, oxo, oyo):
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
                    if ball.collision(self, pxo, pyo) or ball.collision(self, p2xo, p2yo) or ball.collision(self, p3xo,
                                                                                                            p3yo) or ball.collision(
                            self, p4xo, p4yo) or ball.collision(self, p5xo, p5yo):
                        self.state = "P"
                if collo == True:
                    blittime = pygame.time.get_ticks() + 1500
                    stat1 = "I"

            if ball.collisionO(self, c2x, c2y):
                setO = True
            if setO == True:
                transition()
                self.x = oxo
                self.y = oyo + 20
            ball.boundaryO(self)
            if self.state == "M":
                if disfn == "T1":
                    fx = 1.5
                elif disfn == "T2":
                    fx = 2
                elif disfn == "T0":
                    fx = 3
                else:
                    fx = 2
                self.x += self.ballmovex * fx
                self.y += self.ballmovey * fx
            elif self.state == "P":
                if activeplayer == "pg":
                    self.x = pxo + 50
                    self.y = pyo + 20
                elif activeplayer == "sg":
                    self.x = p2xo + 50
                    self.y = p2yo + 20
                elif activeplayer == "sf":
                    self.x = p3xo + 50
                    self.y = p3yo + 20
                elif activeplayer == "pf":
                    self.x = p4xo + 50
                    self.y = p4yo + 20
                elif activeplayer == "c":
                    self.x = p5xo + 50
                    self.y = p5yo + 20
            else:
                if self.state == "D1":
                    self.x = oxo
                    self.y = oyo
                elif self.state == "D2":
                    self.x = o2xo
                    self.y = o2yo
                elif self.state == "D3":
                    self.x = o3xo
                    self.y = o3yo
                elif self.state == "D4":
                    self.x = o4xo
                    self.y = o4yo
                elif self.state == "D5":
                    self.x = o5xo
                    self.y = o5yo
                transition()
        pygame.draw.circle(s, (255, 140, 0), [self.x, self.y], self.rad)


def curvalD():
    if activedefender() == o1:
        return valo1[3:5]
    elif activedefender() == o2:
        return valo2[3:5]
    elif activedefender() == o3:
        return valo3[3:5]
    elif activedefender() == o4:
        return valo4[3:5]
    elif activedefender() == o5:
        return valo5[3:5]


def curvalO():
    if offopp == 'pg':
        return valo1[1:3]
    elif offopp == 'sg':
        return valo2[1:3]
    elif offopp == 'sf':
        return valo3[1:3]
    elif offopp == 'pf':
        return valo4[1:3]
    elif offopp == 'c':
        return valo5[1:3]


def plycurval():
    if curopp() == 'pg':
        return valp1[3:5]
    elif curopp() == 'sg':
        return valp2[3:5]
    elif curopp() == 'sf':
        return valp3[3:5]
    elif curopp() == 'pf':
        return valp4[3:5]
    elif curopp() == 'c':
        return valp5[3:5]


def transition():
    global px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y
    global ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y
    global oxo, oyo, o2xo, o2yo, o3xo, o3yo, o4xo, o4yo, o5xo, o5yo
    global pxo, pyo, p2xo, p2yo, p3xo, p3yo, p4xo, p4yo, p5xo, p5yo
    global status, coll, setO, setD, sec, a1, collo, stat1
    global notransit, shoot, dtime, otime, activeplayer, movement

    notransit = False
    if status == "DEFENSE":
        coll = False
        shoot = False
        ax, ay = 725, 200
        bx, by = 1050, 40
        cx, cy = 1050, 360
        dx, dy = 1250, 120
        ex, ey = 1250, 290
        fx, fy = 925, 200
        gx, gy = 1100, 90
        hx, hy = 1100, 320
        ix, iy = 1300, 160
        jx, jy = 1300, 255
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
        try:
            px += (ax - px) / step1
            py += (ay - py) / step1
        except:
            pass
        try:
            p2x += (bx - p2x) / step2
            p2y += (by - p2y) / step2
        except:
            pass
        try:
            p3x += (cx - p3x) / step3
            p3y += (cy - p3y) / step3
        except:
            pass
        try:
            p4x += (dx - p4x) / step4
            p4y += (dy - p4y) / step4
        except:
            pass
        try:
            p5x += (ex - p5x) / step5
            p5y += (ey - p5y) / step5
        except:
            pass
        if math.dist([ox, oy], [fx, fy]) <= 1:
            ox, oy = fx, fy
        else:
            ox += (fx - ox) / step6
            oy += (fy - oy) / step6
        if math.dist([o2x, o2y], [gx, gy]) <= 1:
            o2x, o2y = gx, gy
        else:
            o2x += (gx - o2x) / step7
            o2y += (gy - o2y) / step7
        if math.dist([o3x, o3y], [hx, hy]) <= 1:
            o3x, o3y = hx, hy
        else:
            o3x += (hx - o3x) / step8
            o3y += (hy - o3y) / step8

        if math.dist([o4x, o4y], [ix, iy]) <= 1:
            o4x, o4y = ix, iy
        else:
            o4x += (ix - o4x) / step9
            o4y += (iy - o4y) / step9
        if math.dist([o5x, o5y], [jx, jy]) <= 1:
            o5x, o5y = jx, jy
        else:
            o5x += (jx - o5x) / step10
            o5y += (jy - o5y) / step10
        if step1 == 0 and step2 == 0 and step3 == 0 and step4 == 0 and step5 == 0 and step6 == 0 and step7 == 0 and step8 == 0 and step9 == 0 and step10 == 0:
            coll = False
            setD = False
            notransit = True
            ball.state(B2, "P")
            dtime = 0
            movement = True
            activeplayer = "pg"
            otime = pygame.time.get_ticks() + 21000
            status = "OFFENSE"
            px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y = 500, 200, 285, 90, 285, 320, 85, 160, 85, 255
            ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y = 675, 200, 365, 35, 370, 370, 145, 120, 145, 290

    if status == "OFFENSE":
        sec = 5
        collo = False
        shoot = False
        ax, ay = 500, 200
        bx, by = 285, 90
        cx, cy = 285, 320
        dx, dy = 85, 160
        ex, ey = 85, 255
        fx, fy = 675, 200
        gx, gy = 365, 35
        hx, hy = 370, 370
        ix, iy = 145, 120
        jx, jy = 145, 290
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
        try:
            pxo += (ax - pxo) / step1
            pyo += (ay - pyo) / step1
        except:
            pass
        try:
            p2xo += (bx - p2xo) / step2
            p2yo += (by - p2yo) / step2
        except:
            pass
        try:
            p3xo += (cx - p3xo) / step3
            p3yo += (cy - p3yo) / step3
        except:
            pass
        try:
            p4xo += (dx - p4xo) / step4
            p4yo += (dy - p4yo) / step4
        except:
            pass
        try:
            p5xo += (ex - p5xo) / step5
            p5yo += (ey - p5yo) / step5
        except:
            pass
        if math.dist([oxo, oyo], [fx, fy]) <= 1:
            oxo, oyo = fx, fy
            step6 = 0
        else:
            oxo += (fx - oxo) / step6
            oyo += (fy - oyo) / step6
        if math.dist([o2xo, o2yo], [gx, gy]) <= 1:
            o2xo, o2yo = gx, gy

        else:
            o2xo += (gx - o2xo) / step7
            o2yo += (gy - o2yo) / step7
        if math.dist([o3xo, o3yo], [hx, hy]) <= 1:
            o3xo, o3yo = hx, hy
        else:
            o3xo += (hx - o3xo) / step8
            o3yo += (hy - o3yo) / step8

        if math.dist([o4xo, o4yo], [ix, iy]) <= 1:
            o4xo, o4yo = ix, iy
        else:
            o4xo += (ix - o4xo) / step9
            o4yo += (iy - o4yo) / step9
        if math.dist([o5xo, o5yo], [jx, jy]) <= 1:
            o5xo, o5yo = jx, jy
        else:
            o5xo += (jx - o5xo) / step10
            o5yo += (jy - o5yo) / step10
        if step1 == 0 and step2 == 0 and step3 == 0 and step4 == 0 and step5 == 0 and step6 == 0 and step7 == 0 and step8 == 0 and step9 == 0 and step10 == 0:
            notransit = True
            a1 = random.randint(1, 10)
            dtime = pygame.time.get_ticks() + 21000
            otime = 0
            o4x, o5x = o4xo, o5xo
            o4y, o5y = o4yo, o5yo
            o3x, o3y, o2x, o2y, ox, oy = o3xo, o3yo, o2xo, o2yo, oxo, oyo
            defplayer = "pg"
            ball.state(b1, "P")
            activeopp = "pg"
            setO = False
            stat1 = "P"
            status = "DEFENSE"
            pxo, pyo, p2xo, p2yo, p3xo, p3yo, p4xo, p4yo, p5xo, p5yo = 725, 200, 1050, 40, 1050, 360, 1250, 120, 1250, 290
            oxo, oyo, o2xo, o2yo, o3xo, o3yo, o4xo, o4yo, o5xo, o5yo = 925, 200, 1100, 90, 1100, 320, 1300, 160, 1300, 255


def over():
    global OVER
    if sc > 21:
        OVER = True
        wintext = "YOU LOSE"
        wintext2 = "Exit window to close game"
        Playsc = "PLAYER SCORECARD"
        Oppsc = "OPPONENT SCORECARD"
        sL1 = valp1[0] + " -  " + str(s1)
        sL2 = valp2[0] + " -  " + str(s2)
        sL3 = valp3[0] + " -  " + str(s3)
        sL4 = valp4[0] + " -  " + str(s4)
        sL5 = valp5[0] + " - " + str(s5)
        sM5 = valo5[0] + " -  " + str(k5)
        sM4 = valo4[0] + " -  " + str(k4)
        sM3 = valo3[0] + " -  " + str(k3)
        sM2 = valo2[0] + " -  " + str(k2)
        sM1 = valo1[0] + " - " + str(k1)
        winblit = winfont.render(wintext, True, [0, 0, 0], [155, 0, 0])
        winblit2 = winfont2.render(wintext2, True, [0, 0, 0], [155, 0, 0])
        splblit = scoresh.render(Playsc, True, [0, 0, 0], [155, 0, 0])
        sopblit = scoresh.render(Oppsc, True, [0, 0, 0], [155, 0, 0])
        sblit1 = cardfont.render(sL1, True, [0, 0, 0], [155, 0, 0])
        sblit2 = cardfont.render(sL2, True, [0, 0, 0], [155, 0, 0])
        sblit3 = cardfont.render(sL3, True, [0, 0, 0], [155, 0, 0])
        sblit4 = cardfont.render(sL4, True, [0, 0, 0], [155, 0, 0])
        sblit5 = cardfont.render(sL5, True, [0, 0, 0], [155, 0, 0])
        opblit1 = cardfont.render(sM1, True, [0, 0, 0], [155, 0, 0])
        opblit2 = cardfont.render(sM2, True, [0, 0, 0], [155, 0, 0])
        opblit3 = cardfont.render(sM3, True, [0, 0, 0], [155, 0, 0])
        opblit4 = cardfont.render(sM4, True, [0, 0, 0], [155, 0, 0])
        opblit5 = cardfont.render(sM5, True, [0, 0, 0], [155, 0, 0])
        s.blit(splblit, (cardcenter[0] - 80, cardcenter[1] - 60))
        s.blit(sblit1, cardcenter)
        s.blit(sblit2, (cardcenter[0], cardcenter[1] + 40))
        s.blit(sblit3, (cardcenter[0], cardcenter[1] + 80))
        s.blit(sblit4, (cardcenter[0], cardcenter[1] + 120))
        s.blit(sblit5, (cardcenter[0], cardcenter[1] + 160))
        s.blit(sopblit, (1000, 90))
        s.blit(opblit1, (1100, 150))
        s.blit(opblit2, (1100, 190))
        s.blit(opblit3, (1100, 230))
        s.blit(opblit4, (1100, 270))
        s.blit(opblit5, (1100, 310))
        s.blit(winblit, wincenter)
        s.blit(winblit2, wincenter2)

    elif scp > 21:
        OVER = True
        wintext = "YOU WIN"
        wintext2 = "Exit window to close game"
        Playsc = "PLAYER SCORECARD"
        Oppsc = "OPPONENT SCORECARD"
        sL1 = valp1[0] + " -  " + str(s1)
        sL2 = valp2[0] + " -  " + str(s2)
        sL3 = valp3[0] + " -  " + str(s3)
        sL4 = valp4[0] + " -  " + str(s4)
        sL5 = valp5[0] + " - " + str(s5)
        sM5 = valo5[0] + " -  " + str(k5)
        sM4 = valo4[0] + " -  " + str(k4)
        sM3 = valo3[0] + " -  " + str(k3)
        sM2 = valo2[0] + " -  " + str(k2)
        sM1 = valo1[0] + " - " + str(k1)
        winblit2 = winfont2.render(wintext2, True, [0, 0, 0], [155, 0, 0])
        winblit = winfont.render(wintext, True, [0, 0, 0], [155, 0, 0])
        splblit = scoresh.render(Playsc, True, [0, 0, 0], [155, 0, 0])
        sopblit = scoresh.render(Oppsc, True, [0, 0, 0], [155, 0, 0])
        sblit1 = cardfont.render(sL1, True, [0, 0, 0], [155, 0, 0])
        sblit2 = cardfont.render(sL2, True, [0, 0, 0], [155, 0, 0])
        sblit3 = cardfont.render(sL3, True, [0, 0, 0], [155, 0, 0])
        sblit4 = cardfont.render(sL4, True, [0, 0, 0], [155, 0, 0])
        sblit5 = cardfont.render(sL5, True, [0, 0, 0], [155, 0, 0])
        opblit1 = cardfont.render(sM1, True, [0, 0, 0], [155, 0, 0])
        opblit2 = cardfont.render(sM2, True, [0, 0, 0], [155, 0, 0])
        opblit3 = cardfont.render(sM3, True, [0, 0, 0], [155, 0, 0])
        opblit4 = cardfont.render(sM4, True, [0, 0, 0], [155, 0, 0])
        opblit5 = cardfont.render(sM5, True, [0, 0, 0], [155, 0, 0])
        s.blit(splblit, (cardcenter[0] - 80, cardcenter[1] - 60))
        s.blit(sblit1, cardcenter)
        s.blit(sblit2, (cardcenter[0], cardcenter[1] + 40))
        s.blit(sblit3, (cardcenter[0], cardcenter[1] + 80))
        s.blit(sblit4, (cardcenter[0], cardcenter[1] + 120))
        s.blit(sblit5, (cardcenter[0], cardcenter[1] + 160))
        s.blit(sopblit, (1000, 90))
        s.blit(opblit1, (1100, 150))
        s.blit(opblit2, (1100, 190))
        s.blit(opblit3, (1100, 230))
        s.blit(opblit4, (1100, 270))
        s.blit(opblit5, (1100, 310))
        s.blit(winblit, wincenter)
        s.blit(winblit2, wincenter2)



s = pygame.display.set_mode([1450, 800])
pygame.display.set_caption("Swisheroo")
COURT = pygame.image.load("Courtn2.png").convert()
icon = pygame.image.load("icon2.jpeg").convert()
pygame.display.set_icon(icon)
l1 = [[pygame.image.load("down1.png").convert(), pygame.image.load("down2.png").convert(),
      pygame.image.load("down3.png").convert(), pygame.image.load("down4.png").convert()],
      [pygame.image.load("left1.png").convert(), pygame.image.load("left2.png").convert(),
      pygame.image.load("left3.png").convert(), pygame.image.load("left4.png").convert()],
      [pygame.image.load("right1.png").convert(),pygame.image.load("right2.png").convert(),
      pygame.image.load("right3.png").convert(),pygame.image.load("right4.png").convert()],
      [pygame.image.load("up1.png").convert(),pygame.image.load("up2.png").convert(),
      pygame.image.load("up3.png").convert(),pygame.image.load("up4.png").convert()]]

l2 = [[pygame.image.load("down1.png").convert(), pygame.image.load("down2.png").convert(),
      pygame.image.load("down3.png").convert(), pygame.image.load("down4.png").convert()],
      [pygame.image.load("left1.png").convert(), pygame.image.load("left2.png").convert(),
      pygame.image.load("left3.png").convert(), pygame.image.load("left4.png").convert()],
      [pygame.image.load("right1.png").convert(),pygame.image.load("right2.png").convert(),
      pygame.image.load("right3.png").convert(),pygame.image.load("right4.png").convert()],
      [pygame.image.load("up1.png").convert(),pygame.image.load("up2.png").convert(),
      pygame.image.load("up3.png").convert(),pygame.image.load("up4.png").convert()]]
l3 = [[pygame.image.load("down1.png").convert(), pygame.image.load("down2.png").convert(),
      pygame.image.load("down3.png").convert(), pygame.image.load("down4.png").convert()],
      [pygame.image.load("left1.png").convert(), pygame.image.load("left2.png").convert(),
      pygame.image.load("left3.png").convert(), pygame.image.load("left4.png").convert()],
      [pygame.image.load("right1.png").convert(),pygame.image.load("right2.png").convert(),
      pygame.image.load("right3.png").convert(),pygame.image.load("right4.png").convert()],
      [pygame.image.load("up1.png").convert(),pygame.image.load("up2.png").convert(),
      pygame.image.load("up3.png").convert(),pygame.image.load("up4.png").convert()]]
l4 =[[pygame.image.load("down1.png").convert(), pygame.image.load("down2.png").convert(),
      pygame.image.load("down3.png").convert(), pygame.image.load("down4.png").convert()],
      [pygame.image.load("left1.png").convert(), pygame.image.load("left2.png").convert(),
      pygame.image.load("left3.png").convert(), pygame.image.load("left4.png").convert()],
      [pygame.image.load("right1.png").convert(),pygame.image.load("right2.png").convert(),
      pygame.image.load("right3.png").convert(),pygame.image.load("right4.png").convert()],
      [pygame.image.load("up1.png").convert(),pygame.image.load("up2.png").convert(),
      pygame.image.load("up3.png").convert(),pygame.image.load("up4.png").convert()]]
l5 = [[pygame.image.load("down1.png").convert(), pygame.image.load("down2.png").convert(),
      pygame.image.load("down3.png").convert(), pygame.image.load("down4.png").convert()],
      [pygame.image.load("left1.png").convert(), pygame.image.load("left2.png").convert(),
      pygame.image.load("left3.png").convert(), pygame.image.load("left4.png").convert()],
      [pygame.image.load("right1.png").convert(),pygame.image.load("right2.png").convert(),
      pygame.image.load("right3.png").convert(),pygame.image.load("right4.png").convert()],
      [pygame.image.load("up1.png").convert(),pygame.image.load("up2.png").convert(),
      pygame.image.load("up3.png").convert(),pygame.image.load("up4.png").convert()]]
f1 = [[pygame.image.load("odown1.png").convert(), pygame.image.load("odown2.png").convert(),
      pygame.image.load("odown3.png").convert(), pygame.image.load("odown4.png").convert()],
      [pygame.image.load("oleft1.png").convert(), pygame.image.load("oleft2.png").convert(),
      pygame.image.load("oleft3.png").convert(), pygame.image.load("oleft4.png").convert()],
      [pygame.image.load("oright1.png").convert(),pygame.image.load("oright2.png").convert(),
      pygame.image.load("oright3.png").convert(),pygame.image.load("oright4.png").convert()],
      [pygame.image.load("oup1.png").convert(),pygame.image.load("oup2.png").convert(),
      pygame.image.load("oup3.png").convert(),pygame.image.load("oup4.png").convert()]]
f2 = [[pygame.image.load("odown1.png").convert(), pygame.image.load("odown2.png").convert(),
      pygame.image.load("odown3.png").convert(), pygame.image.load("odown4.png").convert()],
      [pygame.image.load("oleft1.png").convert(), pygame.image.load("oleft2.png").convert(),
      pygame.image.load("oleft3.png").convert(), pygame.image.load("oleft4.png").convert()],
      [pygame.image.load("oright1.png").convert(),pygame.image.load("oright2.png").convert(),
      pygame.image.load("oright3.png").convert(),pygame.image.load("oright4.png").convert()],
      [pygame.image.load("oup1.png").convert(),pygame.image.load("oup2.png").convert(),
      pygame.image.load("oup3.png").convert(),pygame.image.load("oup4.png").convert()]]
f3 = [[pygame.image.load("odown1.png").convert(), pygame.image.load("odown2.png").convert(),
      pygame.image.load("odown3.png").convert(), pygame.image.load("odown4.png").convert()],
      [pygame.image.load("oleft1.png").convert(), pygame.image.load("oleft2.png").convert(),
      pygame.image.load("oleft3.png").convert(), pygame.image.load("oleft4.png").convert()],
      [pygame.image.load("oright1.png").convert(),pygame.image.load("oright2.png").convert(),
      pygame.image.load("oright3.png").convert(),pygame.image.load("oright4.png").convert()],
      [pygame.image.load("oup1.png").convert(),pygame.image.load("oup2.png").convert(),
      pygame.image.load("oup3.png").convert(),pygame.image.load("oup4.png").convert()]]
f4 = [[pygame.image.load("odown1.png").convert(), pygame.image.load("odown2.png").convert(),
      pygame.image.load("odown3.png").convert(), pygame.image.load("odown4.png").convert()],
      [pygame.image.load("oleft1.png").convert(), pygame.image.load("oleft2.png").convert(),
      pygame.image.load("oleft3.png").convert(), pygame.image.load("oleft4.png").convert()],
      [pygame.image.load("oright1.png").convert(),pygame.image.load("oright2.png").convert(),
      pygame.image.load("oright3.png").convert(),pygame.image.load("oright4.png").convert()],
      [pygame.image.load("oup1.png").convert(),pygame.image.load("oup2.png").convert(),
      pygame.image.load("oup3.png").convert(),pygame.image.load("oup4.png").convert()]]
f5 = [[pygame.image.load("odown1.png").convert(), pygame.image.load("odown2.png").convert(),
      pygame.image.load("odown3.png").convert(), pygame.image.load("odown4.png").convert()],
      [pygame.image.load("oleft1.png").convert(), pygame.image.load("oleft2.png").convert(),
      pygame.image.load("oleft3.png").convert(), pygame.image.load("oleft4.png").convert()],
      [pygame.image.load("oright1.png").convert(),pygame.image.load("oright2.png").convert(),
      pygame.image.load("oright3.png").convert(),pygame.image.load("oright4.png").convert()],
      [pygame.image.load("oup1.png").convert(),pygame.image.load("oup2.png").convert(),
      pygame.image.load("oup3.png").convert(),pygame.image.load("oup4.png").convert()]]
img1 = pygame.image.load("PG1.png").convert()
img2 = pygame.image.load("SG.png").convert()
img3 = pygame.image.load("PG2.png").convert()
img4, img5 = pygame.image.load("PF.png").convert(), pygame.image.load("C.png").convert()
con = mysql.connector.connect(host="localhost", user="root", password="Agasthya0112", database="project")
cursor = con.cursor(buffered=True)
sql1 = "Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where name = 'Kyrie Irving'"
sql2 = "Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where name = 'James Harden'"
sql3 = "Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where name = 'Damian Lillard'"
sql4 = "Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where name = 'Jayson Tatum'"
sql5 = "Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where name = 'Steven Adams'"
sql6 = "Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where position = 'PG' and name not like 'Kyrie Irving' and name not like 'Damian Lillard' order by rand() limit 1"
sql7 = "Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where position = 'SG' and name not like 'James Harden' order by rand() limit 1"
sql8 = "Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where position = 'SF' and name not like 'Damian Lillard' order by rand() limit 1"
sql9 = "Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where position = 'PF' and name not like 'Jayson Tatum' order by rand() limit 1"
sql10 = "Select Name,Shooting_Outside,Shooting_Inside,Defense_Outside,Defense_Inside from players where position = 'C' and name not like 'Steven Adams' order by rand() limit 1"
cursor.execute(sql1)
valp1 = cursor.fetchall()[0]
cursor.execute(sql2)
valp2 = cursor.fetchall()[0]
cursor.execute(sql3)
valp3 = cursor.fetchall()[0]
cursor.execute(sql4)
valp4 = cursor.fetchall()[0]
cursor.execute(sql5)
valp5 = cursor.fetchall()[0]
cursor.execute(sql6)
valo1 = cursor.fetchall()[0]
cursor.execute(sql7)
valo2 = cursor.fetchall()[0]
cursor.execute(sql8)
valo3 = cursor.fetchall()[0]
cursor.execute(sql9)
valo4 = cursor.fetchall()[0]
cursor.execute(sql10)
valo5 = cursor.fetchall()[0]
offopp = "pg"
defplayer = "pg"
activeplayer = "pg"
pass1 = True
pass2 = True
pass3 = True
pass4 = True
pass5 = True
pass1dur = 1
pass2dur = random.randint(7, 9)
pass3dur = random.randint(11, 13)
pass4dur = random.randint(15, 17)
pass5dur = random.randint(3, 5)
a1 = random.randint(1, 10)
block = False
shoot = False
coll = False
collo = False
movement = True
move = True
fin = False
setO = False
setD = False
OVER = False
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
stat1 = "P"
fontdefst = pygame.font.get_fonts()[12]
fontst = pygame.font.SysFont(fontdefst, 50)
mtext = "MISS!"
mcenter = (665, 40)
thptext = "3 POINTER MADE!"
thpcenter = (540, 40)
tptext = "2 POINTER MADE!"
tpcenter = (540, 40)
sc1 = 0
bltext = "BLOCKED!"
shothap = 0
blcenter = (620, 40)
itext = "INTERCEPTED"
icenter = (580, 40)
status = 'OFFENSE'
notransit = True
px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y = 500, 200, 285, 90, 285, 320, 85, 160, 85, 255
oldpx,oldpy,oldp2x,oldp2y,oldp3x,oldp3y,oldp4x,oldp4y,oldp5x,oldp5y = px, py, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y
ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y = 675, 200, 365, 35, 370, 370, 145, 120, 145, 290
oldox,oldoy,oldo2x,oldo2y,oldo3x,oldo3y,oldo4x,oldo4y,oldo5x,oldo5y = ox, oy, o2x, o2y, o3x, o3y, o4x, o4y, o5x, o5y
b1 = ball(ox, oy + 40)
cx, cy = 85, 217
pxo, pyo, p2xo, p2yo, p3xo, p3yo, p4xo, p4yo, p5xo, p5yo = 725, 200, 1050, 40, 1050, 360, 1250, 120, 1250, 290
oldpxo,oldpyo,oldp2xo,oldp2yo,oldp3xo,oldp3yo,oldp4xo,oldp4yo,oldp5xo,oldp5yo = pxo, pyo, p2xo, p2yo, p3xo, p3yo, p4xo, p4yo, p5xo, p5yo
oxo, oyo, o2xo, o2yo, o3xo, o3yo, o4xo, o4yo, o5xo, o5yo = 925, 200, 1100, 90, 1100, 320, 1300, 160, 1300, 255
oldoxo, oldoyo, oldo2xo, oldo2yo, oldo3xo, oldo3yo, oldo4xo, oldo4yo, oldo5xo, oldo5yo = oxo, oyo, o2xo, o2yo, o3xo, o3yo, o4xo, o4yo, o5xo, o5yo
B2 = ball(pxo, pyo)
c2x, c2y = 1375, 225
blittime = None
dtime = 22000
otime = 22000
i = True
coord = []
b, b2 = 280, 130
count = 0
a = 465
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
    nonpcollide()
    s.blit(text, textcenter)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if notransit == True:
                if status == 'DEFENSE':
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        LEFT = True
                        RIGHT = False
                        UP = False
                        DOWN = False
                        player.movement(curplayer(), -20, 0)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.movement(curplayer(), 20, 0)
                        RIGHT = True
                        LEFT = False
                        UP = False
                        DOWN = False
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        UP = True
                        LEFT = False
                        RIGHT = False
                        DOWN = False
                        player.movement(curplayer(), 0, -20)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        DOWN = True
                        LEFT = False
                        RIGHT = False
                        UP = False
                        player.movement(curplayer(), 0, 20)
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
                elif status == 'OFFENSE':
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        LEFT = True
                        RIGHT = False
                        UP = False
                        DOWN = False
                        player.movement(useplayer(), -20, 0)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        RIGHT = True
                        LEFT = False
                        UP = False
                        DOWN = False
                        player.movement(useplayer(), 20, 0)
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        UP = True
                        LEFT = False
                        RIGHT = False
                        DOWN = False
                        player.movement(useplayer(), 0, -20)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        DOWN = True
                        LEFT = False
                        RIGHT = False
                        UP = False
                        player.movement(useplayer(), 0, 20)
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
                            if scp < 21:
                                shoot = True
                                if activeplayer == "pg":
                                    player.shot(useplayer(), valp1[1:3], curvalD(), activedefender())
                                    s1, scp = s1 + player.score(useplayer()), scp + player.score(useplayer())
                                elif activeplayer == "sg":
                                    player.shot(useplayer(), valp2[1:3], curvalD(), activedefender())
                                    s2, scp = s2 + player.score(useplayer()), scp + player.score(useplayer())
                                elif activeplayer == "sf":
                                    player.shot(useplayer(), valp3[1:3], curvalD(), activedefender())
                                    s3, scp = s3 + player.score(useplayer()), scp + player.score(useplayer())
                                elif activeplayer == "pf":
                                    player.shot(useplayer(), valp4[1:3], curvalD(), activedefender())
                                    s4, scp = s4 + player.score(useplayer()), scp + player.score(useplayer())
                                elif activeplayer == "c":
                                    player.shot(useplayer(), valp5[1:3], curvalD(), activedefender())
                                    s5, scp = s5 + player.score(useplayer()), scp + player.score(useplayer())
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
    if notransit == False:
        sec = 5
        tleft = "Time Left is : " + str(sec)
    else:
        if status == "OFFENSE":
            sec = ((otime - pygame.time.get_ticks()) // 1000)
            tleft = "Time Left is : " + str(sec)
        elif status == "DEFENSE":
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
            opponent.update(activedefender())

    pygame.display.update()
    if RUN == False:
        pygame.quit()
