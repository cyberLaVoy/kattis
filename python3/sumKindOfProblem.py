
def sumAll(N):
    return int(N*((1+N)/2))
def sumOdd(N):
    return int(N*((1+(2*N-1))/2))
def sumEven(N):
    return int(N*((2+(2*N))/2))
def solve():
    numTests = int(input())
    for i in range(numTests):
        N = int(input().split()[1])
        print(i+1, sumAll(N), sumOdd(N), sumEven(N))
solve()