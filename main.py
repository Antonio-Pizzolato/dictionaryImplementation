import time
import matplotlib.pyplot as plt
import collections
import numpy as np
import array as arr


class Cell(object):
    __slots__ = ("key", "value")

    def __init__(self):
        self.key = None
        self.value = None

    def __repr__(self):
        return "({0}, {1})".format(self.key, self.value)


def linearHash(x, i):
    h1 = (x - (round(x / elements_number, 0) * elements_number))
    x = (h1 + (1 * i)) - (round((h1 + (1 * i)) / elements_number, 0) * elements_number)
    return x


class HashTable(object):
    empty_cell = "empty"
    deleted_cell = "deleted"

    def __init__(self, default_size):
        self.table = []
        for i in range(default_size):
            self.table.append(Cell())

    def insert(self, v):
        i = 0
        while True:
            k = int(linearHash(v, i))
            if self.table[k] == "empty" or self.table[k] == "deleted" or ("key", None):
                self.table[k].key = k
                self.table[k].value = v
                return k
            else:
                i = i + 1
            if i >= len(self.table):
                print("Error: Hash Table Overflow")
                return

    def search(self, v):
        i = 0
        while True:
            k = linearHash(v, i)
            if self.table[k].key == k and self.table[k].value == v:
                return k
            i = i + 1
            if self.table[k].key == k and (self.table[k] == self.empty_cell or self.table[k] == self.deleted_cell):
                print('ERROR: value not found')
                return


elements_number = int(input("Enter the length of the array that will be randomly created: "))
elements = np.random.randint(0, 9999, elements_number)
print(elements)

A = HashTable(11)

elements = arr.array('i', elements)
for element in elements:
    A.insert(element)

print(A.table)
