
numTests = int(input())

for i in range(numTests):
    input()
    X = input().split()
    X = [int(x) for x in X]
    Y = input().split()
    Y = [int(y) for y in Y]
    X.sort()
    Y.sort(reverse=True)
    dotProduct = 0
    for j in range(len(X)):
        dotProduct += X[j]*Y[j]
    print("Case #" + str(i+1) + ':', dotProduct)
        