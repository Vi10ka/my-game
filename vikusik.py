import pygame
pygame.init()
window=pygame.display.set_mode((1400, 715))
background=pygame.image.load("Slider-CL01-Background.png")
background=pygame.transform.scale(background, (1400, 715))
clock=pygame.time.Clock()
pygame.mixer.music.load("Toby Fox - Megalovania.mp3.crdownload")
pygame.mixer.music.play(-1)
class Pepsi():
    def __init__(self, x, y, width, height, step, image_pepsi):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.step=step
        self.image=pygame.image.load(image_pepsi)
        self.image=pygame.transform.scale(self.image, (self.width, self.height))
    
    def draw(self, x, y):
        window.blit(self.image, (self.x, self.y))

    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]and self.x>0:
            self.x-=self.step
        if keys[pygame.K_RIGHT]and self.x<1400-100:
            self.x+=self.step 



class Enemy(Pepsi):
    def draw(self, x, y):
        window.blit(self.image, (self.x, self.y))



class Boll():
    def __init__(self, x, y, width, height, speed, radius, image_boll):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.speed_x=speed
        self.speed_y=speed
        self.radius=radius
        self.image=pygame.image.load(image_boll)
        self.image=pygame.transform.scale(self.image, (self.width, self.height))

    
    def move(self):
        self.x+=self.speed_x
        self.y+=self.speed_y

        if self.x <= self.radius or self.x >= self.radius:
            self.speed_x*=-1
        if self.y <= self.radius:
            self.speed_y*=-1

player=Pepsi(550, 350, 10, 10, 15, "loading-bar-four-quarters-game-asset-2d-icon-transparent-background-png.webp")
#enemy=Enemy(100, 100, 100, 100, 0, "enemy.png")
boll=Boll(100, 100, 10, 10, 15, 0, "222.png")
# створення ворогів
start_x = 5
start_y = 5
monsters = []
for i in range(4):
    y = start_y + (55 * i)
    x = start_x + (25 * i)
    for j in range(4):
        enemy = Enemy(x, y, 100, 100, 0, "enemy.png")
        monsters.append(enemy)
        x += 55
game=True
while game:
    for enemy in monsters:
        enemy.draw(10, 10)
        enemy.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False

    window.fill((0, 0, 0))
    window.blit(background, (0, 0))
    player.draw(10, 10)
    pygame.display.update()
    player.update()
    enemy.draw(10, 10)
    boll.move()
    pygame.display.update()
    clock.tick(40)
pygame.quit()
