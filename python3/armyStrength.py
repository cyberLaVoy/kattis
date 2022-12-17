
def winner(godzilla, mecha):
    while True:
        if len(godzilla) == 0:
            print("MechaGodzilla")
            return
        if len(mecha) == 0:
            print("Godzilla")
            return
        if godzilla[-1] == mecha[-1]:
            mecha.pop()
        elif godzilla[-1] > mecha[-1]:
            mecha.pop()
        else:
            godzilla.pop()

def solve():
    numTests = int(input())

    for i in range(numTests):
        input() # discard empty line
        input() # discard unnecessary parameters
        godzilla = input().split()
        mecha = input().split()
        godzilla = [int(x) for x in godzilla]
        mecha = [int(x) for x in mecha]
        godzilla.sort(reverse=True)
        mecha.sort(reverse=True)
        winner(godzilla, mecha)
solve()
