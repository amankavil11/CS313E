import time
#PushTime: 9.5367431640625e-07
#PopTime: 8.106231689453125e-06
#PeekTime: 4.0531158447265625e-06

class Queue(object):
    '''Queue implements the FIFO principle.'''

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if (not self.isEmpty()):
            return self.queue.pop(0)
        else:
            return None

    def isEmpty(self):
        return (len(self.queue) == 0)

    def size(self):
        return len(self.queue)

    # a string representation of this stack.
    def __str__(self):
        return str(self.queue)


class newStack(object):
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        self.queue1.enqueue(item)

    def pop(self):
        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())
        x = self.queue1.dequeue()
        while not self.queue2.isEmpty():
            self.queue1.enqueue(self.queue2.dequeue())
        return x

    def peek(self):
        while (self.queue1.size() > 1):
            self.queue2.enqueue(self.queue1.dequeue())
        x = self.queue1.dequeue()
        while not self.queue2.isEmpty():
            self.queue1.enqueue(self.queue2.dequeue())
        self.queue1.enqueue(x)
        return x

    def __str__(self):
        return str(self.queue1)
    

def main():
    my_stack = newStack()

    # Push 10
    start = time.time()
    my_stack.push(10)
    finish = time.time()
    print("PushTime: " + str(finish - start))
    print(my_stack)

    # Push 18
    my_stack.push(18)
    print(my_stack)


    # Push 1024
    my_stack.push(1024)
    print(my_stack)


    # pop() 
    start = time.time()
    print("pop()  ", my_stack.pop())
    finish = time.time()
    print("PopTime: " + str(finish - start))

    # peek()
    start = time.time()
    print("peek()  ", my_stack.peek())
    finish = time.time()
    print("PeekTime: " + str(finish - start))


    print("pop()  ", my_stack.pop())
    print("pop()  ", my_stack.pop())
    print("pop()  ", my_stack.pop())

if __name__ == "__main__":
    main()