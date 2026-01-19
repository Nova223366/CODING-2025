import pygame
import random

pygame.init()


WIDTH, HEIGHT = 500, 400


SPRITE_COLOR_CHANGE = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE = pygame.USEREVENT + 2


BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-3, 3]), random.choice([-3, 3])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.velocity[0] *= -1
            boundary_hit = True

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.velocity[1] *= -1
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(
                pygame.event.Event(SPRITE_COLOR_CHANGE, sprite=self)
            )
            pygame.event.post(
                pygame.event.Event(BACKGROUND_COLOR_CHANGE)
            )

    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Color Change on Boundary Hit")

bg_color = BLUE
screen.fill(bg_color)


all_sprites = pygame.sprite.Group()
sp1 = Sprite(WHITE, 20, 30)
sp1.rect.topleft = (
    random.randint(0, WIDTH - 20),
    random.randint(0, HEIGHT - 30)
)
all_sprites.add(sp1)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == SPRITE_COLOR_CHANGE:
            event.sprite.change_color()

        elif event.type == BACKGROUND_COLOR_CHANGE:
            bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])

    all_sprites.update()
    screen.fill(bg_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
