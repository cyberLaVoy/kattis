import math

def isPrime(value):
    if value == 1:
        return False
    if value & 1 != 1:
        return False
    for i in range(3,math.ceil(math.sqrt(value))+1,2):
        if value % i == 0:
            return False
    return True

def sumOfSquaredDigits(value):
    value = str(value)
    total = 0
    for v in value:
        total += int(v)**2
    return total


def isHappy(value):
    sums = {}
    while True:
        value = sumOfSquaredDigits(value)
        if value == 1:
            return True
        if value in sums:
            return False
        sums[value] = "Found"
    

def solve():
    numTests = int(input())

    for i in range(numTests):
        params = input().split()
        value = int(params[1])
        if not isPrime(value):
            print(params[0], value, "NO")
        else:
            if isHappy(value):
                print(params[0], value, "YES")
            else:
                print(params[0], value, "NO")
solve()
    
