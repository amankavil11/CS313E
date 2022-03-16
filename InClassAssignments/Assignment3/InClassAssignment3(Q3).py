import time
#PushTime: 1.9073486328125e-06
#PopTime: 5.0067901611328125e-06
#PeekTime: 2.86102294921875e-06
class Link(object):
  ''' This class represents a link between data items only'''
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data) + " --> " + str(self.next)



class LinkedList(object):
  ''' This class implements the operations of a simple linked list'''
  def __init__ (self):
    self.first = None

  def insertFirst (self, data):
    '''inset data at begining of a linked list'''
    newLink = Link(data)
    newLink.next = self.first
    self.first = newLink

  def insertLast (self, data):
    ''' Inset the data at the end of a linked list '''
    newLink = Link(data)
    current = self.first

    if (current == None):
      self.first = newLink
      return
    # find the last and insert it there. 
    while (current.next != None):
      current = current.next

    current.next = newLink

  def findLink(self, data):
    ''' find to which data is the link of a given data inside this linked list'''
    current = self.first
    if (current == None):
      return None

    # searcg and find the position of the given data, the get the link if. 
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  def deleteLink(self, data):
    ''' Removes the data from the list if exist and fix the link problems.'''

    current = self.first
    previous = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
    
      current = current.next

      if (current == self.first):
        self.first = self.first.next
      else:
        previous.next = current.next

    return current

  def __str__(self):
    return str(self.first)

class newStack2(object):
    def __init__(self):
        self.singly1 = LinkedList()
    def push(self, item):
        self.singly1.insertFirst(item)
    def peek(self):
        return self.singly1.first
    def pop(self):
        return self.singly1.deleteLink(self.peek())
    def __str__(self):
        return str(self.singly1)


def main():
    my_stack = newStack2()

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