#!/usr/bin/python3
"""Define a Single Linked list"""


class Node:
    """Singly linked list Node."""
    def __init__(self, data, next_node=None):
        """Initiate a singly linked list Node.

        Args:
            data (int): Node data
            next_node (Node): next node in the list
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrive Node data."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Set data in a Node

        Args:
            value (int): Node value to be set
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrive the next node in the list."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set next node value

        Args:
            value (Node): next node pointer
        """
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        """Print list data."""
        stri = ""
        temp = self.__head
        while (temp):
            stri = stri + str(temp.data)
            if (temp.next_node):
                stri = stri + "\n"
            temp = temp.next_node
        return stri

    def sorted_insert(self, value):
        """Sort and insert data to list.

        Args:
            value (int): data to be inserted
        """
        if not self.__head:
            self.__head = Node(value, None)
        else:
            aux1 = self.__head
            aux2 = aux1.next_node
            if (self.__head.data > value):
                self.__head = Node(value, self.__head)
            else:
                while (aux2):
                    if (aux2.data > value):
                        new = Node(value, None)
                        new.next_node = aux2
                        aux1.next_node = new
                        break
                    aux1 = aux1.next_node
                    aux2 = aux2.next_node
                new = Node(value, aux2)
                aux1.next_node = new
