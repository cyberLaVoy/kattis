
def knapsack01(items, maxCapacity):
    container = [float("-inf")]*(maxCapacity+1)
    container[0] = 0
    for itemValue, itemWeight in items:
        for j in range(len(container)-1, -1, -1):
            if j-itemWeight >= 0:
                container[j] = max(container[j], container[j-itemWeight] + itemValue)
    return container

def knapsack0k(items, maxCapacity):
    container = [float("-inf")]*(maxCapacity+1)
    container[0] = 0
    for weight in items:
        print(weight)
        print("****************")
        i = 0
        while i < weight:
            j = 0
            while j <= maxCapacity:
                print(j+i)
                j += weight
            i += 1



def main():
    goal = int(input())
    coinCounts = [int(x) for x in input().split()]
    coins = {}
    coins[1] = coinCounts[0]
    coins[5] = coinCounts[1]
    coins[10] = coinCounts[2]
    coins[25] = coinCounts[3]
    knapsack0k(coins, goal)
    """
    sums = knapsack01(coins, goal)
    if sums[-1] == float("-inf"):
        print("Impossible")
    else:
        print(sums[-1])
    """

if __name__ == "__main__":
    main()