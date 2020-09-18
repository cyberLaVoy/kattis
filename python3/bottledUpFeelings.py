def knapsack0inf(items, maxCapacity):
    container = [float("-inf")]*(maxCapacity+1)
    container[0] = 0
    for itemValue, itemWeight in items:
        for j in range(len(container)):
            if j+itemWeight < len(container):
                container[j+itemWeight] = max(container[j+itemWeight], container[j] + itemValue)
    return container

def splitBetweenBottles(value, bothCount, v1, v2):
    count2 = 0
    while value % v1 != 0:
        value -= v2
        count2 += 1
    return bothCount-count2, count2 

def main():
    params = input().split()
    s = int(params[0])
    v1 = int(params[1])
    v2 = int(params[2])
    # reduction
    items = [(-1, v1), (-1, v2)]
    totalBottles = knapsack0inf(items, s)[-1]
    if totalBottles != float("-inf"):
        count1, count2 = splitBetweenBottles(s, abs(totalBottles), v1, v2)
        print(count1, count2)
    else:
        print("Impossible")

main()