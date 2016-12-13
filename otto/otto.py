import pygame, sys
from pygame.locals import *
from worldmap import *
import time

# Testing purposes only.
DEBUG = False

# Basic map parametres. See documentation.
TILE_SIZE = 8
MAP_WIDTH = 64
MAP_HEIGHT = 64

# Colour values of drawn tiles.
RED = (128, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 128)
GREY = (212, 212, 212)
BROWN = (220, 110, 110)

t = time.time()

worldmap = Worldmap(MAP_WIDTH, MAP_HEIGHT)

if DEBUG:
    # For testing purposes only. Adjust the map in worldmap.py.
    worldmap.debug_creation()
else:
    # Standard map generation.
    worldmap.create_forests(10) # 10 forest tiles
    worldmap.grow_forests(1200) # "Organically" grow the 24 forest tiles into ~1000 ones.
    worldmap.create_cities(1, 8, 32)
    worldmap.create_cities(1, 58, 32)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))

print("Time taken: {} seconds.".format(time.time() - t))

while True:
    # Main loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            # Hit space to draw a road between two randomly chosen cities (using A* to determine path)
            t = time.time()
            worldmap.draw_roads()
            print("Time taken: {} seconds.".format(time.time() - t))
        if event.type == pygame.MOUSEBUTTONUP:
            # Report tile data on mouse click
            pos = pygame.mouse.get_pos()
            pos_x = int(pos[0] / TILE_SIZE)
            pos_y = int(pos[1] / TILE_SIZE)
            print("({}, {}): {}".format(pos_x, pos_y, worldmap.get_type(pos_x, pos_y)))

    for x in range(worldmap.width):
        for y in range(worldmap.height):
            # Draw the actual map, tile by tile
            if worldmap.tilemap[x][y] == 0:
                pygame.draw.rect(DISPLAYSURF, GREY, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif worldmap.tilemap[x][y] == 1:
                pygame.draw.rect(DISPLAYSURF, GREEN, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif worldmap.tilemap[x][y] == 2:
                pygame.draw.rect(DISPLAYSURF, BLUE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif worldmap.tilemap[x][y] == 3:
                pygame.draw.rect(DISPLAYSURF, RED, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif worldmap.tilemap[x][y] == 4:
                pygame.draw.rect(DISPLAYSURF, BROWN, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Refresh display
    pygame.display.update()