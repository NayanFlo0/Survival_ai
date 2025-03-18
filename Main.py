from Environment import *


# Definitions
world_dimensions = [15, 20]
house_shape = [4, 4]
house_loc = [2, 2]
player_loc = [3, 4]
FPS = 10a
clock = pygame.time.Clock()
world = Environment(world_dimensions, house_loc=house_loc)

# Main game loop
running = True
while running:

    # Draw everything
    world.screen.fill(world.COLOURS["WHITE"])
    world.renderer()
    running = world.player()

    # Update the display
    pygame.display.flip()

    # Control FPS
    clock.tick(FPS)


