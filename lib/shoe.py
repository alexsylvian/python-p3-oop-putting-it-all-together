#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size
        self._condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    @property
    def condition(self):
        return self._condition

    def repair(self):
        print("The shoe has been repaired.")
        self._condition = "Repaired"

    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"

