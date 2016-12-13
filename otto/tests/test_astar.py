from unittest import TestCase
from Worldmap import *

class TestAStarGrid(TestCase):
    def setUp(self):
        self.worldmap = Worldmap(7, 7)
        self.worldmap.forest_tiles.append((2, 2))
        self.worldmap.tilemap[2][2] = 1
        self.worldmap.forest_tiles.append((3, 3))
        self.worldmap.tilemap[3][3] = 1
        self.worldmap.forest_tiles.append((4, 4))
        self.worldmap.tilemap[4][4] = 1
        self.worldmap.cities.append((3, 4))
        self.worldmap.tilemap[3][4] = 3
        self.worldmap.cities.append((3, 2))
        self.worldmap.tilemap[3][2] = 3

    def test_search(self):
        start, end = self.worldmap.nodes[3][2], self.worldmap.nodes[3][4]
        path = self.worldmap.paths.search(start, end)
        if path is None:
            self.fail("Failed to find path.")
        if len(path.elements) != 3:
            self.fail("Path is wrong length.")