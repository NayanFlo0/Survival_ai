import pygame
import random



class Environment:

    def __init__(self, map_dimensions=None, player_loc=None, house_shape=None, house_loc=None, point_amt=None, TILE_SIZE=20):
        self.map_dimensions = [12, 12] if map_dimensions is None else [map_dimensions[0] + 2, map_dimensions[1] + 2]
        self.player_loc = [self.map_dimensions[0] // 2, self.map_dimensions[1] // 2] if player_loc is None else player_loc
        self.house_shape = [4, 7] if house_shape is None else [house_shape[0] + 1, house_shape[1] + 1]
        self.house_loc = [(self.map_dimensions[0] - self.house_shape[0]) // 2, (self.map_dimensions[1] - self.house_shape[1]) // 2] if house_loc is None else house_loc
        self.TILE_SIZE = TILE_SIZE
        self.point_amt = 10 if point_amt is None else point_amt
        self.score = 0

        # Initialize Pygame
        pygame.init()

        # Colors
        self.COLOURS = {"WHITE": (255, 255, 255),
                        "BLACK": (0, 0, 0),
                        "RED": (255, 0, 0),
                        "GREEN": (0, 255, 0),
                        "BLUE": (0, 0, 255),
                        "YELLOW": (255, 255, 0)}

        # Create the screen
        self.screen = pygame.display.set_mode([20 * self.map_dimensions[1], 20 * self.map_dimensions[0]])
        pygame.display.set_caption("Survival.ai")

        # Clock for controlling FPS
        clock = pygame.time.Clock()

        # Map / House
        self.map = []
        for i in range(self.map_dimensions[0]):
            buffer = []
            for j in range(self.map_dimensions[1]):
                if (i == 0 or j == 0 or i == self.map_dimensions[0] - 1 or j == self.map_dimensions[1] - 1
                        or ((self.house_loc[0] <= i <= self.house_loc[0] + self.house_shape[0]) and (
                                j == self.house_loc[1] or j == self.house_loc[1] + self.house_shape[1]))
                        or ((self.house_loc[1] <= j <= self.house_loc[1] + self.house_shape[1]) and (
                                i == self.house_loc[0] or i == self.house_loc[0] + self.house_shape[0]))):
                    buffer.append('#')
                else:
                    buffer.append(' ')
            self.map.append(buffer)

    # Random Point Function
        self.place_points()

    def place_points(self):

        placed = 0
        while placed < self.point_amt:
            x = random.randint(1, self.map_dimensions[0] - 2)
            y = random.randint(1, self.map_dimensions[1] - 2)
            if self.map[x][y] == ' ' and [x, y] != self.player_loc:
                self.map[x][y] = 'P'
                placed += 1



    # Function to render the map and points
    def renderer(self):
        for i in range(self.map_dimensions[0]):
            for j in range(self.map_dimensions[1]):
                if self.map[i][j] == '#':
                    pygame.draw.rect(self.screen, self.COLOURS["BLACK"],
                                     (j * self.TILE_SIZE, i * self.TILE_SIZE,
                                      self.TILE_SIZE, self.TILE_SIZE))
                    # Renders Points
                elif self.map[i][j] == 'P':
                    pygame.draw.circle(self.screen, self.COLOURS["YELLOW"],
                                       (j * self.TILE_SIZE + self.TILE_SIZE // 2, i * self.TILE_SIZE + self.TILE_SIZE // 2),
                                       self.TILE_SIZE // 3)
                # Renders Player
        pygame.draw.rect(self.screen, self.COLOURS["BLUE"],
                         (self.player_loc[1] * self.TILE_SIZE, self.player_loc[0] * self.TILE_SIZE,
                          self.TILE_SIZE, self.TILE_SIZE))

    # Player functions
    def player(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and self.map[self.player_loc[0] - 1][self.player_loc[1]] != "#":
            self.player_loc[0] -= 1
        if key[pygame.K_DOWN] and self.map[self.player_loc[0] + 1][self.player_loc[1]] != "#":
            self.player_loc[0] += 1
        if key[pygame.K_LEFT] and self.map[self.player_loc[0]][self.player_loc[1] - 1] != "#":
            self.player_loc[1] -= 1
        if key[pygame.K_RIGHT] and self.map[self.player_loc[0]][self.player_loc[1] + 1] != "#":
            self.player_loc[1] += 1

        if self.map[self.player_loc[0]][self.player_loc[1]] == 'P':
            self.score += 1
            self.map[self.player_loc[0]][self.player_loc[1]] = ' '


        #Display player score
        font = pygame.font.Font(None, 26)
        score_text = font.render(f"Score: {self.score}", True, self.COLOURS["BLACK"])
        self.screen.blit(score_text, (350, 20))


        # Check if the new location has a point
        if self.map[self.player_loc[0]][self.player_loc[1]] == 'P':
            self.score += 1
            self.map[self.player_loc[0]][self.player_loc[1]] = ' '


        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def __del__(self):
        # Quit Pygame
        pygame.quit()
