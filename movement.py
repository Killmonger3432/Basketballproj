import pygame
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
clock = pygame.time.Clock()
x = 50
y = 400
width = 64
height = 64
vel = 10
up = False
down = False
jumpCount = 10
left = False
right = False
walkCount = 0
char = pygame.image.load('down1.png')
bg = pygame.image.load('w.png')
def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    if walkCount +1 >= 4:
        walkCount = 0
    if left and not up and not down and not right:
        walkCount = walkCount + 1
        win.blit(walkleft[walkCount], (x, y))
        print("left")
    elif right and not up and not down and not left:
        walkCount = walkCount + 1
        win.blit(walkright[walkCount],(x,y))
        print("right")
    elif up and not left and not right and not down:
        win.blit(walkup[walkCount],(x,y))
        walkCount = walkCount + 1
        print("up")
    elif down and not left and not right and not up:
        win.blit(walkdown[walkCount],(x,y))
        walkCount = walkCount + 1
        print("down")
    elif right and down and not left and not up:
        win.blit(walkright[walkCount], (x, y))
        walkCount = walkCount +1
        print("4")
    elif left and down and not right and not up:
        win.blit(walkleft[walkCount], (x, y))
        walkCount = walkCount + 1
        print("3")
    elif right and up and not left and not down:
        win.blit(walkright[walkCount], (x, y))
        walkCount = walkCount + 1
        print("1")
    elif left and up and not right and not down:
        win.blit(walkleft[walkCount], (x, y))
        walkCount = walkCount + 1
        print("2")
    else: #not left and not right and not up and not down:
        win.blit(char, (x, y))

        walkCount = 0

    pygame.display.update()
while mainloop:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
    keys = pygame.key.get_pressed()
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
    if up or down or right or left :
        print(up,down,left,right)
    redrawGameWindow()
pygame.quit()