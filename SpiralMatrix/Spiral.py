#  File: Spiral.py

#  Description: Adjacent Sums in Spiral Matrix

#  Student Name: Abe Mankavil

#  Student UT EID: amm23896

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 1/25/22

#  Date Last Modified: 1/30/22

import sys

#Use of Function: returns list containing # of steps for each turn
def turn_magnitudes(n):
    x = []
    for num in range(1,n):
        x.append(num)
        x.append(num)
        #last top row diverges from previous pattern and maintains step-magnitude
        if num == n-1:
            x.append(num)
    return x

def create_spiral(n):
    #make odd dimensions
    if n % 2 == 0:
        n+=1
    #itereative direction steps in 4 directions
    right, down, left, up = (0,1),(1,0),(0,-1),(-1,0)
    cardinal_direct = [right, down, left, up]
    direct_index = 0   #tracks index of cardinal_direct

    table = [[None]*n for i in range(n)]  #intialize 2D array
    x,y = n//2, n//2
    table[y][x] = 1     #intializes center of matrix
    count = 2       #tracks and increments element values

    for steps in turn_magnitudes(n):
        for num in range(count, count+steps):
            y += cardinal_direct[direct_index][0]
            x += cardinal_direct[direct_index][1]
            table[y][x] = num
        count+=steps
        direct_index+=1
        if(direct_index == 4):
            direct_index = 0  
    return table

#helper method that uses discrete rings to traverse spiral aray and find indicies
def indexOf(spiral, n):
    #base case where 1 is always the center of matrix
    if n == 1:
        return len(spiral)//2, len(spiral)//2
    #set intial index to top right corner of spiral
    x = len(spiral)-1
    y = 0

    right, down, left, up = (0,1),(1,0),(0,-1),(-1,0)
    cardinal_direct = [down, left, up, right]
    direct_index = 0

    right_ring = False
    while(right_ring == False):
        if n <= spiral[y][x] and n > spiral[y+1][x-1]:
            right_ring = True
            steps = int((spiral[y][x]**(1/2))-1)
            #iterates around said ring of elements
            for i in range(1,(4*steps)+1):
                y += cardinal_direct[direct_index][0]
                x += cardinal_direct[direct_index][1]

                if(spiral[y][x] == n):
                    final_x = x
                    final_y = y
                if(i%steps == 0):
                    direct_index+=1        
        else:
            y+=1    #go one ring deeper towards center of matrix
            x-=1    
    return final_x,final_y


def sum_adjacent_numbers(spiral, n):
    (x,y) = indexOf(spiral, n)

    right, down, left, up = (0,1),(1,0),(0,-1),(-1,0)
    cardinal_direct = [down, left, up, right]
    direct_index = 0

    total = 0
    x+=1
    y-=1
    #sum up elements that form ring around given element
    for i in range(1,9):
        #checks for boundry cases where index could be out of bounds
        if x == len(spiral) or y == len(spiral) or x == -1 or y == -1:
            y += cardinal_direct[direct_index][0]
            x += cardinal_direct[direct_index][1]
            if(i%2 == 0):
                direct_index+=1
            continue
        total+=spiral[y][x]
        y += cardinal_direct[direct_index][0]
        x += cardinal_direct[direct_index][1]

        if(i%2 == 0):
            direct_index+=1 
    return total

def main():
    #.strip() ignores all possible blank lines at top and bottom of .in file
    x = sys.stdin.read().strip().split("\n")
    a = create_spiral(int(x[0]))
    #del(x[0])
    for i in x:
        if(i is x[0]):
            continue
        print(sum_adjacent_numbers(a,int(i)))
        
    

if __name__ == "__main__":
    main()