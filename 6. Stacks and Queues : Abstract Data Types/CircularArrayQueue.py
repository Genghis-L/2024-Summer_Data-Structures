class CircularArrayQueue():

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    # Returns the number of elements stored in the queue.
    def __len__(self):
        return self.size

    #Returns True if the queue is empty, False otherwise.
    def is_empty(self):
        #TODO
        pass

    #Returns True if the queue is full, False otherwise.
    def is_full(self):
        #TODO
        pass

    # Inserts a new element at the tail of the queue.
    # Displays error notification if the queue is already at full capacity.
    def enqueue(self, element):
        #TODO
        pass

    # Removes the head element from the queue.
    # Displays error notification if the queue is empty.
    def dequeue(self):
        #TODO
        pass
    
    # Returns the value of the head element in the queue.
    # Returns None if the queue is empty.
    # Does not remove the head from the queue.
    def peek(self):
        #TODO
        pass


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
    while (not myqueue.is_full()):
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
    while (not myqueue.is_full()):
        myqueue.enqueue(random.randint(0, 20))
    print(myqueue)
    print(">> Empty queue")
    while (not myqueue.is_empty()):
        print(myqueue.dequeue())
    print(myqueue)

    
testQueue()
