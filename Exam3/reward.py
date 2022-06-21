#  File: reward.py

#  Description: The ABC staff decides to find the minimum number of gifts as each customer's reward.
#  Student Name:
#  Student UT EID:
#  Course Name: CS 313E
#  Unique Number:

import sys

max_val = 1000


def getmin(prices, T):
# Add your code here!




if __name__ == "__main__":

	# Read input list of prices for each gift
	prices_str = sys.stdin.readline().split()
	prices = [ int(x) for x in prices_str ]

	# Read total price that the customer spends
	T = int(sys.stdin.readline())

	print(getmin(prices, T))
