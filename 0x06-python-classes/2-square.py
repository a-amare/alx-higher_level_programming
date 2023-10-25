#!/usr/bin/python3

""" Square Class with size validation """


class Square:
    """ Square class """

    def __init__(self, size=0):
        '''
        Args:
                size (int): size of square side, default set to zero
                '''
        self.__size = size
        try:
            isinstance(self.__size, int)

            if (self.__size >= 0):
                raise ValueError('size must be >= 0')
        except TypeError:
            print('size must be an integer')
        except ValueError:
            print(f'{ValueError}')
