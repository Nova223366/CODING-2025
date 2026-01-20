import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Let's Add Sprites!")

class RectSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def move(self, dx, dy):
        """Simple method to update position."""
        self.rect.x += dx
        self.rect.y += dy

player = RectSprite(BLUE, 50, 50, 100, 100)
static_block = RectSprite(RED, 50, 50, 400, 300)


all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(static_block)

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    speed = 5
    if keys[pygame.K_LEFT]:
        player.move(-speed, 0)
    if keys[pygame.K_RIGHT]:
        player.move(speed, 0)
    if keys[pygame.K_UP]:
        player.move(0, -speed)
    if keys[pygame.K_DOWN]:
        player.move(0, speed)

    screen.fill(WHITE)           
    all_sprites.draw(screen)     
    pygame.display.flip()        

    clock.tick(60)               

pygame.quit()

