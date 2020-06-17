import pygame
#import time
pygame.init()
mainloop = True
screen = pygame.display.set_mode((1800, 1000))
walkright = [pygame.image.load('right1.png'), pygame.image.load('right2.png'), pygame.image.load('right3.png'),
             pygame.image.load('right4.png')]
walkleft = [pygame.image.load('left1.png'), pygame.image.load('left2.png'), pygame.image.load('left3.png'),
            pygame.image.load('left4.png')]
walkup = [pygame.image.load('up1.png'), pygame.image.load('up2.png'), pygame.image.load('up3.png'),
          pygame.image.load('up4.png')]
walkdown = [pygame.image.load('down1.png'), pygame.image.load('down2.png'), pygame.image.load('down3.png'),
            pygame.image.load('down4.png')]
win = pygame.display.set_mode((1500, 800))
char = pygame.image.load('down1.png')
char2 = pygame.image.load('down1.png')
clock = pygame.time.Clock()
x2 = 150
y2 = 400
x1 = 50
y1 = 400
width = 64
height = 64
vel = 10
up = False
player1 = False
player2 = False
down = False
jumpCount = 10
left = False
right = False
walkCount = 0
char = pygame.image.load('down1.png')
bg = pygame.image.load('w.png')
def movement(keys,x,y,vel):

    global left
    global right
    global up
    global down

    if keys[pygame.K_LEFT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and not keys[pygame.K_RIGHT] and x > vel:
        x -= vel
        left = True
        right = False
        up = False
        down = False
    elif keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and x < 800 - width - vel:
        x += vel
        left = False
        right = True
        up = False
        down = False
    elif keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_DOWN] and y > 0:
        y -= vel
        left = False
        right = False
        up = True
        down = False
    elif keys[pygame.K_DOWN] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_UP] and y < 1500 - height:
        y += vel
        left = False
        right = False
        up = False
        down = True

    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT]:
        right = True
        left = False
        up = True
        down = False
        y -= vel
        x += vel
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP]:
        right = False
        left = True
        up = False
        down = True
        y += vel
        x -= vel
    elif keys[pygame.K_UP] and keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN]:
        right = False
        left = True
        up = True
        down = False
        y -= vel
        x -= vel
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_LEFT]:
        right = True
        left = False
        up = False
        down = True
        y += vel
        x += vel
    else:
        right = False
        left = False
        up = False
        down = False
        walkCount = 0
    return(x,y)

def redrawGameWindow(x,y):
    global walkCount
    #win.blit(bg, (0, 0))
    if walkCount +1 >= 4:
        walkCount = 0
    if left and not up and not down and not right:
        walkCount = walkCount + 1
        win.blit(walkleft[walkCount], (x, y))

    elif right and not up and not down and not left:
        walkCount = walkCount + 1
        win.blit(walkright[walkCount],(x,y))

    elif up and not left and not right and not down:
        win.blit(walkup[walkCount],(x,y))
        walkCount = walkCount + 1

    elif down and not left and not right and not up:
        win.blit(walkdown[walkCount],(x,y))
        walkCount = walkCount + 1

    elif right and down and not left and not up:
        win.blit(walkright[walkCount], (x, y))
        walkCount = walkCount +1

    elif left and down and not right and not up:
        win.blit(walkleft[walkCount], (x, y))
        walkCount = walkCount + 1

    elif right and up and not left and not down:
        win.blit(walkright[walkCount], (x, y))
        walkCount = walkCount + 1

    elif left and up and not right and not down:
        win.blit(walkleft[walkCount], (x, y))
        walkCount = walkCount + 1

    else: #not left and not right and not up and not down:
        win.blit(char, (x, y))

        walkCount = 0

    #pygame.display.update()
while mainloop:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        player1=True
        player2= False
    if keys[pygame.K_2]:
        player1= False
        player2 = True
    if player1 :
        x1, y1 = movement(keys, x1, y1, vel)
        redrawGameWindow(x1,y1)
        win.blit(char2, (x2, y2))
    if player2 :
        x2, y2 = movement(keys, x2, y2, vel)
        redrawGameWindow(x2,y2)
        win.blit(char, (x1, y1))
    pygame.display.update()

    win.blit(bg, (0, 0))
    #if all([b == 0 for b in keys]):
    #time.sleep(0.2)
   # win.blit(char, (x1, y1))
    #win.blit(char2, (x2, y2))
pygame.quit()
