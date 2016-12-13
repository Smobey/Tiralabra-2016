from math import sqrt
from NeoSet import NeoSet
from NeoQueue import NeoQueue


class AStarGrid(object):
    def heuristic(self, node, start, end):
        # Basic heuristic for determining approx. distance between start and end nodes.
        return sqrt((end.x - node.x)**2 + (end.y - node.y)**2)

    def grid_min_set(self, set):
        # Returns the "smallest" node from amongst a NeoSet of AStarGridNodes (defined by g + h)
        smallest = set.elements[0]
        for i in range(1, set.index):
            if set.elements[i].g + set.elements[i].h < smallest.g + smallest.h:
                smallest = set.elements[i]
        return smallest

    def search(self, start, end):
        # The main search function. It takes the start and the end node and tries to find a path between them.
        # The function uses the (highly inefficient) NeoSet and NeoQueue data structures for this purpose.
        openset = NeoSet()
        closedset = NeoSet()
        current = start
        openset.add(current)
        while openset:
            current = self.grid_min_set(openset)
            if current == end:
                path = NeoQueue()
                while current.parent:
                    path.put(current)
                    current = current.parent
                path.put(current)
                path.reverse()
                return path
            openset.remove(current)
            closedset.add(current)

            for node in current.neighbours:
                if closedset.search(node) != -1:
                    continue
                if openset.search(node) != -1:
                    new_g = current.g + current.move_cost(node)
                    if node.g > new_g:
                        node.g = new_g
                        node.parent = current
                else:
                    node.g = current.g + current.move_cost(node)
                    node.h = self.heuristic(node, start, end)
                    node.parent = current
                    openset.add(node)
        return None

    def search2(self, start, end):
        # Search function using python's prebuilt set() class.
        # Unused, only for comparison.
        openset = set()
        closedset = set()
        current = start
        openset.add(current)
        while openset:
            current = min(openset, key=lambda o:o.g + o.h)
            if current == end:
                path = []
                while current.parent:
                    path.append(current)
                    current = current.parent
                path.append(current)
                return path[::-1]
            openset.remove(current)
            closedset.add(current)
            for node in current.neighbours:
                if node in closedset:
                    continue
                if node in openset:
                    new_g = current.g + current.move_cost(node)
                    if node.g > new_g:
                        node.g = new_g
                        node.parent = current
                else:
                    node.g = current.g + current.move_cost(node)
                    node.h = self.heuristic(node, start, end)
                    node.parent = current
                    openset.add(node)
        return None


class AStarGridNode(object):
    # Node object for A* search. One node is an equivalent to a single (x, y) coord in the worldmap.
    # The worldmap itself needs to be passed to the node so it can access it to calculate the movement costs
    # to neighbouring tiles.

    def __init__(self, x, y, worldmap):
        self.x = x
        self.y = y
        self.g = 0 # Current cost
        self.h = 0 # Current guess (heurestic)
        self.parent = None
        self.worldmap = worldmap
        self.neighbours = NeoSet(10)

    def move_cost(self, other):
        # Base movement cost for calculation is 10, with 4 added for diagonal movement (approx of sqrt(2))
        # Movement cost is increased by 2000 for forest tiles, 4100 for water tiles.
        cost = 10
        diagonal = abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1
        if diagonal:
            cost += 4
        if self.worldmap.get_type(other.x, other.y) == 1: # Forest
            cost += 2000
        return cost

    def __str__(self):
        return "AStarGridNode at " + str(self.x) + ", " + str(self.y)