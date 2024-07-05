import pygame
import random
import math

# Initialize the Pygame
pygame.init()

# Display the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background1.png").convert()

# Title and Icon
pygame.display.set_caption("Alien Shooter")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Player
playerIMG = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyIMG = pygame.image.load("enemy.png")
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 50

# Bullet
# Ready - You can't see the bullet
# Fire - The bullet is currently moving
bulletIMG = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"


#score
score_value = 0
font= pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

# game over text

over_font= pygame.font.Font('freesansbold.ttf',70)

def show_score(x,y):
    score = font.render("Score: "+ str(score_value),True, (255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text,(200, 250))

# To draw player on screen
def player(x, y):
    screen.blit(playerIMG, (x, y))


def enemy(x, y):
    screen.blit(enemyIMG, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x + 16, y + 10))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop (for things that are needed to be constant in a game under running loop)
running = True
while running:

    # RGB = Red Blue Green (0 - 255)
    screen.fill((0, 0, 0))

    # Background image
    screen.blit(background, (0, 0))

    # To close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    #get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # Game boundary for player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    # Game movement for enemy

    if enemyY > 430:
        enemyY = 2000
        game_over_text()
        #break

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    # Game movement for bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = iscollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1
       #enemyX = random.randint(0, 735)
       #enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_score(textX,textY)
    pygame.display.update()