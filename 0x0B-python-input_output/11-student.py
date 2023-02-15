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
        Instantiation initialized
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs= None):
        """
        Public method that retrieves the dictionary representation of instance student
        """
        my_dict = {}
        if isinstance(attrs, list):
            for i in attrs:
                if not isinstance(i, str):
                    my_dict = self.__dict__
                    break
                try:
                    my_dict[i] = self.__dict__
                except:
                    pass
        else:
            my_dict = self.__dict__
        return (my_dict)
    
    def reload_from_json(self, json):
        """
        Public method that replaces all attributes of the student instance
        """
        for key, val in json.items():
            self.__setattr__(key, val)
