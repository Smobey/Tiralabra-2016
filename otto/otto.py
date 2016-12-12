import pygame, sys
from pygame.locals import *
from worldmap import *

RED = (128, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 128)
GREY = (212, 212, 212)
BROWN = (220, 110, 110)

TILE_SIZE = 8
MAP_WIDTH = 48
MAP_HEIGHT = 48

worldmap = Worldmap(MAP_WIDTH, MAP_HEIGHT)
worldmap.debug_creation()
#worldmap.create_forests(24) # 24 forest tiles
#worldmap.grow_forests(8000) # "Organically" grow the 24 forest tiles into ~5000 ones.
#worldmap.create_cities(12) # Randomly scatter 12 cities around.

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))

while True:
    # Main loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            # Hit space to draw a road between two randomly chosen cities (using A* to determine path)
            worldmap.draw_roads()


    for x in range(worldmap.width):
        for y in range(worldmap.height):
            # Kind of a lazy way to do it for now
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