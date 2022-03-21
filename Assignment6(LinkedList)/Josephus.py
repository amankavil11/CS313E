import sys


class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.last = None
    
    # Insert an element (value) in the list
    def insert(self, data):
        newLink = Link(data)
        if self.last is None:
            self.last = newLink
            self.last.next = self.last
        else:
            newLink.next = self.last.next
            self.last.next = newLink
            self.last = newLink
    
    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        Node = self.last
        if Node is None:
            return None
        if Node.data == data:
            return Node
        Node = Node.next
        while Node is not self.last:
            if Node.data == data:
                return Node
            else:
                Node = Node.next
        if Node.next == Node and Node.data == data:
            return Node
        return None
    
    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete(self, data):
        if self.find(data) is None:
            return None
        Node = self.last
        if Node.data == data:
            if Node is Node.next:
                delNode = Node
                self.last = None
                return delNode
            else:
                while Node.next is not self.last:
                    Node = Node.next
                delNode = Node.next
                self.last = Node
                Node.next = Node.next.next
                return delNode
        
        while Node.next is not self.last:
            if Node.next.data == data:
                delNode = Node.next
                Node.next = Node.next.next
                return delNode
            else:
                if Node.next.next is self.last and Node.next.data == data:
                    delNode = Node.next
                    Node.next = Node.next.next
                    return delNode
                Node = Node.next
    
    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after(self, start, n):
        Node = self.find(start)
        for i in range(n - 2):
            Node = Node.next
        delNode = self.delete(Node.next.data)
        return delNode, Node.next
    
    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        if self.last is None:
            return "[]"
        Node = self.last.next
        
        toString = "[" + str(Node)
        Node = Node.next
        while Node is not self.last.next:
            toString += ", " + str(Node)
            Node = Node.next
        return toString + "]"


def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)
    
    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)
    
    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)
    
    soldiers_linked = CircularList()
    for i in range(1, num_soldiers + 1):
        soldiers_linked.insert(i)
    while soldiers_linked.last is not None:
        del_soldier, new_start = soldiers_linked.delete_after(start_count, elim_num)
        print(del_soldier)
        start_count = new_start.data


if __name__ == "__main__":
    main()
