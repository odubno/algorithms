

class Queue2Stacks:
    """
    Stack reverses the order while the Queue doesn't
    """
    def __init__(self):

        # Two Stacks
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            for i in range(len(self.instack)):
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


if __name__ == '__main__':
    q = Queue2Stacks()

    for i in xrange(5):
        q.enqueue(i)

    for i in xrange(5):
        print q.dequeue()
    pass
