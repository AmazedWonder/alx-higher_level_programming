#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """A class that represents a node of a singly linked list.
       Defines a Node class with private instance attributes.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """Initializes a new instance of the Node class.
           Defines an __init__ method that takes,initializes
           attributes using the property setters.

        Args:
            data (int): Data to be stored in the node.
            next_node (Node, optional): Next node in linked list.
            Defaults set to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the values/data stored in the node.

        Returns:
            int: The values/data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the values/data stored in the node.

        Args:
            value (int): The new data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the linked list.

        Args:
            value (Node): The new next node in the linked list.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines a SinglyLinkedList class with a private instance
       attribute __head, which represents first node in linked list.
    """

    def __init__(self):
        """Initializes a new instance of the SinglyLinkedList class."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node into correct sorted position in list.

        Args:
            value (int): Value to be stored in the new node.
        """
        # Creates a new node with the given value
        new_node = Node(value)
        # checks if the linked list is empty
        if self.__head is None:
            #  sets the new node as the head of the linked list
            self.__head = new_node
        elif value < self.__head.data:
            #  set the head as next node of the linked list
            new_node.next_node = self.__head
            # sets new node as head of linked list
            self.__head = new_node
        else:
            # traverse the linked list until we find the
            # correct position to insert the new node
            present = self.__head
            while (present.next_node is not None and
                    present.next_node.data < value):
                present = present.next_node
            new_node.next_node = present.next_node
            present.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        present = self.__head
        result = ""
        while present is not None:
            result += str(present.data) + "\n"
            present = present.next_node
        return result
