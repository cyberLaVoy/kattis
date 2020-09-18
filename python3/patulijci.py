from random import shuffle

def findSubset(nums, matrix, goal):
    subset = []
    possible = matrix[len(matrix)-1][goal]
    if not possible:
        return subset
    i = len(matrix)-1
    while goal != 0:
        if i == 0 or not matrix[i-1][goal]:
            goal -= nums[i]
            subset.append(nums[i])
        i -= 1
    return subset
    
def subsetSum(nums, goal):
    matrix = []
    for i in range(len(nums)):
        matrix.append([0]*(goal+1))
    for i in range(len(matrix)):
        matrix[i][0] = 1
    if nums[0] <= goal:
        matrix[0][nums[0]] = 1
    for i in range(1, len(nums)):
        for j in range(1, goal+1):
            if nums[i] <= j:
                matrix[i][j] = matrix[i-1][j-nums[i]] or matrix[i-1][j]
            else:
                matrix[i][j] = matrix[i-1][j]
    return findSubset(nums, matrix, goal)


def solve():
    dwarfs = []
    for i in range(9):
        dwarf = int(input())
        dwarfs.append(dwarf)
    lineup = dwarfs[:]
    dwarfs.sort()
    subset = subsetSum(dwarfs, 100)
    exclude = 0
    while len(subset) != 7:
        shuffle(dwarfs)
        subset = subsetSum(dwarfs, 100)
    for dwarf in lineup:
        if dwarf in subset:
            print(dwarf)
solve()