# File: Anagrams.py

# Description: A program to group strings into anagram families

# Student Name: Abe Mankavil

# Student UT EID: amm23896

# Course Name: CS 313E

# Unique Number: 51130

# Output: True or False
from os import remove


def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Input: lst is a list of strings comprised of lowercase letters only
# Output: the number of anagram families formed by lst
def anagram_families(lst):
    
    ana_fam = {}
    for element in lst:
        if str(sorted(element)) in ana_fam:
            ana_fam[str(sorted(element))] +=1
        else:
            ana_fam[str(sorted(element))] = 1
    return len(ana_fam)

def main():
    # read the number of strings in the list
    num_strs = int(input())

    # add the input strings into a list
    lst = []
    for i in range(num_strs):
        lst += [input()]

    # compute the number of anagram families
    num_families = anagram_families(lst)

    # print the number of anagram families
    print(num_families)

if __name__ == "__main__":
    main()
