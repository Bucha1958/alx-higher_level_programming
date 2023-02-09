#!/usr/bin/python3
"""
No importation of module
"""


class Rectangle():
    """
    Class rectangle
    """


    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialization
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        public instance method that returns the area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        public instance method that returns the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return "0"
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        str should print the rectangle with the character #
        """
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle
        for h in range(self.height):
            for w in range(self.width):
                print(self.print_symbol, end="")
            if h != self.height - 1:
                print()
        return rectangle

    def __repr__(self):
        """
        It returns the string representation of the object
        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """
        It deletes the object instance
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() == rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new rectangle instance
        """
        return cls(size, size)
