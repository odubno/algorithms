# Implement a Deque

class Deque:
    """
    Both LIFO and FIFO
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        # check if it's empty
        return self.items == []

    def add_front(self, item):
        # add to the front
        self.items.append(item)

    def add_rear(self, item):
        # add to the rear
        self.items.insert(0, item)

    def rm_front(self):
        # remove from the front
        return self.items.pop()

    def rm_rear(self):
        # remove from the rear
        return self.items.pop(0)

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    d = Deque()