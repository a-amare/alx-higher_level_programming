#!/usr/bin/python3

""" Rectangle Class with dimensions """


class Rectangle:
    """ Rectangle dimensions length and width """

    def __init__(self, width=0, length=0):
        """ instatiates length and width with zero """
        self._width = width
        self._length = length

    def width(self):
        """ gets width variable"""
        print(self._width)

    def length(self):
        """gets length of rectangle variable """
        print(self._length)

    def height(self, value):
        """ sets height value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def width(self, value):
        """ sets width value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self._height = value
