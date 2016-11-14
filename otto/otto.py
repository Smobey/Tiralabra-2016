import pygame, sys
from pygame.locals import *
from Worldmap import *

RED = (128, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 128)
GREY = (212, 212, 212)

TILE_SIZE = 8
MAP_WIDTH = 128
MAP_HEIGHT = 96

worldmap = Worldmap(MAP_WIDTH, MAP_HEIGHT)
worldmap.create_forests(24)
worldmap.grow_forests(5000)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for x in range(worldmap.width):
        for y in range(worldmap.height):
            if worldmap.tilemap[x][y] == 0:
                pygame.draw.rect(DISPLAYSURF, GREY, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif worldmap.tilemap[x][y] == 1:
                pygame.draw.rect(DISPLAYSURF, GREEN, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif worldmap.tilemap[x][y] == 2:
                pygame.draw.rect(DISPLAYSURF, BLUE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.update()