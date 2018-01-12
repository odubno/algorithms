
# Super fast 208 nano seconds
def nth_to_last_node(n, head):
    """
    :param n:
    :param head:
    :return:
    1. Starting count at 1 because the while loop already begins with the 2nd node.
    2. Subtracting 1 from n, because the index in Python starts at 0.
    3. At each loop increment the 'current' node until the nth node
    4. Once the loop reaches the nth node, begin incrementing the head.
       As we loop, the difference between 'current' and 'head' is exactly n nodes.
       Once 'current' runs out of nextnodes, we found our desired nth to last node
    5. return the 'head'
    """
    current = head
    count = 1  # 1
    while current.nextnode:
        current = current.nextnode  # 3
        if count > n-1:  # 4
            head = head.nextnode  # 4
        count += 1  # 4
    return head  # 5


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


def nth_to_last_node2(n, head):
    current = reverse(head)
    for i in range(n-1):
        current = current.nextnode
    return current

def nth_to_last_node3(n, head):
    current = head
    for i in xrange(n-1):
        # this for loop increments the right_pointer to the nth node
        current = current.nextnode

    while current.nextnode:
        # this while loop picks up where the for loop left off, eg on the nth node
        # during the while loop we're incrementing the actual head until the right_pointer runs out of nodes
        # once the right_pointer is out of nodes our head will have the desired nth node
        head = head.nextnode
        current = current.nextnode

    return head


def nth_to_last_node4(n, head):
    left_pointer = head
    right_pointer = head

    # Set right pointer at n nodes away from head
    for i in xrange(n - 1):

        # Check for edge case of not having enough nodes!
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list.')

        # Otherwise, we can set the block
        right_pointer = right_pointer.nextnode

    # Move the block down the linked list
    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    # Now return left pointer, its at the nth to last element!
    return left_pointer


class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None

if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    d.nextnode = e

    nth_to_last_node(4, a)
    print 'test'
    # %timeit nth_to_last_node(4, a)
    # %timeit nth_to_last_node2(4, a)
    # %timeit nth_to_last_node3(4, a)
    # %timeit nth_to_last_node4(4, a)