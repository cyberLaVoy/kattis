
def solve():
    n = int(input())

    helium = input().split()
    helium = [int(x) for x in helium]
    helium.sort()

    fractionsFilled = []
    for i in range(n):
        h = helium[i]
        b = i+1
        if h > b:
            print("impossible")
            return
        filledFraction = h/b
        fractionsFilled.append(filledFraction)

    minFilledFraction = min(fractionsFilled)
    print(minFilledFraction)
solve()