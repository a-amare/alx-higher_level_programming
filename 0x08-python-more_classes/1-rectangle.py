#!/usr/bin/python3

""" Rectangle Class with attributes"""


class Rectangle:
    """ Rectangle with init """

    @property
    def width(self):
        ''' width getter function '''
        return (self.__height)

    @width.setter
    def width(self, value):
        '''width setter function '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return (self.__width)

    @property
    def height(self):
        '''getter function for height'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''height setter function'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        return (self.__height)

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
