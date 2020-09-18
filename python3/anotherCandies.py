
numTests = int(input())

for i in range(numTests):
    input()
    numChildren = int(input())
    totalCandies = 0
    for j in range(numChildren):
        totalCandies += int(input())
    if totalCandies % numChildren == 0:
        print("YES")
    else:
        print("NO")

