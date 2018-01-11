
def cycle_check(node):
    # Take in a node and based on the nextnode return a Boolean if the linked list
    # contains a cycle, eg nodes next point points back to the previous node
    node_val = node.value
    v = None
    while node_val != v:
        v = node.nextnode
        if not v:
            return False
        v = v.value
        node = node.nextnode
    return True


def cycle_check2(node):
    # Begin both markers at the first node
    marker1 = node
    marker2 = node

    # Go until end of list
    while marker2 != None and marker2.nextnode != None:

        # Note
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        # Check if the markers have matched
        if marker2 == marker1:
            return True

    # Case where marker ahead reaches the end of the list
    return False


class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None

if __name__ == '__main__':
    # Cycle List
    a = Node(1)
    b = Node(2)
    c = Node(3)
    # Link
    a.nextnode = b
    b.nextnode = c
    c.nextnode = a
    # None Cycle List
    x = Node(1)
    y = Node(2)
    z = Node(3)
    # Link
    x.nextnode = y
    y.nextnode = z

    print 'pass'
    pass
    # %timeit cycle_check(a)
    # %timeit cycle_check2(a)
    pass