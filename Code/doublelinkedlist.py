from linkedlist import Node, LinkedList

class Node_2(Node):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList(LinkedList):
    def __init__(self, items=None):
        pass