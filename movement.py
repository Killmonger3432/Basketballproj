import pygame
pygame.init()
win = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("First Game")
walkRight = [pygame.image.load('right1.png'), pygame.image.load('right2.png'), pygame.image.load('right3.png'),
             pygame.image.load('right4.png')]
walkLeft = [pygame.image.load('left1.png'), pygame.image.load('left2.png'), pygame.image.load('left3.png'),
            pygame.image.load('left4.png')]
walkup = [pygame.image.load('up1.png'), pygame.image.load('up2.png'), pygame.image.load('up3.png'),
          pygame.image.load('up4.png')]
walkdown = [pygame.image.load('down1.png'), pygame.image.load('down2.png'), pygame.image.load('down3.png'),
            pygame.image.load('down4.png')]
bg = pygame.image.load('w.png')
char = pygame.image.load('down1.png')
clock = pygame.time.Clock()
x = 50
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
up = False
down = False
walkCount = 0
def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    if walkCount + 1 >= 4:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount], (x, y))
        walkCount += 1
    if up:
        win.blit(walkup[walkCount], (x, y))
        walkCount += 1
    elif down:
        win.blit(walkdown[walkCount], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    pygame.display.update()
# mainloop
run = True
while run:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
        up = False
        down = False
    elif keys[pygame.K_RIGHT] and x < 800 - width - vel:
        x += vel
        right = True
        left = False
        up = False
        down = False
    if keys[pygame.K_UP] and y > 0:
        y -= vel
        right = False
        left = False
        up = True
        down = False
    elif keys[pygame.K_DOWN] and y < 1500 - height:
        y += vel
        right = False
        left = False
        up = False
        down = True
    else:
        right = False
        left = False
        up = False
        down = False
        walkCount = 0
    redrawGameWindow()
pygame.quit()
