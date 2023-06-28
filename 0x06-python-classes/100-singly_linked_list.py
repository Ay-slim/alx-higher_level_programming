#!/usr/bin/python3
"""Set up node class"""


class Node:
    """Template for a singly linked list node"""

    def __init__(self, data, next_node=None):
        """Initializer for node object
        Args:
            data: Data node contains
            next_node: The next node
        """
        self.data = data
        self.next_node = next_node

    def data(self):
        return self.__data

    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    def next_node(self):
        return self.__next_node

    def next_node(self, value):
        is_none = value is None
        is_node = isinstance(value, Node)
        if is_none or is_node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Template for a singly linked list"""

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            is_node = current.next_node is not None
            data_less_val = current.next_node.data < value
            while is_node and data_less_val:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
