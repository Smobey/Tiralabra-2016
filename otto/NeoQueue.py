import collections


class NeoQueue:
    # Just an interface for python's default queue functions.
    # Simulates a traditional one-directional queue that only supports putting and popping in one direction.
    # Fairly efficient, though has some unnecessary overhead over just using deque by itself.
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        # Simply tells you if the queue is empty.
        return len(self.elements) == 0
    
    def put(self, x):
        # Puts an element to the right of the queue.
        self.elements.append(x)
    
    def pop(self):
        # Pops an element from the right of the queue.
        return self.elements.pop()

    def reverse(self):
        # Reverses the queue.
        newelements = collections.deque()
        while not self.empty():
            newelements.append(self.elements.pop())
        self.elements = newelements

    def __iter__(self):
        for e in self.elements:
            yield e