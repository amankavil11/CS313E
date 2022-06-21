#  File: Adjacency.py
#  Description: Converts an edge list into an adjacency matrix
#  Student Name: Abe Mankavil
#  Student UT EID: amm23896
#  Course Name: CS 313E
#  Unique Number: 86610

def edge_to_adjacency(edge_list):
    vertex = []
    for i in range(len(edge_list)):
        vertex.append(edge_list[i][0])
        vertex.append(edge_list[i][1])
    vertex = sorted(set(vertex))
    vertex_dict = {}
    #map index to each specific string node on adj matrix
    for i in range(len(vertex)):
        vertex_dict[vertex[i]] = i
    
    #intialize zeros in NxN matrix
    adj_matrix = [[0 for i in range(len(vertex))] for j in range(len(vertex))]
    
    #add weights where necessary
    for weight in edge_list:
        adj_matrix[vertex_dict[weight[0]]][vertex_dict[weight[1]]] = weight[2]
    return  adj_matrix
        
    

# ------ DO NOT CHANGE BELOW HERE ------ #
import ast

def main():
    matrix = edge_to_adjacency(ast.literal_eval(input()))

    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))

if __name__ == "__main__":
    main()
