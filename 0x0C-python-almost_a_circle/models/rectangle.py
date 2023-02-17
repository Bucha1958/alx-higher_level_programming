#!/usr/bin/python3
"""
class called rectangle that will inherits from Base class.
"""

from models.base import Base


class Rectangle(Base):
    """
    class created called rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instance attribute which contains parameters like
        __width -> width
        __height -> height
        __x -> x
        __y -> y
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def validator_setter(self, name, value):
        """
        This my method validates all the setters in the file
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if name == 'x' or name == 'y':
            if value < 0:
                raise ValueError(name + " must be >= 0")
        elif value <= 0:
            raise ValueError(name+" must be > 0")

    def update(self, *args, **kwargs):
        """
            public method that assigns an argument to each attribute
        """
        key = ('id', 'width', 'height', 'x', 'y')

        if (args) and len(args) != 0:
            i = 0
            for arg in args:
                self.__setattr__(key[i], arg)
                i += 1
        else:
            if (kwargs):
                for key, val in kwargs.items():
                    if hasattr(self, key):
                        setattr(self, key, val)


    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        """
        self.validator_setter("width", value)
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        self.validator_setter("height", value)
        self.__height = value

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x
        """
        self.validator_setter("x", value)
        self.__x = value

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y
        """
        self.validator_setter("y", value)
        self.__y = value

    def area(self):
        """
            Public method that returns the area value of rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
            Public method  that prints in stdout the Rectangle.
        """
        rectangle = ""
        print("\n" * self.y, end="")
        for x in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def to_dictionary(self):
        """
            Public method that returns the dictionary representation of Rectangle
        """
        dictionary = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
        return (dictionary)

    def __str__(self):
        """
            Magic method that represents the class object as a string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, 
                                                     self.width, self.height)
