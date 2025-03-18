
house_shape = ["#######",
               "#     #",
               "#     #",
               "### ###"]

print(len(house_shape))
print(len(house_shape[0]))

import pygame

# Constants
TILE_SIZE = 40  # Size of each tile in pixels
MAP = [
    "##########",
    "#A       #",
    "#        #",
    "#        #",
    "#   # #  #",
    "#  ##### #",
    "#        #",
    "##########"
]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)

# Pygame Initialization
pygame.init()

# Screen dimensions
WIDTH = len(MAP[0]) * TILE_SIZE
HEIGHT = len(MAP) * TILE_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Grid Movement")

# Find player start position
player_x, player_y = 0, 0
for y, row in enumerate(MAP):
    for x, tile in enumerate(row):
        if tile == "A":
            player_x, player_y = x, y

# Game loop
running = True
while running:
    pygame.time.delay(100)  # Control speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()

    # Movement Logic
    new_x, new_y = player_x, player_y
    if keys[pygame.K_w]:
        new_y -= 1
    if keys[pygame.K_s]:
        new_y += 1
    if keys[pygame.K_a]:
        new_x -= 1
    if keys[pygame.K_d]:
        new_x += 1

    # Check if new position is not a wall
    if MAP[new_y][new_x] != "#":
        player_x, player_y = new_x, new_y

    # Rendering
    screen.fill(BLACK)  # Clear screen

    for y, row in enumerate(MAP):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if tile == "#":
                pygame.draw.rect(screen, WHITE, rect)  # Draw wall
            elif (x, y) == (player_x, player_y):
                pygame.draw.rect(screen, RED, rect)  # Draw player

    pygame.display.update()

pygame.quit()


