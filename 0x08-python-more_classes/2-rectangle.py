#!/usr/bin/python3
'''Classes and objects project'''


class Rectangle:
    '''class Rectangle'''

    def __init__(self, width=0, height=0):
        '''Initializes the instance'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Property to asign value to width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Property to asign value to height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''calculates rectangle's area'''
        return self.__width * self.__height

    def perimeter(self):
        '''calculates rectangle's perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
