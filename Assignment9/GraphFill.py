#  File: GraphFill.py
#  Student Name: Abe Mankavil
#  Student UT EID: am23896
#  Course Name: CS 313E
#  Unique Number: 51130
#  Date Created: 4/3/22
#  Date Last Modified:

import os
import sys

# this enables printing colors on Windows somehow
os.system("")

# code to reset the terminal color
RESET_CHAR = "\u001b[0m"
# color codes for the terminal
COLOR_DICT = {
    "black":"\u001b[30m",
    "red":"\u001b[31m",
    "green":"\u001b[32m",
    "yellow":"\u001b[33m",
    "blue":"\u001b[34m",
    "magenta":"\u001b[35m",
    "cyan":"\u001b[36m",
    "white":"\u001b[37m"
}
# character code for a block
BLOCK_CHAR = "\u2588"


# Input: text is some string we want to write in a specific color
#   color is the name of a color that is looked up in COLOR_DICT
# Output: returns the string wrapped with the color code
def colored(text, color):
    color = color.strip().lower()
    if not color in COLOR_DICT:
        raise Exception(color + " is not a valid color!")
    return COLOR_DICT[color] + text


# Input: color is the name of a color that is looked up in COLOR_DICT
# prints a block (two characters) in the specified color
def print_block(color):
    print(colored(BLOCK_CHAR, color) * 2, end='')


# Stack class; you can use this for your search algorithms
class Stack(object):
    def __init__(self):
        self.stack = []
    
    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)
    
    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()
    
    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]
    
    # check if the stack if empty
    def is_empty(self):
        return len(self.stack) == 0
    
    # return the number of elements in the stack
    def size(self):
        return len(self.stack)


# Queue class; you can use this for your search algorithms
class Queue(object):
    def __init__(self):
        self.queue = []
    
    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)
    
    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)
    
    # checks the item at the top of the Queue
    def peek(self):
        return self.queue[0]
    
    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0
    
    # return the size of the queue
    def size(self):
        return len(self.queue)


# class for a graph node; contains x and y coordinates, a color, a list of edges and
# a flag signaling if the node has been visited (useful for search algorithms)
# it also contains a "previous color" attribute. This might be useful for your flood fill implementation.
class ColorNode:
    # Input: x, y are the location of this pixel in the image
    #   color is the name of a color
    def __init__(self, x, y, color):
        self.color = color
        self.prev_color = color
        self.x = x
        self.y = y
        self.edges = []
        self.visited = False
    
    # Input: node_index is the index of the node we want to create an edge to in the node list
    # adds an edge and sorts the list of edges
    def add_edge(self, node_index):
        self.edges.append(node_index)
        self.edges.sort()
    
    # Input: color is the name of the color the node should be colored in;
    # the function also saves the previous color (might be useful for your flood fill implementation)
    def set_color(self, color):
        self.prev_color = self.color
        self.color = color


# class that contains the graph
class ImageGraph:
    def __init__(self, image_size):
        self.nodes = []
        self.image_size = image_size
    
    # prints the image formed by the nodes on the command line
    def print_image(self):
        img = [["black" for i in range(self.image_size)] for j in range(self.image_size)]
        
        # fill img array
        for node in self.nodes:
            img[node.y][node.x] = node.color
        
        for line in img:
            for pixel in line:
                print_block(pixel)
            print()
        # print new line/reset color
        print(RESET_CHAR)
    
    # sets the visited flag to False for all nodes
    def reset_visited(self):
        for i in range(len(self.nodes)):
            self.nodes[i].visited = False
    
    # implement your adjacency matrix printing here.
    def print_adjacency_matrix(self):
        print("Adjacency matrix:")
        for node in self.nodes:
            row = ""
            for i in range(len(self.nodes)):
                if i in node.edges:
                    row += "1"
                else:
                    row += "0"
            print(row)
        # empty line afterwards
        print()
    
    # implement your bfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with
    def bfs(self, start_index, color):
        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting BFS; initial state:")
        self.print_image()
        s = self.nodes[start_index]
        replace_color = s.color
        s.set_color(color)
        gray_queue = Queue()
        gray_queue.enqueue(s)
        self.print_image()
        while not gray_queue.is_empty():
            u_vert = gray_queue.dequeue()
            for adj in u_vert.edges:
                if self.nodes[adj].color == replace_color:
                    self.nodes[adj].set_color(color)
                    gray_queue.enqueue(self.nodes[adj])
                    self.print_image()
                    
    # implement your dfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with
    def dfs(self, start_index, color):
        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting DFS; initial state:")
        self.print_image()
        s = self.nodes[start_index]
        replace_color = s.color
        visited_stack = Stack()
        s.set_color(color)
        visited_stack.push(s)
        while not visited_stack.is_empty():
            v = visited_stack.pop()
            if not v.visited:
                v.visited = True
                v.set_color(color)
                self.print_image()
                for adj in v.edges[::-1]:
                    if not self.nodes[adj].visited and self.nodes[adj].color == replace_color:
                        visited_stack.push(self.nodes[adj])


def main():
    size = int(sys.stdin.readline())
    graph = ImageGraph(size)
    for i in range(int(sys.stdin.readline())):
        node_chars = sys.stdin.readline().split(",")
        graph.nodes.append(ColorNode(int(node_chars[0]), int(node_chars[1]), node_chars[2]))
    for i in range(int(sys.stdin.readline())):
        edges = sys.stdin.readline().split(",")
        graph.nodes[int(edges[0])].add_edge(int(edges[1]))
        graph.nodes[int(edges[1])].add_edge(int(edges[0]))
    BFSsource_vert = sys.stdin.readline().split(",")
    bfs_start = int(BFSsource_vert[0])
    bfs_color = BFSsource_vert[1]
    DFSsource_vert = sys.stdin.readline().split(",")
    dfs_start = int(DFSsource_vert[0])
    dfs_color = DFSsource_vert[1]
    
    #print matrix
    graph.print_adjacency_matrix()
    
    # # run bfs
    graph.bfs(bfs_start, bfs_color)
    #
    # # run dfs
    graph.dfs(dfs_start, dfs_color)


if __name__ == "__main__":
    main()
