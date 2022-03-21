#  File: ExpressionTree.py
#  Description: Assignment 7

#  Student Name: Abe Mankavil

#  Student UT EID: amm23896

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 3/18/22

#  Date Last Modified:
import sys

operators = ['+', '-', '*', '/', '//', '%', '**']


class Stack(object):
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None
    
    def is_empty(self):
        return len(self.stack) == 0


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree(object):
    def __init__(self):
        self.root = Node()
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree(self, expr):
        current = self.root
        stack_tree = Stack()
        for token in expr.split():
            if token == '(':
                current.lChild = Node()
                stack_tree.push(current)
                current = current.lChild
            elif token in operators:
                current.data = token
                stack_tree.push(current)
                current.rChild = Node()
                current = current.rChild
            elif token == ')':
                if not stack_tree.is_empty():
                    current = stack_tree.pop()
            else:
                current.data = token
                current = stack_tree.pop()
    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
        if aNode is not None:
            l = self.evaluate(aNode.lChild)
            r = self.evaluate(aNode.rChild)
            if l is None or r is None:
                return aNode.data
            if aNode.data == '+':
                return float(l) + float(r)
            elif aNode.data == '*':
                return float(l) * float(r)
            elif aNode.data == '-':
                return float(l) - float(r)
            elif aNode.data == '**':
                return float(l) ** float(r)
            elif aNode.data == '//':
                return float(l) // float(r)
            elif aNode.data == '/':
                return float(l) / float(r)
            elif aNode.data == '%':
                return float(l) % float(r)
    
    # # this function should generate the preorder notation of
    # # the tree's expression
    # # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        if aNode is not None:
            l = self.pre_order(aNode.lChild)
            r = self.pre_order(aNode.rChild)
            if l is None or r is None:
                return aNode.data
            else:
                return aNode.data + " " + l + " " + r
    
    # # this function should generate the postorder notation of
    # # the tree's expression
    # # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        if aNode is not None:
            l = self.post_order(aNode.lChild)
            r = self.post_order(aNode.rChild)
            if l is None or r is None:
                return aNode.data + " "
            else:
                return l + r + aNode.data + " "


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
    
    tree = Tree()
    tree.create_tree(expr)
    
    #print(tree.print_tree(tree.root))  #remove
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))
    
    # # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())
    
    # # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
