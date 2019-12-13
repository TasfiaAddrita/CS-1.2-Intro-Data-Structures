# from linkedlist import Node, LinkedList
from queue import Queue

class CircularBuffer(Queue):
    def __init__(self, n=1, items=None):
        if items is None:
            items = [None for _ in range(n)]
        super().__init__(items)
        self.length = n
        self.tail.next = self.head

