#!/usr/bin/python3
"""This is the Rectangle module"""


class Rectangle:
    """Rectangle class that has private width and hight attributes"""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError('width must be an integer')
        if val < 0:
            raise ValueError('width must be >= 0')
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError('height must be an integer')
        if val < 0:
            raise ValueError('height must be >= 0')
        self.__height = val

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")
        else:
            for i in range(self.__height):
                return ("#" * self.__width + "\n" + "#" * self.__width +
                        "\n" + "#" * self.__width + "\n" + "#" * self.__width)
