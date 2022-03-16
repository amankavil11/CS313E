import sys
import time
import math


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series(v, k):
  sum = v
  p = 1
  for i in range(int(math.log(v,k))):
    sum+= v//(k**p)
    p+=1
  return sum

#inefficient sum_series
def sum_series2(v,k):
  sum = 0
  p = 0
  while(v//(k**p) > 0):
    sum+=v//(k**p)
    p+=1
  return sum
  



# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  if k >= n:
    return n
  for i in range(1,n):
    if (sum_series(i,k)) == n or (sum_series(i,k)) == n+1:
      return i

    


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
  if k >= n:
    return n
  left, right = 0, n-1
  while(left <= right):
    middle = (left + right) // 2
    if sum_series(middle,k) == n or (sum_series(middle,k)) == n+1:
      if sum_series(middle,k) == n+1:
        if abs(n-sum_series(middle,k)) > abs(n-sum_series(middle-1,k)):
          return middle-1
        else:
          return middle
      else:
        return middle
    if sum_series(middle,k) < n:
      left = middle + 1
    if sum_series(middle,k) > n:
      right = middle - 1
    


def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int(line)

  for i in range(num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp = line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()
  
if __name__ == "__main__":
  main()
