
def willSolve(cases):
    for case in cases:
        for i in range(1, len(case)):
            if ord(case[i]) >= 65 and ord(case[i]) <= 90:
                return False
    return True

def solve():
    params = input().split()

    numProblems = int(params[0])
    numTests = int(params[1])

    solved = 0
    for i in range(numProblems):
        cases = []
        for j in range(numTests):
            cases.append(input())
        if willSolve(cases):
            solved += 1
    print(solved)
solve()