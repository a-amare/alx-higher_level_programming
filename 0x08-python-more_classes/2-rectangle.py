#!/usr/bin/python3

""" Rectangle Class with attributes and calculator"""


class Rectangle:
    """ Rectangle with init, getter and setter, perimeter and area calculator"""

    @property
    def width(self):
        ''' width getter function '''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter function '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return self.__width

    @property
    def height(self):
        '''getter function for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter function'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        return self.__height

    def __init__(self, width=0, height=0):
        '''initializes with 0 if not supplied '''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        ''' calcuates area of rectangle width*height '''
        return self.__width * self.__height

    def perimeter(self):
        ''' calcuates area of perimeter 2(width*height) '''
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__height + self.__width)

    # just a randm comment
