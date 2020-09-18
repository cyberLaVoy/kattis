
numTests = int(input())
for k in range(numTests):
    numCards = int(input())
    cards = []
    for i in range(numCards, 0, -1):
        cards.insert(0,i)
        for j in range(i):
            cards.insert(0,cards.pop())
    string = ""
    for l in cards:
        print(l, end=' ')
    print()
