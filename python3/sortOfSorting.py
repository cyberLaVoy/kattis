
def firstTwoCharacters(string):
    return string[:2]

def solve():
    numNames = int(input())
    while numNames != 0:
        names = []
        for i in range(numNames):
            name = input() 
            names.append(name)
        names.sort(key=firstTwoCharacters)
        for name in names:
            print(name)
        print()
        numNames = int(input())
solve()
