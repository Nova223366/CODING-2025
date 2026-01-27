import math
import random
import pygame

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
PLAYER_START_X = 351
PLAYER_START_Y = 698
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 1
ENEMY_SPEED_Y = 2
BULLET_SPEED_Y = 4
COLLISION_DISTANCE = 20

pygame.init()

#Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load(
    r'C:\CODING 2025\Space_invader\png-transparent-starry-night-night-sky-star-nebula-galaxy-background-texture-other-atmosphere-thumbnail.png'
)

background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))



#captions and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('C:\CODING 2025\Space_invader\png-transparent-pistol-gun-computer-icons-rifle-weapon-weapon-text-logo-handgun-thumbnail.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('C:\CODING 2025\Space_invader\png-transparent-thunder-plane-airplane-red-plane-game-plane-pixel-sprite-airplane-game-food-vertebrate-thumbnail.png')
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('C:\CODING 2025\Space_invader\png-transparent-action-toy-figures-figurine-national-entertainment-collectibles-association-alien-prototype-alian-ccedil-as-action-toy-figures-suit-statue-thumbnail.png'))
    enemyImg[i] = pygame.transform.scale(enemyImg[i], (64, 64))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64)) #64 is the size of the enemy
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet
bulletImg = pygame.image.load('C:\CODING 2025\Space_invader\image.png')
bulletImg = pygame.transform.scale(bulletImg, (32, 32))
bulletX = 0
bulletY = PLAYER_START_Y
bullet_change = BULLET_SPEED_Y
bullet_state = "ready"  # "ready" - You can't see the bullet on the screen; "fire" - The bullet is currently moving

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    #Display the current score on the screen 
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

    # render function help to display the font 
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

# Game Loop
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))

    # Enemy movement
    for i in range (num_of_enemies):
        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Collision check
        if is_collision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        enemy(enemyX[i], enemyY[i], i)
    # Bullet movement
    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_change
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
pygame.quit()