#  File: Cipher.py

#  Description: Encrypt and Decrypt Algo

#  Student Name: Abe Mankavil

#  Student UT EID: amm23896

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 2/1/22

#  Date Last Modified: 2/5/22
import math
import sys

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
# 
def encrypt(strng):
    dimension = math.ceil(len(strng)**(1/2))    #sets dimension of 2D Matrix
    table = [[None]*dimension for i in range(dimension)]
    copy = list(strng)      #make copy of string so as not to lose string data
    for i in range(dimension):
        for j in range(dimension):  
            if len(copy) != 0:      #adds first letter in copy to matrix
                table[i][j] = copy.pop(0)
            else:
                table[i][j] = "*"  
    table = list(zip(*table[::-1])) #takes each row of table and revereses order and then zips each column together
    messageList = [x for line in table for x in line if x != '*']
    return ''.join(messageList)
        

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt(strng):
    dimension = math.ceil(len(strng)**(1/2))
    num_stars = (dimension**(2))-len(strng)  #find number of '*' to put in matrix
    table = [[None]*dimension for i in range(dimension)]
    star_indexy = -1
    star_indexx = 0
    copy = list(strng)
    #for-loop to add necessary # of '*' placeholders
    for star in range(num_stars):
        table[star_indexy][star_indexx] = "*"
        star_indexy-=1
        if(star_indexy == -1*(dimension+1)):    #checks for out of bounds index
            star_indexy = -1
            star_indexx += 1
    for i in range(dimension):
        for j in range(dimension):
            if table[i][j] == '*':  #bypasses any '*' already in matrix
                continue
            if len(copy) != 0:
                table[i][j] = copy.pop(0)
    table = list(zip(*table))[::-1] #zips each column together and then takes each row of table and revereses order
    messageList = [x for line in table for x in line if x != '*']
    return ''.join(messageList)



def main():
    x = sys.stdin.read().split("\n")
    print(encrypt(x[0]))
    print(decrypt(x[1]))

if __name__ == "__main__":
  main()


