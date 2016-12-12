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

        graph, self.nodes = self.make_graph(self.width, self.height)
        self.paths = AStarGrid(graph)

    def debug_creation(self):
        # Just a testing function. For testing. Manually.
        self.forest_tiles.append((24, 24))
        self.tilemap[24][24] = 1
        self.grow_forests(600)
        self.cities.append((8, 24))
        self.tilemap[8][24] = 3
        self.cities.append((40, 24))
        self.tilemap[40][24] = 3

    def exists(self, x, y):
    # Check if tile exists
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return True

    def get_type(self, x, y):
    # Give tile type of (X, Y)
        return self.tilemap[x][y]

    def get_adjucent(self, x, y):
    # Return all tiles adjucent to (x, y)
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

    def get_adjucent_by_type(self, type, x, y):
    # Return all tiles of type T adjucent to (x, y)
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

    def create_cities(self, amount):
    # Randomly create X amount of city tiles
        for i in range(0, amount):
            plains = []
            for x in range(5, self.width - 6):  # Pick non-forest/mountain/etc tiles for city locations
                for y in range(5, self.height - 6):
                    if self.get_type(x, y) == 0:
                        plains.append((x, y))
            tile = random.choice(plains)
            self.cities.append(tile)
            self.tilemap[tile[0]][tile[1]] = 3

    def create_forests(self, amount):
    # Randomly create X amount of forest tiles (for future growing)
        for i in range(0, amount):
            tile = (random.randint(5, self.width - 6), random.randint(5, self.height - 6))
            self.forest_tiles.append(tile)
            self.tilemap[tile[0]][tile[1]] = 1

    def grow_forests(self, size):
        # SLOW way of growing forests, but results in natural look.
        for i in range(0, size):
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

    def make_graph(self, width, height):
        # Makes a graph of nodes from all the tiles on the map (for A* search purposes)
        nodes = [[AStarGridNode(x, y, self) for y in range(height)] for x in range(width)]
        graph = {}
        for x in range(width):
            for y in range(height):
                node = nodes[x][y]
                graph[node] = []
                for i, j in product([-1, 0, 1], [-1, 0, 1]):
                    # Make every node in the graph adjucent to the ones next to it (incl. diagonally)
                    if not (0 <= x + i < width):
                        continue
                    if not (0 <= y + j < height):
                        continue
                    graph[nodes[x][y]].append(nodes[x + i][y + j])
        return graph, nodes

    def draw_roads(self):
        # Simply draws a road between two random cities on the map.
        for i in range (0, 1):
            paired_cities = random.sample(self.cities, 2)
            print("cities: ", paired_cities)
            start, end = self.nodes[paired_cities[0][0]][paired_cities[0][1]], self.nodes[paired_cities[1][0]][paired_cities[1][1]]
            path = self.paths.search(start, end)
            if path is None:
                print("No path found")
            else:
                for node in path:
                    if self.tilemap[node.x][node.y] is not 3:
                        self.tilemap[node.x][node.y] = 4
                print("Path found:", path)