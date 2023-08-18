#!/usr/bin/python3
"""Defines two classes for a singly-linked list:
   Node and SinglyLinkedList.

The Node class represents a node in the linked list. Each
node has a data attribute to store the data and a next_node
attribute to reference the next node in the list. The data
attribute can be accessed and modified using the @property decorator,
which provides getter and setter methods. Similarly,
the next_node attribute can be accessed and modified using
the @property decorator.

The SinglyLinkedList class represents the singly-linked list itself.
It has a private attribute __head that points to the first node in
the list. The __init__ method initializes a new linked list with an
empty head. The sorted_insert method is used to insert a new node into
the list at the correct ordered numerical position. If the list is
empty, the new node becomes the head. If the value of the new node
is less than the current head, the new node becomes the new head.
Otherwise, the method iterates through the list until finding the
correct position to insert the new node. The __str__ method defines
the string representation of the linked list, which concatenates the
string representation of each node's data with a newline character.

The code provides a basic implementation of a singly-linked list
with support for sorted insertions. It allows you to create a
linked list, insert nodes in sorted order, and print the contents
of the list.

"""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
