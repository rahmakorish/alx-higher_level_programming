#!/usr/bin/python3
"""python file"""


class Node:
    """class node"""
    def __init__(self, data, next_node=None):
        """constructor.
        Args:
        data:node data
        next_node:following node pointer
        """
        self.__data = data
        self.__next_node = next_node
        @property
        def data(self):
            return (self.__data)
        @data.setter
        def data(self, value):
            self.__data = value
            if not type(value) is int:
                raise TypeError("data must be an integer")
        @propert
        def next_node(self):
            return (self.__next_node)
        @next_node.setter
        def next_node(self, value):
            self.__next_node = value
            """if not type(value) is Node():
                raise TypeError("next_node must be a Node object")"""
class SinglyLinkedList:
    """SinglyLinkedList class"""
    def __init___(self):
        self.__head = Node()
    def sorted_insert(self, value):
        self.Node = value
