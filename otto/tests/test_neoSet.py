from unittest import TestCase
from NeoSet import NeoSet


class TestNeoSet(TestCase):
    def setUp(self):
        self.set = NeoSet()

    def test_make_array(self):
        array = self.set.make_array(10)
        if len(array) != 10:
            self.fail("Wrong size array.")

    def test_copy_to(self):
        self.set.add(1)
        newelements = self.set.make_array(20)
        if self.set.search(1) == -1:
            self.fail("Didn't find old value in newly copied array.")

    def test_expand(self):
        self.set.expand()
        self.set.expand()
        if len(self.set.elements) != self.set.elements.size:
            self.fail("True length of array does not match the reported size of set.")

    def test_search(self):
        self.set.add(1)
        self.set.add(2)
        self.set.add(15)
        if self.set.search(2) == -1:
            self.fail("Didn't find added element.")

    def test_add(self):
        self.set.add(1)
        self.set.add(2)
        self.set.add(15)
        if self.set.index != 3:
            self.fail("Reported index wrong.")

    def test_remove(self):
        self.set.add(1)
        self.set.add(2)
        self.set.add(15)
        self.set.remove(2)
        if self.set.search(2) != -1:
            self.fail("Found an element that was supposed to have been removed.")
        if self.set.index != 2:
            self.fail("Reported index wrong.")
