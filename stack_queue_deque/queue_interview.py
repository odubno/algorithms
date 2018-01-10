# Implement a Queue

class Queue:
    """
    LIFO - Last in First out
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        # check if the Queue is empty
        return self.items == []

    def enqueue(self, item):
        # items are added at one end; in this case in the beginning
        self.items.insert(0, item)

    def dequeue(self):
        # items are removed from the other end; in this case from the end
        return self.items.pop()

    def size(self):
        # return the size of the Queue
        return len(self.items)

if __name__ == '__main__':
    q = Queue()