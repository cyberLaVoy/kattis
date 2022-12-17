
numTest = int(input())

for i in range(numTest):
    num = int(input())
    if num & 1 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")