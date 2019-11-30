from tweet_generator_tutorial.linkedlist import Node, LinkedList

class DoubleLinkedNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None

class DoubleLinkedList(LinkedList):
    def __init__(self, items=None):
        super().__init__(items)

    def append(self, data):
        if self.head == None:
            self.head = DoubleLinkedNode(data)
            self.tail = self.head
        else:
            current = self.head
            while current is not None:
                prev = current
                current = current.next
            current = DoubleLinkedNode(data)
            prev.next = current
            current.prev = prev
            self.tail = current
        self.count += 1
    
    def prepend(self, data):
        if self.head == None:
            self.head = DoubleLinkedNode(data)
        else:
            current = self.head
            self.head = DoubleLinkedNode(data)
            self.head.next = current
            current.prev = self.head
        self.count += 1
    
    def traverse_forwards(self):
        self.items()
    
    def traverse_backwards(self):
        items = []
        current = self.tail
        while current is not None:
            items.append(current.data)
            current = current.prev
        return items

if __name__ == "__main__":
    ht = DoubleLinkedList([4, 7, 2, 8])
    print(ht.items())