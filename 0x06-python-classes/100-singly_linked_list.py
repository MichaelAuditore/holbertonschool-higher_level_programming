#!/usr/bin/python3


class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if (not isinstance(data, int)):
            raise TypeError("size must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if ((value is None) or (not isinstance(value, Node))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def __str__(self):
        pr = ""
        tmp = self.__head
        while (tmp):
            pr += str(tmp.data)
            if (tmp.next_node):
                pr += "\n"
            tmp = tmp.next_node
        return pr

    def sorted_insert(self, value):
        if not self.__head:
            self.__head = Node(value, None)
        else:
            head = self.__head
            tmp = head.next_node
            if (self.__head.data > value):
                self.__head = Node(value, self.__head)
            else:
                while (tmp):
                    if (tmp.data > value):
                        new = Node(value, None)
                        new.next_node = tmp
                        head.next_node = new
                        break
                    head = head.next_node
                    tmp = tmp.next_node
                new = Node(value, tmp)
                head.next_node = new
