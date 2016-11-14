from math import sqrt


class AStarGrid(object):
    def __init__(self, graph):
        self.graph = graph

    def heuristic(self, node, start, end):
        return sqrt((end.x - node.x)**2 + (end.y - node.y)**2)

    def search(self, start, end):
        openset = set()
        closedset = set()
        current = start
        openset.add(current)
        while openset:
            current = min(openset, key=lambda o: o.g + o.h)
            if current == end:
                path = []
                while current.parent:
                    path.append(current)
                    current = current.parent
                path.append(current)
                return path[::-1]
            openset.remove(current)
            closedset.add(current)
            for node in self.graph[current]:
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
    def __init__(self, x, y, worldmap):
        self.x, self.y = x, y
        self.g = 0
        self.h = 0
        self.parent = None
        self.worldmap = worldmap

    def move_cost(self, other):
        cost = 10
        diagonal = abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1
        if diagonal:
            cost += 4
        if self.worldmap.get_type(other.x, other.y) == 1:
            cost += 2000
        return cost