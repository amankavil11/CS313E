#  File: TestBinaryTree.py

#  Description: Extending Binary Tree and Node Class from lecture

#  Student Name: Abe Mankavil

#  Student UT EID: amm23896

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 03/27/22

#  Date Last Modified:

import sys

class Node(object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None
    
    def print_node(self, level=0):
        
        if self.rChild:
            self.rChild.print_node(level + 1)
        
        print(' ' * 3 * level + '->', self.data)
        
        if self.lChild:
            self.lChild.print_node(level + 1)
    
    def get_level(self, level, lvl_lst):
        temp_lvl = level
        current = self
        if temp_lvl == 0:
            lvl_lst += [current]
        else:
            if not current.lChild and not current.rChild and level != 0:
                lvl_lst += []
            if temp_lvl != 0 and current.lChild:
                current.lChild.get_level(temp_lvl - 1, lvl_lst)
            temp_lvl = level
            if temp_lvl != 0 and current.rChild:
                current.rChild.get_level(temp_lvl - 1, lvl_lst)
    
    def get_height(self):
        if self.lChild is not None and self.rChild is not None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild is not None:
            return 1 + self.lChild.get_height()
        elif self.rChild is not None:
            return 1 + self.rChild.get_height()
        else:
            return 1


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None
    
    def print(self, level):
        self.root.print_node(level)
    
    def get_height(self):
        return self.root.get_height()
    
    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return
    
    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        parent = self.root
        #checking for empty tree
        if not parent:
            return None
        #checking for tree with only root node
        if not parent.lChild and not parent.rChild:
            return 0
        current = self.root
        #tree with a root that has two seperate branches
        if current.rChild and current.lChild:
            while current.lChild:
                current = current.lChild
            min = current.data
            current = parent
            while current.rChild:
                current = current.rChild
            max = current.data
            return max - min
        #for case when tree only has right branch
        if current.rChild:
            min = current.data
            while current.rChild:
                current = current.rChild
            max = current.data
            return max - min
        #for case when tree only has left branch
        if current.lChild:
            max = current.data
            while current.lChild:
                current = current.lChild
            min = current.data
            return max - min
    
    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        if not self.root:
            return []
        lvl_lst = []
        self.root.get_level(level, lvl_lst)
        return lvl_lst
    
    # # Returns the list of the node that you see from left side
    # # The order of the output should be from top to down
    def left_side_view(self):
        if not self.root:
            return []
        left_lst = []
        for level in range(self.get_height()):
            left_lst += [self.get_level(level)[0].data]
        return left_lst
        
         

    # # returns the sum of the value of all leaves.
    # # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        pass


def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    a = Tree()
    # for i in range(12,20):
    #     a.insert((i))
    # r = [55, 8, 70, 2, 25, 63, 75, 68, 73, 80, 79]
    r = [1,2,3,4,5]
    for i in r:
        a.insert((i))
    #a.print(1)
    print(a.get_level(3))
    #print(a.left_side_view())
    
    # Create three trees - two are the same and the third is different
    # line = sys.stdin.readline()
    # line = line.strip()
    # line = line.split()
    # tree1_input = list(map(int, line)) 	# converts elements into ints
    # t1 = make_tree(tree1_input)
    # t1.print(t1.get_height())
    #
    # print("Tree range is: ",   t1.range())
    # print("Tree left side view is: ", t1.left_side_view())
    # print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    # print("##########################")


# # Another Tree for test.
#     line = sys.stdin.readline()
#     line = line.strip()
#     line = line.split()
#     tree2_input = list(map(int, line)) 	# converts elements into ints
#     t2 = make_tree(tree2_input)
#     t2.print(t2.get_height())
#
#     print("Tree range is: ",   t2.range())
#     print("Tree left side view is: ", t2.left_side_view())
#     print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
#     print("##########################")
# # Another Tree
#     line = sys.stdin.readline()
#     line = line.strip()
#     line = line.split()
#     tree3_input = list(map(int, line)) 	# converts elements into ints
#     t3 = make_tree(tree3_input)
#     t3.print(t3.get_height())
#
#     print("Tree range is: ",   t3.range())
#     print("Tree left side view is: ", t3.left_side_view())
#     print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
#     print("##########################")


if __name__ == "__main__":
    main()
