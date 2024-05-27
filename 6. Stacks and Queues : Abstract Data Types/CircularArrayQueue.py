class CircularArrayQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    # Returns the number of elements stored in the queue.
    def __len__(self):
        return self.size

    # Returns True if the queue is empty, False otherwise.
    def is_empty(self):
        # TODO
        return self.size == 0

    # Returns True if the queue is full, False otherwise.
    def is_full(self):
        # TODO
        return self.size == self.capacity

    # Inserts a new element at the tail of the queue.
    # Displays error notification if the queue is already at full capacity.
    # Returns the removed tail value; None when error occurs. 
    def enqueue(self, element):
        # TODO
        if self.is_full():
            print("The max capacity has been reached. ")
            return None
        else:
            pre_tail = self.array[self.tail]
            self.array[self.tail] = element
            self.tail = (self.tail+1) % self.capacity
            self.size += 1
        return pre_tail

    # Removes the head element from the queue.
    # Displays error notification if the queue is empty.
    # Returns the removed head value; None when error occurs. 
    def dequeue(self):
        # TODO
        if self.is_empty():
            print("The queue is empty. ")
            return None
        else:
            pre_head = self.array[self.head]
            self.array[self.head] = None
            self.head = (self.head+1) % self.capacity
            self.size -= 1
        return pre_head

    # Returns the value of the head element in the queue.
    # Returns None if the queue is empty.
    # Does not remove the head from the queue.
    def peek(self):
        # TODO
        if self.is_empty():
            return None
        else:
            return self.array[self.head]

    def __str__(self):
        s = str(self.size) + " values\n[ "
        i = self.head
        for j in range(self.size):
            s += str(self.array[i]) + " "
            i = (i + 1) % self.capacity
        s += "]"
        return s


def testQueue():
    import random

    print("------------------------------")
    print("         TEST - QUEUE")
    print("------------------------------")
    myqueue = CircularArrayQueue(8)
    print(">> Show empty queue")
    print(myqueue)
    print(">> Enqueue one element")
    myqueue.enqueue(8)
    print(myqueue)
    print(">> Fill up queue")
    while not myqueue.is_full():
        myqueue.enqueue(random.randint(0, 20))
    print(myqueue)
    print(">> Illegal enqueue twice")
    myqueue.enqueue(8)
    myqueue.enqueue(5)
    print(myqueue)
    print(">> Peek in queue")
    print(myqueue.peek())
    print(">> Dequeue three elements")
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue)
    print(">> Fill up queue again")
    while not myqueue.is_full():
        myqueue.enqueue(random.randint(0, 20))
    print(myqueue)
    print(">> Empty queue")
    while not myqueue.is_empty():
        print(myqueue.dequeue())
    print(myqueue)


testQueue()
