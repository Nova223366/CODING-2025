import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 40)
text = font.render("No Image", True, WHITE)
text_rect = text.get_rect(center=(250, 250))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()