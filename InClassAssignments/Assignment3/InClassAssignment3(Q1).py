import time
#EnqueueTime: 9.5367431640625e-07
#DequeueTime: 9.775161743164062e-06

class Stack(object):

    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        if(not self.isEmpty()):
            return self.stack.pop()
        else:
            return None

    # check what item is on top of the stack without removing it
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # check if a stack is empty
    def isEmpty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))

    # a string representation of this stack.
    def __str__(self):
        return str(self.stack)


class newQueue(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())
        x = self.stack2.pop()
        while not self.stack2.isEmpty():
            self.stack1.push(self.stack2.pop())
        return x

    def __str__(self):
        return str(self.stack1)


def main():
    my_queue = newQueue()

    # enqueue 10
    my_queue.enqueue(10)
    print(my_queue)

    # enqueue 18
    start = time.time()
    my_queue.enqueue(18)
    finish = time.time()
    print(my_queue)
    print("EnqueueTime: " + str(finish - start))

    # enqueue 1024
    my_queue.enqueue(1024)
    print(my_queue)

    # dequeue()
    start = time.time()
    print("Dequeue ", my_queue.dequeue())
    finish = time.time()
    print("DequeueTime: " + str(finish - start))
    print("Dequeue ", my_queue.dequeue())
    print("Dequeue ", my_queue.dequeue())
    print("Dequeue ", my_queue.dequeue())


if __name__ == "__main__":
    main()
