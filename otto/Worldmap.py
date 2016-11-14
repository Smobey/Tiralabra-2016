import random
from astar import *
from itertools import product

class Worldmap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tilemap = [[0 for x in range(height)] for y in range(width)]

        self.forest_tiles = []
        self.cities = []

    def debug_creation(self):
        self.forest_tiles.append((64, 48))
        self.tilemap[64][48] = 1
        self.grow_forests(12000)
        self.cities.append((16, 48))
        self.tilemap[16][48] = 3
        self.cities.append((112, 48))
        self.tilemap[112][48] = 3
        self.draw_roads()

    def exists(self, x, y):  # Check if tile exists
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return True

    def get_type(self, x, y):  # Give tile type of (X, Y)
        return self.tilemap[x][y]

    def get_adjucent(self, x, y):  # Return all tiles adjucent to (x, y)
        adjucent = []
        if self.exists(x - 1, y):
            adjucent.append((x - 1, y))
        if self.exists(x + 1, y):
            adjucent.append((x + 1, y))
        if self.exists(x, y - 1):
            adjucent.append((x, y - 1))
        if self.exists(x, y + 1):
            adjucent.append((x, y + 1))
        return adjucent

    def get_adjucent_by_type(self, type, x, y):  # Return all tiles of type T adjucent to (x, y)
        adjucent = []
        if self.exists(x - 1, y) and self.get_type(x - 1, y) == type:
            adjucent.append((x - 1, y))
        if self.exists(x + 1, y) and self.get_type(x + 1, y) == type:
            adjucent.append((x + 1, y))
        if self.exists(x, y - 1) and self.get_type(x, y - 1) == type:
            adjucent.append((x, y - 1))
        if self.exists(x, y + 1) and self.get_type(x, y + 1) == type:
            adjucent.append((x, y + 1))
        return adjucent

    def create_cities(self, amount):  # Randomly create X amount of city tiles
        for i in range(0, amount):
            plains = []
            for x in range(5, self.width - 6):  # Pick non-forest/mountain/etc tiles for city locations
                for y in range(5, self.height - 6):
                    if self.get_type(x, y) == 0:
                        plains.append((x, y))
            tile = random.choice(plains)
            self.cities.append(tile)
            self.tilemap[tile[0]][tile[1]] = 3

    def create_forests(self, type, amount):  # Randomly create X amount of forest tiles
        for i in range(0, amount):
            tile = (random.randint(5, self.width - 6), random.randint(5, self.height - 6))
            self.forest_tiles.append(tile)
            self.tilemap[tile[0]][tile[1]] = 1

    def grow_forests(self, size):
        loops = 0
        for i in range(0, size):
            loops += 1
            tile = random.choice(self.forest_tiles)

            adjucent = self.get_adjucent_by_type(0, *tile)
            if len(adjucent) == 0:  # Something has gone wrong.
                pass
            else:
                newtile = random.choice(adjucent)
                self.tilemap[newtile[0]][newtile[1]] = 1

                if len(self.get_adjucent_by_type(0, *tile)) == 0:
                    self.forest_tiles.remove(tile)
                if not self.get_adjucent_by_type(0, *newtile) == 0:
                    self.forest_tiles.append(newtile)

    def make_graph(self, width, height): # Temporary, probably
        nodes = [[AStarGridNode(x, y, self) for y in range(height)] for x in range(width)]
        graph = {}
        for x, y in product(range(width), range(height)):
            node = nodes[x][y]
            graph[node] = []
            for i, j in product([-1, 0, 1], [-1, 0, 1]):
                if not (0 <= x + i < width):
                    continue
                if not (0 <= y + j < height):
                    continue
                graph[nodes[x][y]].append(nodes[x + i][y + j])
        return graph, nodes

    def draw_roads(self):
        graph, nodes = self.make_graph(self.width, self.height)
        paths = AStarGrid(graph)

        for i in range (0, 1):
            paired_cities = random.sample(self.cities, 2)
            print("cities: ", paired_cities)
            start, end = nodes[paired_cities[0][0]][paired_cities[0][1]], nodes[paired_cities[1][0]][paired_cities[1][1]]
            path = paths.search(start, end)
            if path is None:
                print("No path found")
            else:
                for node in path:
                    if self.tilemap[node.x][node.y] is not 3:
                        self.tilemap[node.x][node.y] = 4
                print("Path found:", path)