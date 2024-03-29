#!/usr/bin/python3
"""
No importation of module
"""


class Student():
    """
    Student class created
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs= None):
        """
        public method that retrieves the dictionary representation of the student instance
        """
        my_dict = {}
        if type(attrs) == list:
            for i in attrs:
                if type(i) != str:
                    my_dict = self.__dict__
                    break
                try:
                    my_dict[i] = getattr(self, i)
                except:
                    pass
        else:
            my_dict = self.__dict__
        return (my_dict)
