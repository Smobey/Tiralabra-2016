import random


class Worldmap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tilemap = [[0 for x in range(height)] for y in range(width)]

        self.forest_tiles = []

    def exists(self, x, y):  # Check if tile exists
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return True

    def return_type(self, x, y):  # Give tile type of (X, Y)
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
        if self.exists(x - 1, y) and self.return_type(x - 1, y) == type:
            adjucent.append((x - 1, y))
        if self.exists(x + 1, y) and self.return_type(x + 1, y) == type:
            adjucent.append((x + 1, y))
        if self.exists(x, y - 1) and self.return_type(x, y - 1) == type:
            adjucent.append((x, y - 1))
        if self.exists(x, y + 1) and self.return_type(x, y + 1) == type:
            adjucent.append((x, y + 1))
        return adjucent

    def create_forests(self, amount):  # Create X amount of random forest tiles
        for i in range(0, amount):
            tile = (random.randint(5, self.width - 6), random.randint(5, self.height - 6))
            print("FOREST: " + str(tile))
            self.forest_tiles.append(tile)
            self.tilemap[tile[0]][tile[1]] = 2

    def grow_forests(self, size):
        loops = 0
        for i in range(0, size):
            loops += 1
            tile = random.choice(self.forest_tiles)
            print("selected: " + str(tile))
            print("forest tiles: " + str(self.forest_tiles))

            adjucent = self.get_adjucent_by_type(0, *tile)
            print("adjucent: " + str(adjucent))
            if len(adjucent) == 0:  # Something has gone wrong.
                print("AAAAAAAA")
            else:
                newtile = random.choice(adjucent)
                print("created: " + str(newtile) + " (type " + str(self.return_type(*newtile)) + ")")

                self.tilemap[newtile[0]][newtile[1]] = 1

                print("get_adjucent_by_type: " + str(self.get_adjucent_by_type(0, *tile)))

                if len(self.get_adjucent_by_type(0, *tile)) == 0:
                    self.forest_tiles.remove(tile)
                    print("removed old: " + str(tile))
                if not self.get_adjucent_by_type(0, *newtile) == 0:
                    self.forest_tiles.append(newtile)
                    print("appended new: " + str(newtile))

                print("tile " + str(newtile) + " type = " + str(self.return_type(*newtile)))
                print("-----")

        print("loops: " + str(loops))

        count = 0
        forest_count = 0
        for x in range(self.width):  # Cleanup: No non-forest tiles in the middle of forests.
            for y in range(self.height):
                count += 1
                if self.return_type(x, y) == 1:
                    forest_count += 1
        print(count)
        print(forest_count)