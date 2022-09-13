#!/usr/bin/python3

"""Defines a LinkedList Node class"""


class Node:
    """Represents a LinkedList Node"""
    def __init__(self, data, next_node=None):
        """Initializes a LinkedList Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if type(data) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Represents a Singly LinkedList class"""

    def __init__(self):
        """Initializes a SinglyLinkedList class"""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts node into a LinedList in sorted order

        Args:
            value (Node): The new Node to insert
        """
        ptr = self.__head
        new_node = Node(value)
        new_node.next_node = None
        if self.__head == None:
            self.head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            while ptr.next_node and ptr.next_node.data < value:
                ptr = ptr.next_node
            if ptr.next == None:
                ptr.next = new_node
            else:
                new_node.next_node = ptr.next_node
                ptr.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
