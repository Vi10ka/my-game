import pygame
pygame.init()
window=pygame.display.set_mode((1400, 715))
background=pygame.image.load("Slider-CL01-Background.png")
background=pygame.transform.scale(background, (1400, 715))
clock=pygame.time.Clock()
class Pepsi:
    def __init__(self, x, y, width, height, step, image_pepsi):
        self.image=pygame.image.load(image_pepsi)
        self.image=pygame.transform.scale(self.image, (100, 100))
        self.step=step
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def draw(self, x, y):
        window.blit(self.image, (self.x, self.y))

    def update(self):
        keys=pygame.key.get_pressed()
        if event.keys==pygame.K_LEFT:
            self.x-=self.step
        if event.keys==pygame.K_RIGHT:
            self.x+=self.step
player=Pepsi(550, 350, 10, 10, 5, "loading-bar-four-quarters-game-asset-2d-icon-transparent-background-png.webp")
game=True
while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
    window.fill((0, 0, 0))
    window.blit(background, (0, 0))
    player.draw(10, 10)
    pygame.display.update()
    clock.tick(40)
pygame.quit()