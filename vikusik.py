
import pygame

pygame.init()
window = pygame.display.set_mode((1550, 810))
background = pygame.image.load("Slider-CL01-Background.png")
background = pygame.transform.scale(background, (1550, 810))
clock = pygame.time.Clock()

pygame.mixer.music.load("Toby Fox - Megalovania.mp3.crdownload")
pygame.mixer.music.play(-1)

font = pygame.font.SysFont('Arial', 80)
score_font = pygame.font.SysFont('Arial', 40)

class Pepsi:
    def __init__(self, x, y, width, height, step, image_pepsi=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.step = step
        self.image = pygame.transform.scale(pygame.image.load(image_pepsi), (self.width, self.height))

    def draw(self):
        window.blit(self.image, (self.x, self.y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.step
        if keys[pygame.K_RIGHT] and self.x < 1550 - self.width:
            self.x += self.step

class Enemy(Pepsi):
    def draw(self):
        window.blit(self.image, (self.x, self.y))

class Boll:
    def __init__(self, x, y, width, height, speed, radius, image_boll):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed_x = speed
        self.speed_y = speed
        self.radius = radius
        self.image = pygame.image.load(image_boll)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0 or self.x + self.width >= 1550:
            self.speed_x *= -1
        if self.y <= 0:
            self.speed_y *= -1

    def check_collision_with_platform(self, platform):
        ball_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        platform_rect = pygame.Rect(platform.x, platform.y, platform.width, platform.height)
        if ball_rect.colliderect(platform_rect):
            if self.speed_y > 0:
                self.speed_y *= -1
                self.y = platform.y - self.height

    def check_collision_with_enemy(self, enemy):
        ball_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
        return ball_rect.colliderect(enemy_rect)

# --- Початковий екран ---
def show_start_screen():
    window.fill((0, 0, 0))
    text_surface = font.render("Натисни SHIFT, щоб почати", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(1550 // 2, 810 // 2))
    window.blit(text_surface, text_rect)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    waiting = False

# --- Ініціалізація гри ---
player_image = "loading-bar-four-quarters-game-asset-2d-icon-transparent-background-png.webp"
enemy_image = "Blue-Monster-PNG-File.png"
boll_image = "tennis-ball-png-photo-2.png"

show_start_screen()

player = Pepsi(550, 650, 150, 100, 15, player_image)

monsters = []
start_x = 5
start_y = 5
for i in range(4):
    y = start_y + (55 * i)
    for j in range(10):
        x = start_x + (150 * j)
        enemy = Enemy(x, y, 100, 100, 0, enemy_image)
        monsters.append(enemy)

boll = Boll(500, 500, 70, 70, 5, 25, boll_image)

game = True
game_over = False
score = 0
total_monsters = len(monsters)
victory = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if not game_over and not victory:
        player.update()
        boll.move()
        boll.check_collision_with_platform(player)

        for enemy in monsters[:]:
            if boll.check_collision_with_enemy(enemy):
                monsters.remove(enemy)
                boll.speed_y *= -1
                boll.speed_x += 1 if boll.speed_x > 0 else -1
                boll.speed_y += 1 if boll.speed_y > 0 else -1
                score += 1
                break

        if boll.y + boll.height >= 810:
            game_over = True

        if score == total_monsters:
            victory = True

    window.fill((0, 0, 0))
    window.blit(background, (0, 0))

    for enemy in monsters:
        enemy.draw()

    player.draw()
    window.blit(boll.image, (boll.x, boll.y))

    score_surface = score_font.render(f"Ти збив {score} із {total_monsters}", True, (255, 255, 255))
    window.blit(score_surface, (10, 700))

    if game_over:
        text_surface = font.render("Гра завершена!", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(1550 // 2, 810 // 2))
        window.blit(text_surface, text_rect)
    elif victory:
        text_surface = font.render("Ти виграв!", True, (0, 255, 0))
        text_rect = text_surface.get_rect(center=(1550 // 2, 810 // 2))
        window.blit(text_surface, text_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
