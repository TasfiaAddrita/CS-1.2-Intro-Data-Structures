from linkedlist import LinkedList

class Queue(LinkedList):
    def __init__(self, items=None):
        super().__init__(items)
    
    def enque(self, data):
        self.append(data)

    def deque(self):
        if self.count == 0:
            self.delete()
        else: 
            self.delete(self.head.data)

if __name__ == "__main__":
    q = Queue(['A', 'B', 'C'])
    print(q)
    q.enque('D')
    print(q)
    q.deque()
    print(q)