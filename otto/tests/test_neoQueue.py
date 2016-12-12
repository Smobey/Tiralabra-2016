from unittest import TestCase
from NeoQueue import NeoQueue


class TestNeoQueue(TestCase):
    def setUp(self):
        self.queue = NeoQueue()

    def test_exists(self):
        pass

    def test_empty(self):
        if not self.queue.empty():
            self.fail("Empty queue should report as empty.")
        self.queue.put(1)
        if self.queue.empty():
            self.fail("Non-empty queue should not report as empty.")

    def test_put(self):
        self.queue.put(1)
        self.queue.put(2)
        self.queue.put(7)
        self.queue.put(15)
        self.queue.put(3)
        if len(self.queue.elements) != 5:
            self.fail("Queue did not contain as many elements as were put inside of it.")

    def test_pop(self):
        self.queue.put(1)
        self.queue.put(2)
        self.queue.put(7)
        self.queue.put(15)
        self.queue.put(3)
        if self.queue.pop() != 3:
            self.fail("Queue popped the wrong value.")
        if self.queue.pop() != 15:
            self.fail("Queue popped the wrong value.")

    def test_reverse(self):
        self.queue.put(1)
        self.queue.put(2)
        self.queue.put(7)
        self.queue.put(15)
        self.queue.put(3)
        self.queue.reverse()
        pop = self.queue.pop()
        if pop != 1:
            self.fail("Queue popped the wrong value after reversing it: " + str(pop))
        pop = self.queue.pop()
        if pop != 2:
            self.fail("Queue popped the wrong value after reversing it: " + str(pop))
