import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
# this is the UI you will see when you run the code
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Avoid the Falling Objects!use arrow keys to move PLAY")

# Colors
# the color options that are currently here
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
LIGHT_BLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player properties
player_size = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - player_size - 10
player_speed = 10

# Enemy properties
enemy_size = 50
enemy_speed = 7
enemies = []

# Function to spawn enemies
def spawn_enemy():
    x_pos = random.randint(0, SCREEN_WIDTH - enemy_size)
    enemies.append([x_pos, 0])

# Function to move enemies
def move_enemies():
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > SCREEN_HEIGHT:
            enemies.remove(enemy)

# Function to detect collisions
def detect_collision(player_x, player_y, enemies):
    for enemy in enemies:
        if (
            enemy[0] < player_x < enemy[0] + enemy_size
            or enemy[0] < player_x + player_size < enemy[0] + enemy_size
        ):
            if enemy[1] < player_y < enemy[1] + enemy_size or enemy[1] < player_y + player_size < enemy[1] + enemy_size:
                return True
    return False

# Main game loop
running = True
spawn_timer = 0

while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keys for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_speed
    
    # Spawn enemies periodically
    spawn_timer += 1
    if spawn_timer > 30:  # Adjust spawn rate
        spawn_enemy()
        spawn_timer = 0
    
    # Move enemies
    move_enemies()
    
    # Check for collision
    if detect_collision(player_x, player_y, enemies):
        print("videojuevo Over!ycercftbeshkndcysgeucbgfsyetbcykhseugcxfrycuishfyuesuivhievyufybuecsyfubibeskr,cfhnihifucbtfryvjchsuitjycg")
        running = False
    
    # Draw the player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    
    # Draw the enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))
    
    # Update the screen
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
print("how to download is type pip install pygame in bash")
print("you can customize the color of the things you see in the game")
print("you can also ajust the spawn rate of the enimies")