
def reverse(head):
    """
    :param node:
    :return:
    Reverse the linked lists
    """
    current = head
    prev = None
    while True:
        # copy the current eg next node before overriding it
        next = current.nextnode
        # override the next node of current
        current.nextnode = prev
        # flip the assignment
        prev = current
        current = next
        if not current:
            break

    return prev

class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None

if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = d

    p = reverse(a)
    pass