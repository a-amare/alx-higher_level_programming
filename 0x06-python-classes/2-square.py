#!/usr/bin/python3

""" Square Class with size validation """


class Square:
    """ Square class """

    def __init__(self, size=0):
        '''
        Args:
                size (int): size of square side, default set to zero
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
