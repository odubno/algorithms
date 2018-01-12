# Implement a Singly Linked List

class SingleLinkedList:

    def __init__(self, value):
        self.value = value
        self.next_node = None

class DoublyLinkedList:

    def __init__(self, value):
        self.value = value
        self.prev_node = None
        self.next_node = None

if __name__ == '__main__':
    # Singly Linked List
    a = SingleLinkedList(1)
    b = SingleLinkedList(2)
    c = SingleLinkedList(3)

    a.next_node = b
    b.next_node = c

    # Doubly Linked List
    a = SingleLinkedList(1)
    b = SingleLinkedList(2)
    c = SingleLinkedList(3)

    a.next_node = b
    b.prev_node = a
    b.next_node = c
    c.prev_node = b

    pass
