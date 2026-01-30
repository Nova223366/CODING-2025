import pygame
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard Control + Border Color Change")

clock = pygame.time.Clock()

def random_color():
    return random.randint(0,255), random.randint(0,255), random.randint(0,255)

class Box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = random_color()
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        touched_border = False

        if self.rect.left <= 0:
            self.rect.left = 0
            touched_border = True
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            touched_border = True
        if self.rect.top <= 0:
            self.rect.top = 0
            touched_border = True
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            touched_border = True

        if touched_border:
            self.color = random_color()
            self.image.fill(self.color)

box = Box()
sprites = pygame.sprite.Group(box)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    box.update(keys)

    screen.fill((30, 30, 30))
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()