import pygame

pygame.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Addition with Input")

font = pygame.font.Font(None, 40)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

input_text = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if stage == 1:
                    num1 = int(input_text)
                    input_text = ""
                    stage = 2
                elif stage == 2:
                    num2 = int(input_text)
                    input_text = ""
                    stage = 3
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                if event.unicode.isdigit():
                    input_text += event.unicode

    screen.fill(WHITE)

    if stage == 1:
        msg = font.render("Enter first number:", True, BLACK)
        screen.blit(msg, (50, 50))
    elif stage == 2:
        msg = font.render("Enter second number:", True, BLACK)
        screen.blit(msg, (50, 50))
    else:
        result = num1 + num2
        msg = font.render(f"Result: {num1} + {num2} = {result}", True, BLACK)
        screen.blit(msg, (50, 50))

    input_surface = font.render(input_text, True, BLACK)
    screen.blit(input_surface, (50, 120))

    pygame.display.update()

pygame.quit()