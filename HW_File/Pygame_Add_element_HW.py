import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My first game screen")

BACKGROUND_COLOR = (0, 0, 0)  
RECT_COLOR = (255, 0, 0)  
RECT_WIDTH, RECT_HEIGHT = 120, 60
rect_x = (WIDTH - RECT_WIDTH) // 2
rect_y = (HEIGHT - RECT_HEIGHT) // 2
rectangle = pygame.Rect(rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT)

FONT_COLOR = (255, 255, 255)  
font = pygame.font.SysFont(None, 36)
text_surface = font.render("Hello Pygame!", True, FONT_COLOR)
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, RECT_COLOR, rectangle)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

pygame.quit()