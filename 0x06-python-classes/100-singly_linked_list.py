#!/usr/bin/python3
"""
No importation of modules
"""


class Node():
    """
    class that defines the node of singly_linked list
    """

    def __init__(self, data, next_node=None):
        """
        Instantiation with data and next_node
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Property getter
        """

        return self.__data

    @data.setter
    def data(self, value):
        """
        Property setter
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Property getter
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Property setter
        """

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value

class SinglyLinkedList():
    """
    This class defines a singly linked list
    """

    def __init__(self):
        """
        Instantiation
        """

        self.__head = None


    def sorted_insert(self, value):
        """
        Public instance method that insert a Node into its correct position
        """

        node = Node(value)
        tmp = self.__head
        #check if the head is None then insert the node to the head
        if (self.__head is None):
            self.__head = node
            return
        #check if the first node is less than the new node
        if (node.data < tmp.data):
            node.next_node = tmp
            self.__head = node
            return
        #Iterates and check if the next node is more or less than the new node
        while tmp.next_node is not None:
            if (tmp.next_node.data < node.data):
                tmp = tmp.next_node
            else:
                node.next_node = tmp.next_node
                tmp.next_node = node
                return
        tmp.next_node = node

    def __str__(self):
        tmp = self.__head
        if tmp is None:
            return ("")
        while tmp.next_node is not None:
            print(tmp.data)
            tmp = tmp.next_node
        return (str(tmp.data))
