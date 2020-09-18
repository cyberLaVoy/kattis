

def solve():
    while True:
        N = int(input())
        if N == 0:
            break
        goalSum = 0 
        strN = str(N)
        for i in range(len(strN)):
            goalSum += int(strN[i])

        p = 11
        while True:
            digitSum = 0 
            candidate = str(N*p)
            for i in range(len(candidate)):
                digitSum += int(candidate[i])
            if goalSum == digitSum:
                print(p)
                break
            p += 1
solve()