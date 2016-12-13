from numpy import ndarray


class NeoSet(object):
    # Simulates a java-style ArrayList, with the intention of making a dynamically sizeable array.
    # By default, Python has no support for fixed-size arrays; I'm importing ndarray from numpy to fix that problem.
    # It's fairly inefficient for its intended purpose (to support the A* search function).
    # It would've been far wiser to implement this as some sort of a hash function,
    # but I ran out of time trying to do that.

    def __init__(self, size=100):
        self.size = size
        self.index = 0
        self.elements = self.make_array(size)

    def make_array(self, size):
        # Creates  a numpy array and initialises it to zeroes (by default, they contain junk data)
        array = ndarray((size,),object)
        for i in range(0, array.size):
            array[i] = 0
        return array

    def copy_to(self, newelements):
        # Replace the object's array with a new one, copying the old data into it. Mainly used to expand it.
        for i in range(0, self.index):
            newelements[i] = self.elements[i]

    def expand(self):
        # Doubles the array's size, by creating a new one and copying the old one's data into it.
        newelements = self.make_array(self.size * 2)
        self.copy_to(newelements)
        self.size *= 2
        self.elements = newelements

    def search(self, value):
        # Searches if something already exists within the NeoSet.
        for i in range(0, self.index):
            if self.elements[i] == value:
                return i
        return -1

    def add(self, value):
        # Adds a new element to the NeoSet.
        self.elements[self.index] = value
        self.index += 1
        if self.index == self.size:
            self.expand()

    def remove(self, value):
        # Removes a specific element from within the NeoSet and adjusts the array as needed.
        found = self.search(value)
        if found != -1:
            for i in range(found, self.index):
                self.elements[i] = self.elements[i+1]
            self.index -= 1

    def __iter__(self):
        for i in range (0, self.index):
            yield self.elements[i]

    def __str__(self):
        return str(self.elements)