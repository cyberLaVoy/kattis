
def solve():
    params = input().split()

    numParts = int(params[0])
    days = int(params[1])
    uniqueParts = {}

    for i in range(days):
        part = input()
        uniqueParts[part] = "replaced"
        if len(uniqueParts) == numParts:
            print(i+1)
            return
    print("paradox avoided")
solve()

