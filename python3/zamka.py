
L = int(input())
D = int(input())
X = int(input())

def sumOfDigits(value):
    value = str(value)
    sumOfDigits = 0
    for i in range(len(value)):
        sumOfDigits += int(value[i])
    return sumOfDigits

for i in range(L,D+1):
    if sumOfDigits(i) == X:
        print(i)
        break
for j in range(D,L-1,-1):
    if sumOfDigits(j) == X:
        print(j)
        break