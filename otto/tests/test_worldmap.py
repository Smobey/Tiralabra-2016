from unittest import TestCase
from worldmap import Worldmap


class TestWorldmap(TestCase):
    def setUp(self):
        self.worldmap = Worldmap(32, 32)

    def test_exists(self):
        pass

    def test_get_type(self):
        self.worldmap.tilemap[1][1] = 1
        self.assertEqual(1, self.worldmap.get_type(1, 1))

    def test_get_adjucent(self):
        adjucent = self.worldmap.get_adjucent(1, 1)
        if (0, 1) not in adjucent:
            self.fail("Didn't find coords 0,1")

        if (2, 1) not in adjucent:
            self.fail("Didn't find coords 2,1")

        if (1, 0) not in adjucent:
            self.fail("Didn't find coords 1,0")

        if (1, 2) not in adjucent:
            self.fail("Didn't find coords 1,2")

        self.assertEqual(4, len(adjucent))

    def test_get_adjucent_by_type(self):
        self.worldmap.tilemap[1][0] = 1
        self.worldmap.tilemap[2][1] = 1
        self.worldmap.tilemap[0][0] = 1

        adjucent = self.worldmap.get_adjucent_by_type(1, 1, 1)

        if (1, 0) not in adjucent:
            self.fail("Didn't find coords 1,2")

        if (2, 1) not in adjucent:
            self.fail("Didn't find coords 2,1")

        self.assertEqual(2, len(adjucent))

    def test_create_cities(self):
        self.worldmap.create_cities(6)
        city_counter = 0
        for x in range(self.worldmap.width):
            for y in range(self.worldmap.height):
                if self.worldmap.tilemap[x][y] == 3:
                    city_counter += 1
        self.assertEqual(6, city_counter)

    def test_create_forests(self):
        self.worldmap.create_forests(12)
        forest_counter = 0
        for x in range(self.worldmap.width):
            for y in range(self.worldmap.height):
                if self.worldmap.tilemap[x][y] == 1:
                    forest_counter += 1
        self.assertEqual(12, forest_counter)