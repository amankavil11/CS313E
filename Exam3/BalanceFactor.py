#  File: BalanceFactor.py

#  Description: Determines the balance factor of a binary tree

#  Student Name: Abe Mankavil

#  Student UT EID: amm23896

#  Course Name: CS 313E

#  Unique Number: 86610



class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def getHeight(node):
    #check for single node aka leaf
    if node is None:
        return -1
    else:
        leftHeight = getHeight(node.left)
        rightHeight = getHeight(node.right)
        
        #compare left vs right for length
        if leftHeight < rightHeight:
            return 1 + rightHeight
        else:
            return 1 + leftHeight
            
def balance_factor(node):
    return getHeight(node.right) - getHeight(node.left)

# ------ DO NOT CHANGE BELOW HERE ------ #
import pickle
import sys


def main():
    data_in = ''.join(sys.stdin.readlines())
    node = pickle.loads(str.encode(data_in))

    print(balance_factor(node))


if __name__ == "__main__":
    main()
