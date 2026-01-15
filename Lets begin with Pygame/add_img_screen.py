import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500  # Key word likly

display_surface = pygame.display.set_mod((SCREEN_WIDTH, SCREEN_HEIGHT))

background = image = pygame.transform.scale(
    pygame.image.load(r'https://www.pixelstalk.net/wp-content/uploads/2016/07/Background-Beautiful-Nature-Images-HD.jpg').convert(),(SCREEN_WIDTH, SCREEN_HEIGHT)

)

penguin_image = pygame.transform.scale(
    pygame.image.load(r'https://tse3.mm.bing.net/th/id/OIP.t1p8TBohAPgQjzfvfwAsLgHaFj?pid=Api&P=0&h=180').convert_alpha(), (100, 100)
)
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)
)

text = pygame.font.Font(None, 36).render('Hello World', True, pygame.color("orange"))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2 + 110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        pygame.display.update()
        clock.tick(30)
    pygame.quit()

    if __name__ == '__main__':
        game_loop()
