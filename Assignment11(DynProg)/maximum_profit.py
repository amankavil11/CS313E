import sys


# Add Your functions here
def get_profit(price, increase):
    return price * (increase / 100)


def knapsack(prices, increase, num_houses, money):
    DFTable = [[0 for i in range(money + 1)] for j in range(num_houses + 1)]
    for i in range(1, num_houses + 1):
        for j in range(money + 1):
            if prices[i-1] <= j:
                DFTable[i][j] = max(DFTable[i - 1][j], increase[i-1] + DFTable[i - 1][j - prices[i-1]])
            else:
                DFTable[i][j] = DFTable[i - 1][j]
    return DFTable[num_houses][money]


def main():
    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)
    # The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)
    
    # The third line is a list of house prices in million dollar which is a list of \textit{integer numbers} (
    # Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])
    
    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])
        increase[i] = get_profit(prices[i], increase[i])
    # Add your implementation here ....
    result = knapsack(prices, increase, num_houses, money)
    
    # Add your functions and call them to generate the result.
    
    print(int(result*100)/100)


main()
