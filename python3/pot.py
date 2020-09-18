
numValues = int(input())

X = 0
for i in range(numValues):
    value = input()
    value = int(value[:-1])**int(value[len(value)-1])
    X += value
print(X)