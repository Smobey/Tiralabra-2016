import pygame, sys
from pygame.locals import *

print("moro maailma")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

TILE_SIZE = 64
MAP_WIDTH = 6
MAP_HEIGHT = 4

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for row in range(MAP_HEIGHT):
        for column in range(MAP_WIDTH):
            pygame.draw.rect(DISPLAYSURF, GREEN, (column * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.update()