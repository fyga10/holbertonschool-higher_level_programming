#!/usr/bin/python3
"""
Alocation
"""

from models.base import Base


class Rectangle(Base):
    """ class Rectangle from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init Rectangle class """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """Colo"""
        return self.__width

    @property
    def height(self):
        """Colo"""
        return self.__height

    @property
    def x(self):
        """Colo"""
        return self.__x

    @property
    def y(self):
        """Alocation"""
        return self.__y

    @width.setter
    def width(self, width):
        """Alocation"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """alocation"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """alocation"""

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Alocation"""

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
