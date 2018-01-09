# Implement a Stack

class Stack:
    """
    FIFO - First in First out
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        # check if it's empty
        return self.items == []

    def add_item(self, item):
        # push a new item
        self.items.append(item)

    def pop_item(self):
        # pop an item
        return self.items.pop()

    def peek(self):
        # peek at the top item
        return self.items[len(self.items) - 1]

    def size(self):
        # return the size
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
