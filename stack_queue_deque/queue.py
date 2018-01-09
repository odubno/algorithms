# An ordered collection of items.
# New items are added at one end -> the "rear"
# Items are removed from the other end -> the "front"
# FiFo, first-in first-out or "first-come first served"
# The item that has been in the queue the longest is in the front

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


if __name__ == '__main__':
    s = Queue()
    pass