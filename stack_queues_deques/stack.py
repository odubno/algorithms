# Stack Attributes and Methods
# An ordered collection of items that are added to and removed from the end called the "top".
# Stacks are ordered LIFO (Last in First out).

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    print s.isEmpty()
    pass