#  File: LeftSum.py

#  Description: Get the left sum of the BST

#  Student Name: Abe Mankavil

#  Student UT EID: amm23896

#  Course Name: CS 313E

#  Unique Number: 86610


import sys


class Queue(object):
    def __init__(self):
        self.queue = []
    
    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)
    
    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)
    
    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)
    
    # return the size of the queue
    def size(self):
        return (len(self.queue))


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


def sumLeftHelper(root, level, max_level, result):
    #basecase of recur
    if root is None:
        return
    #checks if this node is first node on its level
    if max_level[0] < level:
        result[0] += root.data
        max_level[0] = level
    
    #recurse over left and right subtrees
    sumLeftHelper(root.lchild, level + 1, max_level, result)
    sumLeftHelper(root.rchild, level + 1, max_level, result)


def sumLeftView(root):
    max_level = [0]
    result = [0]
    sumLeftHelper(root, 1, max_level, result)
    return result[0]


class Tree(object):
    def __init__(self):
        self.root = None
    
    # insert data into the tree
    def insert(self, data):
        new_node = Node(data)
        
        if self.root == None:
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild
            
            # found location now insert node
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node
    
    def get_left_sum(self):
        return sumLeftView(self.root)


# ***There is no reason to change anything below this line***

def main():
    # Create tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree_input = list(map(int, line))  # converts elements into ints
    
    tree = Tree()
    for i in tree_input:
        tree.insert(i)
    
    print(tree.get_left_sum())


if __name__ == "__main__":
    main()
